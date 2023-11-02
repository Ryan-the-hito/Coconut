# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

__version__ = '0.0.1'

info_plist = {
    'LSUIElement': True,
    #'LSBackgroundOnly': True,
}

a = Analysis(
    ['Coconut.py'],
    pathex=['/Users/ryanshenefield/Downloads/Coconut.py'],
    binaries=[],
    datas=[('Coconut-logo.icns', '.'), ('Coconut-dsk.icns', '.'), ('Coconut-logo.png', '.'), ('wechat50.png', '.'), ('wechat20.png', '.'), ('wechat10.png', '.'), ('wechat5.png', '.'), ('alipay50.png', '.'), ('alipay20.png', '.'), ('alipay10.png', '.'), ('alipay5.png', '.'), ('Photos_NAME.txt', '.'), ('SetTime.txt', '.')],
    hiddenimports=['subprocess', 'AppKit'],
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
    [],
    exclude_binaries=True,
    name='Coconut',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Coconut',
)
app = BUNDLE(
    coll,
    name='Coconut.app',
    icon='Coconut-dsk.icns',
    info_plist=info_plist,
    bundle_identifier=None,
    version=__version__,
)
