# "modules/download_dsi.py", licensed under the MIT license
# Copyright 2024 NinjaCheetah

import os
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
    title_dir = pathlib.Path(os.path.join(out_folder, tid))
    if not title_dir.is_dir():
        title_dir.mkdir()
    # Announce the title being downloaded, and the version if applicable.
    if title_version is not None:
        progress_callback.emit("Downloading title " + tid + " v" + str(title_version) + ", please wait...")
    else:
        progress_callback.emit("Downloading title " + tid + " vLatest, please wait...")
    progress_callback.emit(" - Downloading and parsing TMD...")
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
    version_dir = pathlib.Path(os.path.join(title_dir, str(title_version)))
    if not version_dir.is_dir():
        version_dir.mkdir()
    # Write out the TMD to a file.
    tmd_out = open(os.path.join(version_dir, "tmd." + str(title_version)), "wb")
    tmd_out.write(title.tmd.dump())
    tmd_out.close()
    # Use a local ticket, if one exists and "use local files" is enabled.
    if use_local_chkbox is True and os.path.exists(os.path.join(version_dir, "tik")):
        progress_callback.emit(" - Parsing local copy of Ticket...")
        local_ticket = open(os.path.join(version_dir, "tik"), "rb")
        title.load_ticket(local_ticket.read())
    else:
        progress_callback.emit(" - Downloading and parsing Ticket...")
        try:
            title.load_ticket(libTWLPy.download_ticket(tid))
            ticket_out = open(os.path.join(version_dir, "tik"), "wb")
            ticket_out.write(title.ticket.dump())
            ticket_out.close()
        except ValueError:
            # If libTWLPy returns an error, then no ticket is available. Log this, and disable options requiring a
            # ticket so that they aren't attempted later.
            progress_callback.emit("  - No Ticket is available!")
            pack_tad_enabled = False
            decrypt_contents_enabled = False
    # Load the content record from the TMD, and download the content it lists. DSi titles only have one content.
    title.load_content_records()
    content_file_name = hex(title.tmd.content_record.content_id)[2:]
    while len(content_file_name) < 8:
        content_file_name = "0" + content_file_name
    # Check for a local copy of the current content if "use local files" is enabled, and use it.
    if use_local_chkbox is True and os.path.exists(os.path.join(version_dir, content_file_name)):
        progress_callback.emit(" - Using local copy of content")
        local_file = open(os.path.join(version_dir, content_file_name), "rb")
        content = local_file.read()
    else:
        progress_callback.emit(" - Downloading content (Content ID: " + str(title.tmd.content_record.content_id) +
                               ", Size: " + str(title.tmd.content_record.content_size) + " bytes)...")
        content = libTWLPy.download_content(tid, title.tmd.content_record.content_id)
        progress_callback.emit("   - Done!")
        # If keep encrypted contents is on, write out each content after its downloaded.
        if keep_enc_chkbox is True:
            enc_content_out = open(os.path.join(version_dir, content_file_name), "wb")
            enc_content_out.write(content)
            enc_content_out.close()
    title.content.content = content
    # If decrypt local contents is still true, decrypt each content and write out the decrypted file.
    if decrypt_contents_enabled is True:
        try:
            progress_callback.emit(" - Decrypting content (Content ID: " + str(title.tmd.content_record.content_id)
                                   + ")...")
            dec_content = title.get_content()
            content_file_name = hex(title.tmd.content_record.content_id)[2:]
            while len(content_file_name) < 8:
                content_file_name = "0" + content_file_name
            content_file_name = content_file_name + ".app"
            dec_content_out = open(os.path.join(version_dir, content_file_name), "wb")
            dec_content_out.write(dec_content)
            dec_content_out.close()
        except ValueError:
            # If libWiiPy throws an error during decryption, return code -3. This should only be possible if using
            # local encrypted contents that have been altered at present.
            return -3
    # If pack TAD is still true, pack the TMD, ticket, and content into a TAD.
    if pack_tad_enabled is True:
        # Get the TAD certificate chain, courtesy of libTWLPy.
        progress_callback.emit(" - Building certificate...")
        title.tad.set_cert_data(libTWLPy.download_cert())
        # Use a typed TAD name if there is one, and auto generate one based on the TID and version if there isn't.
        progress_callback.emit("Packing TAD...")
        if tad_file_name != "":
            if tad_file_name[-4:] != ".tad":
                tad_file_name = tad_file_name + ".tad"
        else:
            tad_file_name = tid + "-v" + str(title_version) + ".tad"
        # Have libTWLPy dump the TAD, and write that data out.
        file = open(os.path.join(version_dir, tad_file_name), "wb")
        file.write(title.dump_tad())
        file.close()
    progress_callback.emit("Download complete!")
    # This is where the variables come in. If the state of these variables doesn't match the user's choice by this
    # point, it means that they enabled decryption or TAD packing for a title that doesn't have a ticket. Return
    # code 1 so that a warning popup is shown informing them of this.
    if (not pack_tad_enabled and pack_tad_chkbox) or (not decrypt_contents_enabled and decrypt_contents_chkbox):
        return 1
    return 0
