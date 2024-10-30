<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="de_DE">
<context>
    <name>MainWindow</name>
    <message>
        <location filename="../../NUSGet.py" line="85"/>
        <source>NUSGet v{nusget_version}
Developed by NinjaCheetah
Powered by libWiiPy {libwiipy_version}
DSi support provided by libTWLPy {libtwlpy_version}

Select a title from the list on the left, or enter a Title ID to begin.

Titles marked with a checkmark are free and have a ticket available, and can be decrypted and/or packed into a WAD or TAD. Titles with an X do not have a ticket, and only their encrypted contents can be saved.

Titles will be downloaded to a folder named &quot;NUSGet&quot; inside your downloads folder.</source>
        <translatorcomment>&quot;Downloads&quot; in German copies of Windows and macOS isn&apos;t translated
Specified that the tickets for titles with a checkmark are publicly available, for clarity in the translation</translatorcomment>
        <translation>NUSGet v{nusget_version}
Entwickelt von NinjaCheetah
Nutzt libWiiPy {libwiipy_version}
Unterstützung für DSi bereitgestelt durch libTWLPy {libtwlpy_version}

Wähle einen Titel aus der Liste auf der linken Seite oder gebe eine Title-ID ein, um zu beginnen.

Titel, welche mit einem Häkchen markiert sind, sind frei verfügbar und haben ein öffentliches Ticket, und können daher entschlüsselt und/oder in eine WAD/TAD verpackt werden. Titel mit einem Kreuz haben kein öffentlich verfügbares Ticket und können nur verschlüsselt heruntergeladen werden.

Titel werden in einem &quot;NUSGet&quot; Ordner innerhalb des Downloads-Ordners gespeichert.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="184"/>
        <source>NUSGet Update Available</source>
        <translation>NUSGet-Update verfügbar</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="185"/>
        <source>There&apos;s a newer version of NUSGet available!</source>
        <translation>Eine neuere Version von NUSGet ist verfügbar.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="264"/>
        <source>No Output Selected</source>
        <translatorcomment>Changed from &quot;output&quot; to &quot;packaging&quot; for clarity</translatorcomment>
        <translation>Keine Verpackmethode ausgewählt</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="265"/>
        <source>You have not selected any format to output the data in!</source>
        <translation>Es wurde keine Methode zum Verpacken der Inhalte ausgewählt.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="267"/>
        <source>Please select at least one option for how you would like the download to be saved.</source>
        <translatorcomment>Explicitly mentions options for clarity</translatorcomment>
        <translation>Es muss mindestens &quot;verschlüsselte Inhalte speichern&quot;, &quot;entschlüsselte Inhalte speichern&quot; oder &quot;Verpacke als WAD/TAD&quot; ausgewählt worden sein.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="298"/>
        <source>Invalid Title ID</source>
        <translation>Fehlerhafte Title-ID</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="299"/>
        <source>The Title ID you have entered is not in a valid format!</source>
        <translation>Die eingegebene Title-ID ist nicht korrekt.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="301"/>
        <source>Title IDs must be 16 digit strings of numbers and letters. Please enter a correctly formatted Title ID, or select one from the menu on the left.</source>
        <translation>Die Title-ID muss mindestens 16 alphanumerische Zeichen enthalten.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="303"/>
        <source>Title ID/Version Not Found</source>
        <translation>Title-ID/Version nicht gefunden</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="304"/>
        <source>No title with the provided Title ID or version could be found!</source>
        <translatorcomment>The title was moved into the body, and the title was made less of a mouthful, for ease of translation</translatorcomment>
        <translation>Es konnte kein Titel mit der gegebenen Title-ID oder Version gefunden werden.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="306"/>
        <source>Please make sure that you have entered a valid Title ID, or selected one from the title database, and that the provided version exists for the title you are attempting to download.</source>
        <translation>Die Title-ID könnte möglicherweise fehlerhaft sein.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="308"/>
        <source>Content Decryption Failed</source>
        <translation>Entschlüsselung fehlgeschlagen</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="309"/>
        <source>Content decryption was not successful! Decrypted contents could not be created.</source>
        <translation>Die Inhalte des Titels konnten nicht korrekt entschlüsselt werden.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="312"/>
        <source>Your TMD or Ticket may be damaged, or they may not correspond with the content being decrypted. If you have checked &quot;Use local files, if they exist&quot;, try disabling that option before trying the download again to fix potential issues with local data.</source>
        <translation>Die gespeicherte TMD oder das Ticket könnten möglicherweise fehlerhaft sein. &quot;Lokale Dateien nutzen&quot; kann ausgeschaltet werden, um diese erneut herunterzuladen.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="315"/>
        <source>Ticket Not Available</source>
        <translation>Ticket nicht verfügbar</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="316"/>
        <source>No Ticket is Available for the Requested Title!</source>
        <translation>Kein Ticket konnte für den geforderten Titel gefunden werden.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="319"/>
        <source>A ticket could not be downloaded for the requested title, but you have selected &quot;Pack installable archive&quot; or &quot;Create decrypted contents&quot;. These options are not available for titles without a ticket. Only encrypted contents have been saved.</source>
        <translation>Es wurden nur verschlüsselte Inhalte gespeichert.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="321"/>
        <source>Unknown Error</source>
        <translation>Unbekannter Fehler</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="322"/>
        <source>An Unknown Error has Occurred!</source>
        <translation>Ein unbekannter Fehler ist aufgetreten.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="324"/>
        <source>Please try again. If this issue persists, please open a new issue on GitHub detailing what you were trying to do when this error occurred.</source>
        <translation>Versuchen Sie es erneut. Sofern das Problem bestehen bleibt, können Sie ein Issue auf GitHub öffnen, um den Fehler zu berichten.</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="364"/>
        <source>Open NUS script</source>
        <translatorcomment>Translating the file type is pointless, since it&apos;s not an actual &quot;script&quot;</translatorcomment>
        <translation>NUS-Script öffnen</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="364"/>
        <source>NUS Scripts (*.nus *.txt)</source>
        <translation>NUS Script (*.nus *.txt)</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="371"/>
        <location filename="../../NUSGet.py" line="386"/>
        <location filename="../../NUSGet.py" line="389"/>
        <location filename="../../NUSGet.py" line="397"/>
        <location filename="../../NUSGet.py" line="415"/>
        <location filename="../../NUSGet.py" line="422"/>
        <source>Script Failure</source>
        <translation>Script-Fehler</translation>
    </message>
    <message>
        <location filename="../../NUSGet.py" line="371"/>
        <source>Failed to open the script.</source>
        <translation>Konnte das NUS-Script nicht öffnen.</translation>
    </message>
    <message>
        <location filename="../../modules/core.py" line="26"/>
        <source>

Could not check for updates.</source>
        <translation>

Konnte nicht nach Updates suchen.</translation>
    </message>
    <message>
        <location filename="../../modules/core.py" line="34"/>
        <source>

There&apos;s a newer version of NUSGet available!</source>
        <translation>

Eine neuere Version von NUSGet ist verfügbar.</translation>
    </message>
    <message>
        <location filename="../../modules/core.py" line="36"/>
        <source>

You&apos;re running the latest release of NUSGet.</source>
        <translatorcomment>Like previously, we&apos;re trying to refer to the user less directly (since it sounds awkard in German)</translatorcomment>
        <translation>

Die neuste Version von NUSGet ist bereits aktiv.</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="26"/>
        <source>MainWindow</source>
        <translatorcomment>This title isn&apos;t shown</translatorcomment>
        <translation>Hauptmenü</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="43"/>
        <source>Available Titles</source>
        <translation>Verfügbare Titel</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="72"/>
        <source>Wii</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="103"/>
        <source>vWii</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="134"/>
        <source>DSi</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="174"/>
        <source>Title ID</source>
        <translatorcomment>We do not translate &quot;Title ID&quot; beyond making it grammatically correct (hence the dash), since it refers to a NUS specific component</translatorcomment>
        <translation>Title-ID</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="181"/>
        <source>v</source>
        <translation>=</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="194"/>
        <source>Version</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="201"/>
        <source>Console:</source>
        <translation>Konsole:</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="237"/>
        <source>Start Download</source>
        <translation>Herunterladen</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="250"/>
        <source>Run Script</source>
        <translation>Script starten</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="277"/>
        <source>General Settings</source>
        <translation>Einstellungen</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="308"/>
        <source>Pack installable archive (WAD/TAD)</source>
        <translation>Installierbar verpacken (WAD/TAD)</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="323"/>
        <source>File Name</source>
        <translation>Dateiname</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="357"/>
        <source>Keep encrypted contents</source>
        <translation>Verschlüsselte Inhalte speichern</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="393"/>
        <source>Create decrypted contents (*.app)</source>
        <translation>Entschlüsselte Inhalte speichern (*.app)</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="432"/>
        <source>Use local files, if they exist</source>
        <translation>Lokale Dateien nutzen, sofern verfügbar</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="477"/>
        <source>Use the Wii U NUS (faster, only effects Wii/vWii)</source>
        <translation>Wii U-NUS nutzen (schneller, gilt nur für Wii/vWii)</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="519"/>
        <source>Apply patches to IOS (Applies to WADs only)</source>
        <translatorcomment>&quot;Patch&quot; does not have a good translation into German, and in most modding forums, it&apos;s used as is</translatorcomment>
        <translation>Patches für IOS anwenden (Gilt nur für WAD)</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="575"/>
        <source>vWii Title Settings</source>
        <translation>vWii Titel-Einstellungen</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="609"/>
        <source>Re-encrypt title using the Wii Common Key</source>
        <translatorcomment>Common key does not get translated</translatorcomment>
        <translation>Titel mit dem Common-Key der Wii neu verschlüsseln</translation>
    </message>
    <message>
        <location filename="../../qt/ui/MainMenu.ui" line="666"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;Noto Sans&apos;; font-size:10pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Sans Serif&apos;; font-size:9pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation></translation>
    </message>
</context>
</TS>
