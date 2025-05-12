# Translating NUSGet
To translate NUSGet into your language, first make sure that you have NUSGet's dependencies installed:
- [Git](https://git-scm.com/)
- [Python](https://python.org) (make sure to install a version listed as compatible in the README)

### Step 1: Fork and Prepare the Repository
To fork the repository, either click the "Fork" button on the repository's main page, or [click here](https://github.com/NinjaCheetah/NUSGet/fork).

Then, you'll need to clone your new fork locally and enter it:
```shell
git clone https://github.com/<your-username>/NUSGet
cd NUSGet/
```

Then, create and activate a venv (depending on your platform, you may need to specify `python3` rather than `python`):
```shell
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS, Linux, and other Unix-likes
source .venv/bin/activate
```

Finally, install NUSGet's dependencies:
```shell
pip install --upgrade -r requirements.txt
```

### Step 2: Add Your Language
Open `NUSGet.pyproject` in your editor of choice, and check for your language in it. If a line for your language doesn't exist, create a new entry following the format `"./resources/translations/nusget_XX.ts"`, where `XX` is the two-letter code that represents your language.

### Step 3: Update Translation Files
To update the `.ts` files that store the translations and to create them for any newly added languages, run:
```shell
python update_translations.py
```
This ensures that you're working on an up-to-date version of the strings in the app.

### Step 4: Launch Qt Linguist and Load the Translations
Qt Linguist is included as part of the `PySide6` package you installed during Step 1. To launch Qt Linguist, use the appropriate command for your platform, replacing `<ver>` with the version of Python you installed (for example, `3.12`).

```shell
# Windows
.venv\lib\python<ver>\site-packages\PySide6\linguist.exe

# macOS
open .venv/lib/python<ver>/site-packages/PySide6/Linguist.app

# Linux and other Unix-likes
./.venv/lib/python<ver>/site-packages/PySide6/linguist
```
If you have Qt Linguist installed system-wide already, you can use that instead. These steps are included primarily for those who don't, since installing the Qt Platform Tools on Windows or macOS requires having a Qt account.

Once you've launched Qt Linguist, you can open the `.ts` file for your language in it.

### Step 5: Translate!

### Step 6: Test Your Translations
If your current system language is the one you're NUSGet translating into, then you can just run:
```shell
python NUSGet.py
```
and the app should open in your language.

If your system language does not match the language you're translating to, you can specify a language override, like this:
```shell
LANG=xx_XX.UTF-8 python NUSGet.py
```
where `xx` is the two-letter language code, such as `ko` for Korean, and `XX` is the country code, such as `KR` for Korea. All together, that would give you:
```shell
LANG=ko_KR.UTF-8 python NUSGet.py
```
which would open NUSGet with the Korean translations loaded.

### Step 7: Push and Merge Your Translations
When you're done translating, commit your translations and push them to GitHub. Then, open a pull request on the original repository, and you're all done!
