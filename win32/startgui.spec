# -*- mode: python -*-

block_cipher = None

a = Analysis(['startgui'],
             pathex=['.\\gui'],
             binaries=[],
             datas=[],
             hiddenimports=['six', 'scipy.integrate'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib', 'OpenGL', 'PyQt5.QtOpenGL'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='startgui',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='startgui')
