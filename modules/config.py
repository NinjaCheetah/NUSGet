# "modules/config.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah & Contributors

import os
import json
import pathlib
import platform


def get_config_file() -> pathlib.Path:
    if platform.system() == "Windows":
        config_dir = pathlib.Path(os.environ.get('APPDATA'), "NUSGet")
    elif platform.system() == "Darwin":
        config_dir = pathlib.Path(os.environ['HOME'], "Library", "Application Support", "NUSGet")
    else:
        if os.environ.get('XDG_CONFIG_HOME'):
            config_dir = pathlib.Path(os.environ.get('XDG_CONFIG_HOME'), "NUSGet")
        else:
            config_dir = pathlib.Path(os.environ['HOME'], ".config", "NUSGet")
    config_dir.mkdir(exist_ok=True, parents=True)
    return config_dir.joinpath("config.json")


def save_config(config_data: dict) -> None:
    config_file = get_config_file()
    print(f"writing data: {config_data}")
    open(config_file, "w").write(json.dumps(config_data, indent=4))


def update_setting(config_data: dict, setting: str, value: any) -> None:
    config_data[setting] = value
    save_config(config_data)
