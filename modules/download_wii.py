# "modules/download_wii.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah & Contributors

import pathlib

import libWiiPy


def run_nus_download_wii(out_folder: pathlib.Path, tid: str, version: str, pack_wad_chkbox: bool, keep_enc_chkbox: bool,
                         decrypt_contents_chkbox: bool, wiiu_nus_chkbox: bool, use_local_chkbox: bool,
                         repack_vwii_chkbox: bool, patch_ios: bool, wad_file_name: str, progress_callback=None):
    # Actual NUS download function that runs in a separate thread.
    # Immediately knock out any invalidly formatted Title IDs.
    if len(tid) != 16:
        return -1
    # An error here is acceptable, because it may just mean the box is empty. Or the version string is nonsense.
    # Either way, just fall back on downloading the latest version of the title.
    try:
        title_version = int(version)
    except ValueError:
        title_version = None
    # Set variables for these two options so that their state can be compared against the user's choices later.
    pack_wad_enabled = pack_wad_chkbox
    decrypt_contents_enabled = decrypt_contents_chkbox
    # Check whether we're going to be using the (faster) Wii U NUS or not.
    wiiu_nus_enabled = wiiu_nus_chkbox
    # Create a new libWiiPy Title.
    title = libWiiPy.title.Title()
    # Make a directory for this title if it doesn't exist.
    title_dir = out_folder.joinpath(tid)
    title_dir.mkdir(exist_ok=True)
    # Announce the title being downloaded, and the version if applicable.
    if title_version is not None:
        progress_callback.emit(f"Downloading title {tid} v{title_version}, please wait...")
    else:
        progress_callback.emit(f"Downloading title {tid} vLatest, please wait...")
    progress_callback.emit(" - Downloading and parsing TMD...")
    # Download a specific TMD version if a version was specified, otherwise just download the latest TMD.
    try:
        if title_version is not None:
            title.load_tmd(libWiiPy.title.download_tmd(tid, title_version, wiiu_endpoint=wiiu_nus_enabled))
        else:
            title.load_tmd(libWiiPy.title.download_tmd(tid, wiiu_endpoint=wiiu_nus_enabled))
            title_version = title.tmd.title_version
    # If libWiiPy returns an error, that means that either the TID or version doesn't exist, so return code -2.
    except ValueError:
        return -2
    # Make a directory for this version if it doesn't exist.
    version_dir = title_dir.joinpath(str(title_version))
    version_dir.mkdir(exist_ok=True)
    # Write out the TMD to a file.
    version_dir.joinpath(f"tmd.{title_version}").write_bytes(title.tmd.dump())
    # Use a local ticket, if one exists and "use local files" is enabled.
    if use_local_chkbox and version_dir.joinpath("tik").exists():
        progress_callback.emit(" - Parsing local copy of Ticket...")
        title.load_ticket(version_dir.joinpath("tik").read_bytes())
    else:
        progress_callback.emit(" - Downloading and parsing Ticket...")
        try:
            title.load_ticket(libWiiPy.title.download_ticket(tid, wiiu_endpoint=wiiu_nus_enabled))
            version_dir.joinpath("tik").write_bytes(title.ticket.dump())
        except ValueError:
            # If libWiiPy returns an error, then no ticket is available. Log this, and disable options requiring a
            # ticket so that they aren't attempted later.
            progress_callback.emit("  - No Ticket is available!")
            pack_wad_enabled = False
            decrypt_contents_enabled = False
    # Load the content records from the TMD, and begin iterating over the records.
    title.load_content_records()
    content_list = []
    for content in range(len(title.tmd.content_records)):
        # Generate the correct file name by converting the content ID into hex.
        content_file_name = f"{title.tmd.content_records[content].content_id:08X}"
        # Check for a local copy of the current content if "use local files" is enabled, and use it.
        if use_local_chkbox is True and version_dir.joinpath(content_file_name).exists():
            progress_callback.emit(f" - Using local copy of content {content + 1} of {len(title.tmd.content_records)}")
            content_list.append(version_dir.joinpath(content_file_name).read_bytes())
        else:
            progress_callback.emit(f" - Downloading content {content + 1} of {len(title.tmd.content_records)} "
                                   f"(Content ID: {title.tmd.content_records[content].content_id}, Size: "
                                   f"{title.tmd.content_records[content].content_size} bytes)...")
            content_list.append(libWiiPy.title.download_content(tid, title.tmd.content_records[content].content_id,
                                                                wiiu_endpoint=wiiu_nus_enabled))
            progress_callback.emit("   - Done!")
            # If keep encrypted contents is on, write out each content after its downloaded.
            if keep_enc_chkbox is True:
                version_dir.joinpath(content_file_name).write_bytes(content_list[content])
    title.content.content_list = content_list
    # If decrypt local contents is still true, decrypt each content and write out the decrypted file.
    if decrypt_contents_enabled is True:
        try:
            for content in range(len(title.tmd.content_records)):
                progress_callback.emit(f" - Decrypting content {content + 1} of {len(title.tmd.content_records)} "
                                       f"(Content ID: {title.tmd.content_records[content].content_id})...")
                dec_content = title.get_content_by_index(content)
                content_file_name = f"{title.tmd.content_records[content].content_id:08X}.app"
                version_dir.joinpath(content_file_name).write_bytes(dec_content)
        except ValueError:
            # If libWiiPy throws an error during decryption, return code -3. This should only be possible if using
            # local encrypted contents that have been altered at present.
            return -3
    # If pack WAD is still true, pack the TMD, ticket, and contents all into a WAD.
    if pack_wad_enabled is True:
        # If the option to pack for vWii mode instead of Wii U mode is enabled, then the Title Key needs to be
        # re-encrypted with the common key instead of the vWii key, so that the title can be installed from within
        # vWii mode. (vWii mode does not have access to the vWii key, only Wii U mode has that.)
        if repack_vwii_chkbox is True and (tid[3] == "7" or tid[7] == "7"):
            progress_callback.emit(" - Re-encrypting Title Key with the common key...")
            title_key_common = libWiiPy.title.encrypt_title_key(title.ticket.get_title_key(), 0, title.tmd.title_id)
            title.ticket.common_key_index = 0
            title.ticket.title_key_enc = title_key_common
        # Get the WAD certificate chain, courtesy of libWiiPy.
        progress_callback.emit(" - Building certificate...")
        title.load_cert_chain(libWiiPy.title.download_cert_chain(wiiu_endpoint=wiiu_nus_enabled))
        # Use a typed WAD name if there is one, and auto generate one based on the TID and version if there isn't.
        progress_callback.emit(" - Packing WAD...")
        if wad_file_name != "" and wad_file_name is not None:
            # Batch downloads may insert -vLatest, so if it did we can fill in the real number now.
            wad_file_name = wad_file_name.replace("-vLatest", f"-v{title_version}")
            if wad_file_name[-4:].lower() != ".wad":
                wad_file_name += ".wad"
        else:
            wad_file_name = f"{tid}-v{title_version}.wad"
        # If enabled (after we make sure it's an IOS), apply all main IOS patches.
        if patch_ios and (tid[:8] == "00000001" and int(tid[-2:], 16) > 2):
            progress_callback.emit("   - Patching IOS...")
            ios_patcher = libWiiPy.title.IOSPatcher()
            ios_patcher.load(title)
            patch_count = ios_patcher.patch_all()
            if patch_count > 0:
                progress_callback.emit(f"   - Applied {patch_count} patches!")
            else:
                progress_callback.emit("   - No patches could be applied! Is this a stub IOS?")
            title = ios_patcher.dump()
            # Append "-PATCHED" to the end of the WAD file name to make it clear that it was modified.
            wad_file_name = wad_file_name[:-4] + "-PATCHED" + wad_file_name[-4:]
        # Certain special characters are prone to breaking things, so strip them from the file name before actually
        # opening the file for writing. On some platforms (like macOS), invalid characters get replaced automatically,
        # but on Windows the file will just fail to be written out at all.
        wad_file_name = wad_file_name.translate({ord(c): None for c in '/\\:*"?<>|'})
        # Have libWiiPy dump the WAD, and write that data out.
        version_dir.joinpath(wad_file_name).write_bytes(title.dump_wad())
    progress_callback.emit("Download complete!")
    # This is where the variables come in. If the state of these variables doesn't match the user's choice by this
    # point, it means that they enabled decryption or WAD packing for a title that doesn't have a ticket. Return
    # code 1 so that a warning popup is shown informing them of this.
    if (not pack_wad_enabled and pack_wad_chkbox) or (not decrypt_contents_enabled and decrypt_contents_chkbox):
        return 1
    return 0
