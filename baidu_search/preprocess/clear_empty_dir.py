# -*- coding: utf-8 -*-  

""" 
功能： 清理目录
时间： 2018.2.2
"""

import glob
import os
import fnmatch
import shutil
import sys


def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        if 0 == len(files) and len(dirs) == 0:
            print(root)
            os.rmdir(root)


iterfindfiles(r'./input/', '')
