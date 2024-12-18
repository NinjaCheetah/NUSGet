# "modules/download_batch.py", licensed under the MIT license
# Copyright 2024 NinjaCheetah

import pathlib
from typing import List
from modules.core import BatchTitleData
from modules.download_dsi import run_nus_download_dsi
from modules.download_wii import run_nus_download_wii


def run_nus_download_batch(out_folder: pathlib.Path, titles: List[BatchTitleData], pack_wad_chkbox: bool,
                               keep_enc_chkbox: bool, decrypt_contents_chkbox: bool, wiiu_nus_chkbox: bool,
                               use_local_chkbox: bool, repack_vwii_chkbox: bool, patch_ios: bool,
                               progress_callback=None):
    for title in titles:
        if title.console == "Wii" or title.console == "vWii":
            if title.archive_name != "":
                archive_name = f"{title.archive_name}-v{title.version}-{title.console}.wad"
            else:
                archive_name = f"{title.tid}-v{title.version}-{title.console}.wad"
            result = run_nus_download_wii(out_folder, title.tid, str(title.version), pack_wad_chkbox, keep_enc_chkbox,
                                          decrypt_contents_chkbox, wiiu_nus_chkbox, use_local_chkbox, repack_vwii_chkbox,
                                          patch_ios, archive_name, progress_callback)
            if result != 0:
                return result
        elif title.console == "DSi":
            if title.archive_name != "":
                archive_name = f"{title.archive_name}-v{title.version}-{title.console}.tad"
            else:
                archive_name = f"{title.tid}-v{title.version}-{title.console}.tad"
            result = run_nus_download_dsi(out_folder, title.tid, str(title.version), pack_wad_chkbox, keep_enc_chkbox,
                                          decrypt_contents_chkbox, use_local_chkbox, archive_name, progress_callback)
            if result != 0:
                return result
    progress_callback.emit(f"Batch download finished.")
    return 0
