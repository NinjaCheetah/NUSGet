# "modules/download_dsi.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah

import pathlib

import libTWLPy


def run_nus_download_dsi(out_folder: pathlib.Path, tid: str, version: str, pack_tad_chkbox: bool, keep_enc_chkbox: bool,
                         decrypt_contents_chkbox: bool, use_local_chkbox: bool, tad_file_name: str,
                         progress_callback=None):
    # Actual NUS download function that runs in a separate thread, but DSi flavored.
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
    pack_tad_enabled = pack_tad_chkbox
    decrypt_contents_enabled = decrypt_contents_chkbox
    # Create a new libTWLPy Title.
    title = libTWLPy.Title()
    # Make a directory for this title if it doesn't exist.
    title_dir = out_folder.joinpath(tid)
    title_dir.mkdir(exist_ok=True)
    # Announce the title being downloaded, and the version if applicable.
    if title_version is not None:
        progress_callback.emit(0, 0, f"Downloading title {tid} v{title_version}, please wait...")
    else:
        progress_callback.emit(0, 0, f"Downloading title {tid} vLatest, please wait...")
    progress_callback.emit(-1, -1, " - Downloading and parsing TMD...")
    # Download a specific TMD version if a version was specified, otherwise just download the latest TMD.
    try:
        if title_version is not None:
            title.load_tmd(libTWLPy.download_tmd(tid, title_version))
        else:
            title.load_tmd(libTWLPy.download_tmd(tid))
            title_version = title.tmd.title_version
    # If libTWLPy returns an error, that means that either the TID or version doesn't exist, so return code -2.
    except ValueError:
        return -2
    # Make a directory for this version if it doesn't exist.
    version_dir = title_dir.joinpath(str(title_version))
    version_dir.mkdir(exist_ok=True)
    # Write out the TMD to a file.
    version_dir.joinpath(f"tmd.{title_version}").write_bytes(title.tmd.dump())
    # Use a local ticket, if one exists and "use local files" is enabled.
    if use_local_chkbox and version_dir.joinpath("tik").exists():
        progress_callback.emit(-1, -1, " - Parsing local copy of Ticket...")
        title.load_ticket(version_dir.joinpath("tik").read_bytes())
    else:
        progress_callback.emit(-1, -1, " - Downloading and parsing Ticket...")
        try:
            title.load_ticket(libTWLPy.download_ticket(tid))
            version_dir.joinpath("tik").write_bytes(title.ticket.dump())
        except ValueError:
            # If libTWLPy returns an error, then no ticket is available. Log this, and disable options requiring a
            # ticket so that they aren't attempted later.
            progress_callback.emit(-1, -1, "  - No Ticket is available!")
            pack_tad_enabled = False
            decrypt_contents_enabled = False
    # Load the content record from the TMD, and download the content it lists. DSi titles only have one content.
    title.load_content_records()
    content_file_name = f"{title.tmd.content_record.content_id:08X}"
    # Check for a local copy of the current content if "use local files" is enabled, and use it.
    if use_local_chkbox and version_dir.joinpath(content_file_name).exists():
        progress_callback.emit(-1, -1, " - Using local copy of content")
        content = version_dir.joinpath(content_file_name).read_bytes()
    else:
        progress_callback.emit(-1, -1, f" - Downloading content (Content ID: {title.tmd.content_record.content_id}, Size: "
                               f"{title.tmd.content_record.content_size} bytes)...")
        content = libTWLPy.download_content(tid, title.tmd.content_record.content_id)
        progress_callback.emit(-1, -1, "   - Done!")
        # If keep encrypted contents is on, write out the content after its downloaded.
        if keep_enc_chkbox is True:
            version_dir.joinpath(content_file_name).write_bytes(content)
    title.content.content = content
    # If decrypt local contents is still true, decrypt the content and write out the decrypted file.
    if decrypt_contents_enabled is True:
        try:
            progress_callback.emit(-1, -1, f" - Decrypting content (Content ID: {title.tmd.content_record.content_id})...")
            dec_content = title.get_content()
            content_file_name = f"{title.tmd.content_record.content_id:08X}.app"
            version_dir.joinpath(content_file_name).write_bytes(dec_content)
        except ValueError:
            # If libWiiPy throws an error during decryption, return code -3. This should only be possible if using
            # local encrypted contents that have been altered at present.
            return -3
    # If pack TAD is still true, pack the TMD, ticket, and content into a TAD.
    if pack_tad_enabled is True:
        # Get the TAD certificate chain, courtesy of libTWLPy.
        progress_callback.emit(-1, -1, " - Building certificate...")
        title.tad.set_cert_data(libTWLPy.download_cert())
        # Use a typed TAD name if there is one, and auto generate one based on the TID and version if there isn't.
        progress_callback.emit(-1, -1, "Packing TAD...")
        if tad_file_name != "" and tad_file_name is not None:
            # Batch downloads may insert -vLatest, so if it did we can fill in the real number now.
            tad_file_name = tad_file_name.replace("-vLatest", f"-v{title_version}")
            if tad_file_name[-4:].lower() != ".tad":
                tad_file_name += ".tad"
        else:
            tad_file_name = f"{tid}-v{title_version}.tad"
        # Certain special characters are prone to breaking things, so strip them from the file name before actually
        # opening the file for writing. On some platforms (like macOS), invalid characters get replaced automatically,
        # but on Windows the file will just fail to be written out at all.
        tad_file_name = tad_file_name.translate({ord(c): None for c in '/\\:*"?<>|'})
        # Have libTWLPy dump the TAD, and write that data out.
        version_dir.joinpath(tad_file_name).write_bytes(title.dump_tad())
    progress_callback.emit(0, 1, "Download complete!")
    # This is where the variables come in. If the state of these variables doesn't match the user's choice by this
    # point, it means that they enabled decryption or TAD packing for a title that doesn't have a ticket. Return
    # code 1 so that a warning popup is shown informing them of this.
    if (not pack_tad_enabled and pack_tad_chkbox) or (not decrypt_contents_enabled and decrypt_contents_chkbox):
        return 1
    return 0
