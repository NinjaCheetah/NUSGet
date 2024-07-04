# NUSGet
A modern and supercharged NUS downloader built with Python and Qt6. Powered by libWiiPy and libTWLPy. 

[![Python application](https://github.com/NinjaCheetah/NUSGet/actions/workflows/python-build.yml/badge.svg)](https://github.com/NinjaCheetah/NUSGet/actions/workflows/python-build.yml)

The name is a play on NuGet, the .NET package manager. Thank you [@Janni9009](https://github.com/Janni9009) for the name idea!

## Features
NUSDGet allows you to download any content from the Nintendo Update Servers. Free content (content with a Ticket freely available on the servers) can be decrypted or packed directly into an installable archive (WAD/TAD).

NUSGet also offers the ability to create vWii WADs that can be installed from within vWii mode, since the content directly from the update servers is only designed to be installed from Wii U mode.

The following features are available for all supported consoles:
- Downloading encrypted contents (files like `00000000`, `00000001`, etc.) directly from the update servers for any title.
- Creating decrypted contents (*.app files) from the encrypted contents on the servers. Only supported for free titles.

**For Wii and vWii titles only:**
- "Pack installable archive (WAD/TAD)": Pack the encrypted contents, TMD, and Ticket into a WAD file that can be installed on a Wii or in Dolphin Emulator. Only supported for free titles.

**For vWii titles only:**
- "Pack for vWii mode instead of Wii U mode": Re-encrpyt the Title Key in a vWii title's Ticket before packing a WAD, so that the WAD can be installed from inside the vWii on a Wii U. **This also creates WADs that can be installed directly in Dolphin, allowing for running the vWii System Menu in Dolphin without a vWii NAND dump!**

**For DSi titles only:**
- "Pack installable archive (WAD/TAD)": Pack the encrypted contents, TMD, and Ticket into a TAD file that can be installed on a TAD or in a DSi-capable emulator. Only supported for free titles. For real hardware, these titles can be installed using [@rvtr](https://github.com/rvtr)'s handy [TAD Delivery Tool](https://github.com/rvtr/TDT).

## Translating
If you want to contribute tom this project by translating, you can do that on [GitLocalize!](https://gitlocalize.com/repo/9731/badge)
Only the strings containing instructions should be translated, the rest should **not** be touched.
Any string is appreciated! :D

## Building
### System Requirements
- **Windows:** Python 3.11 (Requires Windows 8.1 or later)
- **Linux:** Python 3.11
- **macOS:** Python 3.11 (Requires macOS 10.9 or later, however macOS 11.0 or later may be required for library support)

**Python 3.12 is not supported at this time.**

First, install the required dependencies:
```
pip install -r requirements.txt
```
Then, use the command for your platform to build an executable with Nuitka:

**Windows**
```
nuitka --show-progress --include-data-dir=data=data --include-data-dir=resources=resources --assume-yes-for-downloads --onefile --windows-icon-from-ico=resources/icon.png --plugin-enable=pyside6 NUSGet.py --windows-console-mode=disable
```

**Linux**
```
nuitka3 --show-progress  --include-data-dir=data=data --include-data-dir=resources=resources --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSGet.py
```

**macOS**
```
nuitka3 --show-progress --include-data-dir=data=data --include-data-dir=resources=resources --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSGet.py --macos-create-app-bundle --macos-app-icon=resources/icon.png
```

The result will be a single binary named `NUSGet` that contains everything required to run NUSGet. No dependencies are needed on the target system.


## Why this and not NUSD?
NUS Downloader (Nintendo Update Server Downloader), is an old tool for downloading titles from the Nintendo Update Servers for the Wii and DSi. Originally released in 2009, and effectively last updated in 2011, it stills works today, however it definitely shows its age, and is in need of a refresh. One of the major shortcomings of NUSD is that it only supports Windows, as most of the tools for the Wii from that era are written in C# and use the .NET Framework, especially since they tend to rely on the C# library libWiiSharp. NUSD also has far more limited support for DSi titles, and no support whatsoever for vWii titles.

With my introduction of [libWiiPy](https://github.com/NinjaCheetah/libWiiPy), there's now a work-in-progress Python library designed to eventually have feature parity with libWiiSharp. At this point in time, the library is featured enough that every piece of libWiiSharp that NUSD relied on is now available in libWiiPy, so I decided to put that to use and create a replacement for it. NUSGet offers nearly all the same features as NUSD (currently there is no support for the DSi servers or for scripting), but is built on top of a modern library with a modern graphical framework, that being Qt6. A major benefit of this rewrite is that its fully cross-platform, and is natively compiled for Windows, Linux, and macOS.
