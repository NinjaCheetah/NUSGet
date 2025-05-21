# "modules/core.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah & Contributors

import os
import json
import pathlib
import requests
from dataclasses import dataclass
from typing import List

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QStyledItemDelegate, QSizePolicy


# This is required to make the dropdown look correct with the custom styling. A little fuzzy on the why, but it has to
# do with how Qt handles rendering the dropdown items. The sizing has to be overridden so that they don't overlap.
class ComboBoxItemDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        return QSize(option.rect.width(), 33)


@dataclass
class TitleData:
    # Class to store all data for a Title.
    tid: str
    name: str
    version: str
    ticket: bool
    region: str
    category: str
    danger: str


@dataclass
class BatchTitleData:
    # Class to store all data for a Title in a batch operation.
    tid: str
    version: int
    console: str
    archive_name: str


@dataclass
class BatchResults:
    # Class to store the results of a batch download.
    code: int
    warning_titles: List[str]
    failed_titles: List[str]


def connect_label_to_checkbox(label, checkbox):
    def toggle_checkbox(event):
        if checkbox.isEnabled() and event.button() == Qt.LeftButton:
            checkbox.toggle()
    label.mousePressEvent = toggle_checkbox


def connect_is_enabled_to_checkbox(items, chkbox):
    for item in items:
        if chkbox.isChecked():
            item.setEnabled(True)
        else:
            item.setEnabled(False)


def check_nusget_updates(app, current_version: str, progress_callback=None) -> str | None:
    # Simple function to make a request to the GitHub API and then check if the latest available version is newer.
    gh_api_request = requests.get(url="https://api.github.com/repos/NinjaCheetah/NUSGet/releases/latest", stream=True)
    if gh_api_request.status_code != 200:
        progress_callback.emit(app.translate("MainWindow", "\n\nCould not check for updates."))
    else:
        api_response = gh_api_request.json()
        new_version: str = api_response["tag_name"].replace('v', '')
        new_version_split = new_version.split('.')
        current_version_split = current_version.split('.')
        for place in range(len(new_version_split)):
            if new_version_split[place] < current_version_split[place]:
                return None
            elif new_version_split[place] > current_version_split[place]:
                progress_callback.emit(app.translate("MainWindow", "\n\nThere's a newer version of NUSGet available!"))
                return new_version
        progress_callback.emit(app.translate("MainWindow", "\n\nYou're running the latest release of NUSGet."))
    return None


def get_config_file() -> pathlib.Path:
    config_dir = pathlib.Path(os.path.join(
        os.environ.get('APPDATA') or
        os.environ.get('XDG_CONFIG_HOME') or
        os.path.join(os.environ['HOME'], '.config'),
        "NUSGet"
    ))
    config_dir.mkdir(exist_ok=True)
    return config_dir.joinpath("config.json")


def save_config(config_data: dict) -> None:
    config_file = get_config_file()
    print(f"writing data: {config_data}")
    open(config_file, "w").write(json.dumps(config_data))


def update_setting(config_data: dict, setting: str, value: any) -> None:
    config_data[setting] = value
    save_config(config_data)
