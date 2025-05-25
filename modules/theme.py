# "modules/theme.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah & Contributors

import os
import platform
import subprocess

def is_dark_theme_windows():
    # This has to be here so that Python doesn't try to import it on non-Windows.
    import winreg
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        # This value is "AppsUseLightTheme" so a "1" is light and a "0" is dark. Side note: I hate the Windows registry.
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return value == 0
    except Exception:
        return False

def is_dark_theme_macos():
    # macOS is weird. If the dark theme is on, then `defaults read -g AppleInterfaceStyle` returns "Dark". If the light
    # theme is on, then trying to read this key fails and returns an error instead.
    try:
        result = subprocess.run(
            ["defaults", "read", "-g", "AppleInterfaceStyle"],
            capture_output=True, text=True
        )
        return "Dark" in result.stdout
    except Exception:
        return False

def is_dark_theme_linux():
    try:
        import subprocess
        result = subprocess.run(
            ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"],
            capture_output=True, text=True
        )
        # Looking for *not* "Light", because I want any theme that isn't light to be dark. An example of this is my own
        # KDE Plasma setup on my desktop, where I use the "Breeze" GTK theme and want dark NUSGet to be used in that
        # case.
        return not "light" in result.stdout.lower()
    except Exception:
        return False

def is_dark_theme():
    # First, check for an environment variable overriding the theme, and use that if it exists.
    try:
        if os.environ["THEME"].lower() == "light":
            return False
        elif os.environ["THEME"].lower() == "dark":
            return True
        else:
            print(f"Unknown theme specified: \"{os.environ['THEME']}\"")
    except KeyError:
        pass
    # If the theme wasn't overridden, then check the current system theme.
    system = platform.system()
    if system == "Windows":
        return is_dark_theme_windows()
    elif system == "Darwin":
        return is_dark_theme_macos()
    else:
        return is_dark_theme_linux()
