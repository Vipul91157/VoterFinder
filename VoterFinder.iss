#define MyAppName "VoterFinder"
#define MyAppVersion "1.0"
#define MyAppPublisher "Vipul Kumar"
#define MyAppExeName "VoterFinder.exe"

[Setup]
AppId={{A8C45C4D-7D3B-4D7D-9C54-6F1D7E7E1234}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=Installer
OutputBaseFilename=VoterFinder_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "VoterFinder_Test\VoterFinder.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "VoterFinder_Test\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\VoterFinder"; Filename: "{app}\VoterFinder.exe"
Name: "{autodesktop}\VoterFinder"; Filename: "{app}\VoterFinder.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\VoterFinder.exe"; Description: "Launch VoterFinder"; Flags: nowait postinstall skipifsilent