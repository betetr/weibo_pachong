# -*- coding: utf-8 -*-
import re
import jieba
import os
import sys
from jieba.analyse import extract_tags
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

#sys.path.append('E:/data analysis/python/pachong/天善智能直播/')


data_weibo = pd.read_excel('E:/data analysis/weibo12344.xlsx')

chinese_pattern = re.compile(r'[\u4e00-\u9fa5]+')
clean = lambda x: ''.join(re.findall(chinese_pattern,x))
data_weibo.comment = pd.DataFrame(data_weibo.comment.map(clean)).comment
weibo_clean = data_weibo.drop(data_weibo[data_weibo.comment==''].index)

content = ''.join([x for x in weibo_clean.comment])
tags = extract_tags(content, topK=100)

	#分析得到关键词的词频
word_freq_dict = dict()
word_list = jieba.lcut(content)
for tag in tags:
    freq = word_list.count(tag)
    word_freq_dict[tag] = freq
#解决显示中文问题，仅限windows用户
font = "c:/windows/fonts/微软雅黑/msyh.ttf"  #
def cloud(data):
    wc = WordCloud(font_path=font, background_color='#ff7f50')
    wc.generate_from_frequencies(data)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

#word_freq_dict = {}

cloud(data=word_freq_dict)


























