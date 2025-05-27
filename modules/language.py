# "modules/language.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah & Contributors

from modules.config import update_setting

from PySide6.QtCore import QLocale, QTranslator


LANGS = {
    "en": "English",
    "es": "Español",
    "de": "Deutsch",
    "fr": "Français",
    "it": "Italiano",
    "no": "Norsk",
    "ro": "Românǎ",
    "ko": "한국어",
}


def set_language(config_data: dict, lang: str) -> None:
    # Match the selected language. These names will NOT be translated since they represent each language in that
    # language, but the "System (Default)" option will, so that will match the default case.
    match lang:
        case "English":
            print("setting language to English")
            update_setting(config_data, "language", "en")
        case "Español":
            print("setting language to Spanish")
            update_setting(config_data, "language", "es")
        case "Deutsch":
            print("setting language to German")
            update_setting(config_data, "language", "de")
        case "Français":
            print("setting language to French")
            update_setting(config_data, "language", "fr")
        case "Italiano":
            print("setting language to Italian")
            update_setting(config_data, "language", "it")
        case "Norsk":
            print("setting language to Norwegian")
            update_setting(config_data, "language", "no")
        case "Română":
            print("setting language to Romanian")
            update_setting(config_data, "language", "ro")
        case "한국어":
            print("setting language to Korean")
            update_setting(config_data, "language", "ko")
        case _:
            print("setting language to system (default)")
            update_setting(config_data, "language", "")


def get_language(translator: QTranslator, config_data: dict, path: str) -> QTranslator:
    try:
        lang = config_data["language"]
    except KeyError:
        lang = ""
    # A specific language was set in the app's settings.
    if lang != "":
        # If the target language is English, then return an empty translator because that's the default.
        if lang == "en":
            return translator
        if translator.load(QLocale(lang), 'nusget', '_', path):
            return translator
        else:
            # If we get here, then the saved language is invalid, so clear it and run again to use the system language.
            update_setting(config_data, "language", "")
            return get_language(translator, config_data, path)
    else:
        # Unix-likes and Windows handle this differently, apparently. Unix-likes will try `nusget_xx_XX.qm` and then
        # fall back on just `nusget_xx.qm` if the region-specific translation for the language can't be found. On
        # Windows, no such fallback exists, and so this code manually implements that fallback, since for languages like
        # Spanish NUSGet doesn't use region-specific translations.
        locale = QLocale.system()
        if not translator.load(QLocale.system(), 'nusget', '_', path):
            base_locale = QLocale(locale.language())
            translator.load(base_locale, 'nusget', '_', path)
        return translator
