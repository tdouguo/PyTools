#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File    : tinypng.py
@Author  : Tdou
@功能     : 依赖tinypng批量压缩图片
@快速开始
    1. pip install -r tinypng/requirements.txt
    2. e.g. 
        tinypng sourceFolder outputFolder
        tinypng "./input/" "./output/"
"""

import tinify
import os
import sys

# APIKEY 注意请先获取API key
tinify.key = ""
file_suffixs = ['.png', '.jpg', 'jpeg']

if __name__ == "__main__":
    if len(sys.argv) <3:
        print('args error , [0]py script, [1]sourceFolder, [2]outputFolder')
    if key == '':
        print("you to tinypng.com get key")
        return
    folderinput = sys.argv[1]
    ouputpath = sys.argv[2]
    if folderinput =='':
        print("no source folder")
        return
    if ouputpath =='':
        print("no output folder")
        return
    files = os.listdir(folderinput)
    if(os.path.exists(ouputpath)):
        os.mkdir(ouputpath)

    for filename in files :
        if filename in file_suffixs:
            source = tinify.from_file(folderinput+"/"+filename)
            source.to_file(folderinput+"/"+filename)
    print('successful')