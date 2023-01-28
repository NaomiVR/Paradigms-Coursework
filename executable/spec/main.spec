# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['F:\\University\\Year 1\\Ongoing\\COMP-1811-M01-2022-23 Paradigms of Programming\\Coursework\\Code\\main.py', 'F:\\University\\Year 1\\Ongoing\\COMP-1811-M01-2022-23 Paradigms of Programming\\Coursework\\Code\\source\\classes\\network_reader.py', 'F:\\University\\Year 1\\Ongoing\\COMP-1811-M01-2022-23 Paradigms of Programming\\Coursework\\Code\\source\\classes\\friend_handler.py', 'F:\\University\\Year 1\\Ongoing\\COMP-1811-M01-2022-23 Paradigms of Programming\\Coursework\\Code\\source\\classes\\analyser.py', 'F:\\University\\Year 1\\Ongoing\\COMP-1811-M01-2022-23 Paradigms of Programming\\Coursework\\Code\\source\\classes\\custom_exceptions.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
