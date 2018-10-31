#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: AutoOps 
# Software: PyCharm2018.3
# DateTime: 2018-10-31 18:59
# File: install_python.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


import os
import sys

if os.getuid() == 0:
    pass
else:
    print '当前用户不是root用户，请以root用户执行该脚本'
    sys.exit(1)
version = raw_input('请输入你想安装的Python版本（2.7/3.7）')
if version == '2.7':
    url = 'https://www.python.org/downloads/release/python-2715/'
elif version == '3.7':
    url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
else:
    print '您输入的版本号有误，请输入2.7或者3.7'
    sys.exit(1)

cmd = 'wget ' + url
res = os.system(cmd)
if res != 0:
    print '下载源码包失败，请检查网络'
    sys.exit(1)

if version == '2.7':
    package_name = 'Python-2.7.15'
else:
    package_name = 'Python-3.7.1'
cmd = 'tar -xf' + package_name + '.tgz'
res = os.system(cmd)
if res != 0:
    os.system('rm ' + package_name + '.tgz')
    print '解压缩源码包失败，请重新运行这个脚本下载源码包'
    sys.exit(1)

cmd = 'cd ' + package_name + '&& ./configure --prefix=/usr/local/python && make && make install'

res = os.system(cmd)
if res != 0:
    print '编译Python源码失败，请检查是否缺少依赖库'
    sys.exit(1)
