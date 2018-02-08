# -*- coding: utf-8 -*-  

""" 
功能：  批量解压压缩文件
时间： 2018.2.2
"""

import os, sys
import zipfile
import rarfile

open_path = os.path.abspath('../result')
save_path = os.path.abspath('./output')

os.chdir(open_path)


def Decompression(files, file_path, save_path):
    os.getcwd()
    os.chdir(file_path)
    for file in files:
        r = zipfile.is_zipfile(file)
        if r:
            zpfd = zipfile.ZipFile(file)
            # os.chdir(save_path)
            zpfd.extractall(save_path)
            zpfd.close()
        else:
            rarfd = rarfile.RarFile(file)
            rarfd.extractall(save_path)
            rarfd.close()



def files_save(open_path):
    for file_path, sub_dirs, files in os.walk(open_path):
        Decompression(files, file_path, save_path)


files_save(open_path)
