from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['numpy', 'pygame', 'requests'], excludes = [], include_files = ['rexlia rg.ttf', 'full Pack 2025.ttf', 'settings', 'sprites/', 'music/', 'sfx/', 'fighters/', 'stages/'])

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('main.py', base, targetName = 'main.exe')
]

setup(name='TUSSLE',
      version = '0.1',
      description = 'The Universal Smash System and Legacy Editor',
      options = dict(build_exe = buildOptions),
      executables = executables)
