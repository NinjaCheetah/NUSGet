# Translating NUSGet
Since v1.2.0, NUSGet has support for loading Qt translation files. If you'd like to translate NUSGet into your language, see the following directions.

### 1. Get Qt Linguist
The first thing you'll need to get is Qt Linguist. 

For Windows and macOS users, this comes included with a normal Qt install. You'll want to get the official online Qt installer for open-source development, which is free and can be obtained [here](https://www.qt.io/download-qt-installer-oss). You do **not** need the paid/commercial version of Qt, as NUSGet is free software and is developed with the OSS version of Qt.

For Linux users, you'll likely be able to get Qt's development tools, including Qt Linguist, via your system package manager. You **must** get the Qt 6 version of the development tools, not the Qt 5 version. On Arch, for example, the package you'll need is `qt6-tools`. Depending on how the package is handled, Linguist may not appear in your application menu. If that's the case, you can start it by running `linguist6`.


### 2. Load Your Translation
NUSGet's raw translation files are stored in `resources/translations/`.

If your language doesn't already exist, open up `NUSGet.pyproject` and add a new line for your language. These files must follow the standard two-letter language codes, and you must provide the full path to the file, like with the existing entries. An example entry for Spanish would look like this:
```json
"./resources/translations/nusget_es.ts"
```

If your language already exists, or if you just added it, run `python update_translations.py` to generate any new translation files and update existing ones.

Once your translation file is ready, open it up in Qt Linguist. You should see NUSGet's interface on the right, so you have the context of where these strings are being used.


### 3. Translate
Qt Linguist will show you a list of all strings that need to be translated, along with their status. For strings that are part of the UI, the corresponding UI element will be shown so that you know what you're translating. For strings only present in the code, the code will be shown instead, which can generally be ignored.

When you've finished with your translations (or if you just want to test them), head back to the project and run `python build_translations.py`, which will build the translations to QM files in the same directory as the original TS files. These files are packaged as part of the executable when you build NUSGet, and are the actual resources that Qt loads the translations from at runtime.


### 4. Submit Your Changes
Once you've finished with your translations, open a new pull request on NUSGet's repo with your changes, and make sure to use the `translations` label. Please **do not** submit any unrelated changes as part of a translation pull request. Other changes should be submitted separately.


If you have any questions about translations, feel free to reach out and ask for help.
