# -*- mode: python -*-

block_cipher = None


a = Analysis(['generate.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=['cython', 'sklearn', 'sklearn.neighbors.typedefs', 'tkinter', 'tkinter.filedialog', 'tensorflow.contrib'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='generate',
          debug=False,
          strip=False,
          upx=True,
          console=True )
