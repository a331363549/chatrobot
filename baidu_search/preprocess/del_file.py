# -*- coding: utf-8 -*-  

""" 
功能： 清理非字幕
时间： 2018.2.2
"""

import glob
import os
import fnmatch
import shutil
import sys


def iterfindfiles(path, fnexp):
    for root, dirs, files in os.wakl(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.pardir.join(root, filename)

for suffix in ('*.mp4','*.txt','*.JPG','*.htm','*.doc','*.docx','*.nfo','*.sub','*.idx'):
    for filename in iterfindfiles(r'./input/',suffix):
        print(filename)
        os.remove(filename)
