from setuptools import setup

APP = ['thomas_converter2.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL'],
    'includes': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
