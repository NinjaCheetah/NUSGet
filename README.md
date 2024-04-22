# NUSD-Py
A modern replacement for NUS Downloader built with Python and Qt 6. Powered by libWiiPy.

## Why?
NUS Downloader (Nintendo Update Server Downloader), is an old tool for downloading titles from the Nintendo Update Servers for the Wii and DSi. Originally released in 2009, and effectively last updated in 2011, it stills works today, however it definitely shows its age, and is in need of a refresh. One of the major shortcomings of NUSD is that it only supports Windows, as most of the tools for the Wii from that era are written in C# and use the .NET Framework, especially since they tend to rely on the C# library libWiiSharp.

With my introduction of [libWiiPy](https://github.com/NinjaCheetah/libWiiPy), there's now a work-in-progress Python library designed to eventually have feature parity with libWiiSharp. At this point in time, the library is featured enough that every piece of libWiiSharp that NUSD relied on is now available in libWiiPy, so I decided to put that to use and create a replacement for it. NUSD-Py offers nearly all the same features as NUSD (currently there is no support for the DSi servers or for scripting), but is built on top of a modern library with a modern graphical framework, that being Qt6. A major benefit of this rewrite is that its fully cross-platform, and is natively compiled for Windows, Linux, and macOS.

## Features
NUSD-Py allows you to download any content from the Nintendo Update Servers. Free content (content with a Ticket freely available on the servers) can be decrypted or packed directly into a WAD.

The following options are available:
- Keep encrypted contents: Keeps the files like `00000000`, `00000001`, etc., which are the encrypted contents directly from the update servers.
- Create decrypted contents (*.app): Create decrypted files like `00000000.app`, `00000001.app`, etc., which are the decrypted data from the encrypted contents on the servers. Only supported for free titles.
- Pack WAD: Pack the encrypted contents into a WAD file that can be installed on a Wii or in Dolphin Emulator. Only supported for free titles.

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
nuitka --show-progress --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSD-Py.py --disable-console
```

**Linux**
```
nuitka3 --show-progress  --include-data-dir=data=data --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSD-Py.py
```

**macOS**
```
nuitka3 --show-progress --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSD-Py.py --macos-create-app-bundle --disable-console
```

The result will be a single binary named `NUSD-Py` that contains everything required to run NUSD-Py. No dependencies are needed on the target system.
