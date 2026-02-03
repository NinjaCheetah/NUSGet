# "update_translations.py", licensed under the MIT license
# Copyright 2024-2026 NinjaCheetah & Contributors
# This script exists to work around an issue in PySide6 where the "pyside6-project lupdate" command doesn't work as
# expected, as it struggles to parse the paths in the .pyproject file. This does what it's meant to do for it.

import json
import pathlib
import subprocess


LUPDATE_CMD = "pyside6-lupdate"


pyproject_file = pathlib.Path("NUSGet.pyproject")
pyproject = json.load(open(pyproject_file, "r"))
files = []
for key in pyproject["files"]:
    files.append(pathlib.Path(key))
source_files = []
ts_files = []
for file in files:
    if file.suffix == ".ts":
        ts_files.append(file)
    elif file.suffix == ".py" or file.suffix == ".ui":
        source_files.append(file)

for target in ts_files:
    cmd = [LUPDATE_CMD] + [s for s in source_files] + ["-ts"]
    cmd.append(target)
    subprocess.run(cmd, cwd=str(pyproject_file.parent))
