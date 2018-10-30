from setuptools import setup 
import yxspkg_songzviewer
import sys
import os
from pathlib import Path
from urllib import request
def set_desktop():
    if sys.platform.startswith('linux'):
        p = Path(os.environ['HOME']) /'.yxspkg'/'songzviewer'
        if not p.is_dir():
            os.makedirs(p)
        request.urlretrieve() 
setup(name='yxspkg_songzviewer',   
      version=yxspkg_songzviewer.__version__,    
      description='A Image viewer',    
      author=yxspkg_songzviewer.__author__,    
      install_requires=[],
      py_modules=['yxspkg_songzviewer'],
      platforms='any',
      author_email='blacksong@yeah.net',       
      url='https://github.com/blacksong',
      
      entry_points={'console_scripts': ['songzviewer=yxspkg_songzviewer:main']},
      classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)   