# -*- coding: utf-8 -*-  

""" 
功能： 解压zip文件
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


i = 0
for filename in iterfindfiles(r'./input/', '*.sup'):
    i = i + 1
    newfilename = 'sup/' + str(i) + '_' + os.path.basename(filename)
    print(filename + '<===>' + newfilename)
    shutil.move(filename, newfilename)
