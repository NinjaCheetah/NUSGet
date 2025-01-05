# "build_translations.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah
# This script exists to work around an issue in PySide6 where the "pyside6-project build" command incorrectly places
# translation files in the root of the project directory while building.

import json
import pathlib
import subprocess


LRELEASE_CMD = "pyside6-lrelease"


pyproject_file = pathlib.Path("NUSGet.pyproject")
pyproject = json.load(open(pyproject_file, "r"))
files = []
for key in pyproject["files"]:
    files.append(pathlib.Path(key))
ts_files = []
for file in files:
    if file.suffix == ".ts":
        ts_files.append(file)

for translation in ts_files:
    cmd = [LRELEASE_CMD] + [translation] + ["-qm"] + [translation.with_suffix(".qm")]
    subprocess.run(cmd, cwd=str(pyproject_file.parent))
