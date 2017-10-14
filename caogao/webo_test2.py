# -*- coding: utf-8 -*-
#import re
import pandas as pd
from bs4 import BeautifulSoup
import sys 
sys.path.append('E:/data analysis/python/pycharm/code/weibo_pachong/')
from weibo_login import  launcher

url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4125593912643223&root_comment_max_id=152564300049724&root_comment_max_id_type=0&root_comment_ext_param='

class zhuqu_com():
    def __init__(self, url):
        self.url = url
    
    def get_page_num(self):
        log_test = launcher()
        page_num = log_test.login(self.url)[1]['data']['page']['totalpage']
        #print(page)
        #page_new = page[1]['data']['html']
        #page_num = page[1]['data']['page']['totalpage']
        #print(page_new)
        return page_num
    def get_html(self, url):
        log_test = launcher()
        html = log_test.login(self.url)[1]['data']['html']
        return html        
    
    def get_firstcom(self):
        comment = []
        #page_num = self.get_page_num()
        for i in range(1,3,1):
            url_com = self.url + '&page=' + str(i)
            #print(i)
            page_com = self.get_html(url_com)
            soup = BeautifulSoup(page_com)
            wb_text = soup.find_all('div',class_ = 'WB_text')
            for b in wb_text:
                alast = [c.text for c in b.select('a')]
                alast.append(b.contents[-1])
                comment.append(alast)
        return comment
     
    def get_lastcom(self):
        pg = []
        for p in range(len(self.get_firstcom())):
            pp = [self.get_firstcom()[p][0],self.get_firstcom()[p][-1]]
            #print([comment[p][0],comment[p][-1]])
            pg.append(pp)
        com_data = pd.DataFrame(pg,columns=['WB_name','comment'])
        return com_data

if __name__ == '__main__':

    com_test = zhuqu_com(url)
    data = com_test.get_lastcom()
''' 
page = get_basic(url)

comment = []
for i in range(1,11,1):
    url_com = url + '&page=' + str(i)
    #print(i)
    page_com = get_basic(url_com)['html']
    soup = BeautifulSoup(page_com)
    wb_text = soup.find_all('div',class_ = 'WB_text')
    for b in wb_text:
        alast = [c.text for c in b.select('a')]
        alast.append(b.contents[-1])
        comment.append(alast)
    #com_toal.append()
pg = []
for p in range(len(comment)):
    pp = [comment[p][0],comment[p][-1]]
    #print([comment[p][0],comment[p][-1]])
    pg.append(pp)
com_data = pd.DataFrame(pg,columns=['WB_name','comment'])
com_data.comment   
soup = BeautifulSoup(page_new)

alist = []
ab = soup.find_all('div',class_ = 'WB_text')
for b in ab:
    alast = [c.text for c in b.select('a')]
    alast.append(b.contents[-1])
    alist.append(alast)
    #print(alast)
alist[0]
'''


















