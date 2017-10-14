# -*- coding: utf-8 -*-
from urllib import request
import re

from weibo_login import launcher
log = launcher()

url_test = 'http://weibo.com/u/5100086982/home?wvr=5&uut=fin&from=reg#1499096280784'
url_test2 = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4125440211855957&root_comment_max_id=140332224442037&root_comment_max_id_type=0&root_comment_ext_param=&page=1'
url_test3 = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4124297083420606&root_comment_max_id=140607028718970&root_comment_max_id_type=0&root_comment_ext_param=&page=1'
page = log.login()

page_t = log.other_url(url_test3)
print(page_t)
'''
pagename = re.findall('<a\s*title=[^>]*usercard[^>]*>',page)
for n in range(0,len(pagename)):
	pagename[n] = pagename[n].split('\\"')[1]
'''




