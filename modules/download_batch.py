# "modules/download_batch.py", licensed under the MIT license
# Copyright 2024-2026 NinjaCheetah & Contributors

import pathlib
from typing import List
from modules.core import BatchTitleData, BatchResults
from modules.download_dsi import run_nus_download_dsi
from modules.download_wii import run_nus_download_wii


def run_nus_download_batch(out_folder: pathlib.Path, titles: List[BatchTitleData], pack_wad_chkbox: bool,
                               keep_enc_chkbox: bool, decrypt_contents_chkbox: bool, wiiu_nus_chkbox: bool,
                               use_local_chkbox: bool, repack_vwii_chkbox: bool, patch_ios: bool,
                               progress_callback=None) -> BatchResults:
    result = 0
    warning_titles = []
    failed_titles = []
    for title in titles:
        if title.version == -1:
            version_str = "Latest"
        else:
            version_str = str(title.version)
        if title.console == "Wii" or title.console == "vWii":
            if title.archive_name != "":
                archive_name = f"{title.archive_name}-v{version_str}-{title.console}.wad"
            else:
                archive_name = f"{title.tid}-v{version_str}-{title.console}.wad"
            code = run_nus_download_wii(out_folder, title.tid, version_str, pack_wad_chkbox, keep_enc_chkbox,
                                          decrypt_contents_chkbox, wiiu_nus_chkbox, use_local_chkbox, repack_vwii_chkbox,
                                          patch_ios, archive_name, progress_callback)
            if code == 1:
                # Code 1 means no ticket available, so mark that as a warning title.
                result = 1
                warning_titles.append(title.tid)
            elif code != 0:
                # Any other non-zero return code means that an error occurred during the download, so mark that as a
                # failed title.
                result = 1
                failed_titles.append(title.tid)
        elif title.console == "DSi":
            if title.archive_name != "":
                archive_name = f"{title.archive_name}-v{version_str}-{title.console}.tad"
            else:
                archive_name = f"{title.tid}-v{version_str}-{title.console}.tad"
            code = run_nus_download_dsi(out_folder, title.tid, version_str, pack_wad_chkbox, keep_enc_chkbox,
                                          decrypt_contents_chkbox, use_local_chkbox, archive_name, progress_callback)
            if code == 1:
                # Code 1 means no ticket available, so mark that as a warning title.
                result = 1
                warning_titles.append(title.tid)
            elif code != 0:
                # Any other non-zero return code means that an error occurred during the download, so mark that as a
                # failed title.
                result = 1
                failed_titles.append(title.tid)
    progress_callback.emit(0, 1, f"Batch download finished.")
    return BatchResults(result, warning_titles, failed_titles)
