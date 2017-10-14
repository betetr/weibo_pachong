# -*- coding: utf-8 -*-
import re 
import pandas as pd
import sys
sys.path.append('E:/data analysis/python/pycharm/code/weibo_pachong/')
from get_comment import launcher

url2 = 'http://weibo.com/aj/mblog/add?ajwvr=6'
text = '这是我用脚本写的，第一次尝试，希望成功！'
fawei = launcher(url2)
fawei.faweibo()
'''
url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4126075640431368&root_comment_max_id=141569208318517&root_comment_max_id_type=0&root_comment_ext_param='
com = launcher(url)
data = com.get_comment()
'''
