#coding=utf-8
#@see http://www.py2exe.org/index.cgi/Tutorial
from distutils.core import setup
import py2exe
import jieba

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

setup(console=['Tokenization.py'])