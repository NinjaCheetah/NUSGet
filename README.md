<div align="center">
 <img src="https://github.com/user-attachments/assets/156eb949-93aa-4453-b7a0-99b784ec0c8c" alt="The icon for NUSGet" width=256 height=256>
 <h1>NUSGet</h1>
 <p>A modern and supercharged NUS downloader built with Python and Qt6.</p>
 <p>Powered by libWiiPy and libTWLPy.</p>
 <a href="https://github.com/NinjaCheetah/NUSGet/actions/workflows/python-build.yml">
  <img src="https://github.com/NinjaCheetah/NUSGet/actions/workflows/python-build.yml/badge.svg">
 </a>
</div>

![Linux Screenshot](https://github.com/user-attachments/assets/f9e0e6c4-6a04-4c2b-bffd-7a1dc58671ff)
 
## Features
NUSGet allows you to download any content from the Nintendo Update Servers. Free content (content with a Ticket freely available on the servers) can be decrypted or packed directly into an installable archive (WAD/TAD).

NUSGet also offers the ability to create vWii WADs that can be installed from within vWii mode, since the content directly from the update servers is only designed to be installed from Wii U mode.

The following features are available for all supported consoles:
- Downloading encrypted contents (files like `00000000`, `00000001`, etc.) directly from the update servers for any title.
- Creating decrypted contents (*.app files) from the encrypted contents on the servers. Only supported for free titles.
- Scripting support, allowing you to perform batch downloads of any titles for the Wii, vWii, or DSi in one script. (See `example-script.json` for an example of the scripting format.)

**For Wii and vWii titles only:**
- "Pack installable archive (WAD/TAD)": Pack the encrypted contents, TMD, and Ticket into a WAD file that can be installed on a Wii or in Dolphin Emulator. Only supported for free titles.

**For vWii titles only:**
- "Re-encrypt title using the Wii Common Key": Re-encrypt the Title Key in a vWii title's Ticket before packing the WAD, so that the WAD can be installed via a normal WAD manager on the vWii, and can be extracted with legacy tools. **This also creates WADs that can be installed directly in Dolphin, allowing for running the vWii System Menu in Dolphin without a vWii NAND dump!**

**For DSi titles only:**
- "Pack installable archive (WAD/TAD)": Pack the encrypted contents, TMD, and Ticket into a TAD file that can be installed on a TAD or in a DSi-capable emulator. Only supported for free titles. For real hardware, these titles can be installed using [@rvtr](https://github.com/rvtr)'s handy [TAD Delivery Tool](https://github.com/rvtr/TDT).

## Using NUSGet
For basic usage on all platforms, you can download the latest release for your operating system from [here](https://github.com/NinjaCheetah/NUSGet/releases/latest), and then run the executable.

**Platform-Specific Notes:**
- **macOS:** To use NUSGet on macOS, you'll need to either open NUSGet.app using right-click -> Open, or by using the terminal command `xattr -d com.apple.quarantine NUSGet.app`. After doing either of those things once, you'll be able to double-click NUSGet to open it like you normally would for an app. Note that changes in macOS Sequoia require using the latter method.
- **Windows:** On Windows, you'll likely need to allow NUSGet.exe in your antivirus program. This includes Windows Defender, which is almost guaranteed to prevent the app from being run. This is not because NUSGet is malicious in any way, it's just that NUSGet isn't popular enough to be "known" to Windows, and I don't have the expensive signing certificate necessary to work around this. If you're in doubt, you can look at all of NUSGet's code in this repository.
- **Linux:** No special information applies on Linux, however you can build NUSGet yourself if you'd like to have it as an installed application with an icon that will appear in your favorite application launcher. See [here](https://github.com/NinjaCheetah/NUSGet?tab=readme-ov-file#for-linux-users) for more information.

## Building
### System Requirements
- **Windows:** Python 3.12 (Requires Windows 8.1 or later)
- **Linux:** Python 3.12
- **macOS:** Python 3.12 (Requires macOS 10.9 or later, however macOS 11.0 or later may be required for library support)

First, make sure you're inside a venv, and then install the required dependencies:
```shell
pip install --upgrade -r requirements.txt
```
After that, follow the directions for your platform.

### Linux and macOS
A Makefile is available to build NUSGet on Linux and macOS. **On Linux**, this will give you an executable named `NUSGet` in the root of the project directory. **On macOS**, you'll instead get an application bundle named `NUSGet.app`.
```shell
make all
```

Optionally, **on Linux**, you can install NUSGet so that it's available system-wide. This will install it into `/opt/NUSGet/`.
```shell
sudo make install
```
On macOS, you can instead put the application bundle in `/Applications/` just like any other program.

### Windows
On Windows, you can use the PowerShell script `Build.ps1` in place of the Makefile. This will give you an executable named `NUSGet.exe` in the root of the project directory.
```shell
.\Build.ps1
```

## Translations
A huge thanks to all the wonderful translators who've helped make NUSGet available to more people!
 - **French:** [@rougets](https://github.com/rougets)
 - **German:** [@yeah-its-gloria](https://github.com/yeah-its-gloria)
 - **Italian:** [@LNLenost](https://github.com/LNLenost)
 - **Korean:** [@DDinghoya](https://github.com/DDinghoya)
 - **Norwegian:** [@Rolfie](https://github.com/rolfiee)
 - **Romanian:** [@NotImplementedLife](https://github.com/NotImplementedLife)
 - **Spanish:** [@DarkMatterCore](https://github.com/DarkMatterCore)

If your language isn't present or is out of date, and you'd like to contribute, you can check out [TRANSLATING.md](https://github.com/NinjaCheetah/NUSGet/blob/main/TRANSLATING.md) for directions on how to translate NUSGet.


## Additional Thanks
The name is a play on NuGet, the .NET package manager. Thank you [@Janni9009](https://github.com/Janni9009) for the name idea!

Thanks to all those who contributed to libWiiSharp and NUSD, without which this project would not exist.
