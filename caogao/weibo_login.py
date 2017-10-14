# -*- coding: utf-8 -*-
import re
import rsa
from http import cookiejar
import base64
import urllib
import urllib.parse
import binascii
from urllib import request
import urllib.error
import time
import json
import pandas as pd
from bs4 import BeautifulSoup


class launcher():

    def __init__(self):
        self.password = "2011251994cjzwhb"
        self.username = "627584555@qq.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }

    def enableCookies(self):
        #建立一个cookies 容器
        cookie_container = cookiejar.CookieJar()
        #将一个cookies容器和一个HTTP的cookie的处理器绑定
        cookie_support = request.HTTPCookieProcessor(cookie_container)
        #创建一个opener,设置一个handler用于处理http的url打开
        opener = request.build_opener(cookie_support)
        #安装opener，此后调用urlopen()时会使用安装过的opener对象
        request.install_opener(opener)

    def get_encrypted_name(self):
        #获取加密后的账号
        username_urllike = urllib.request.quote(self.username)
        tusername = base64.b64encode(bytes(username_urllike, encoding='utf-8')).decode('utf-8')
        return tusername

    def get_prelogin_args(self):

        json_pattern = re.compile('\((.*)\)')
        urlpre = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&' + self.get_encrypted_name() + '&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)' + str(
            int(time.time() * 1000))

        try:
            req = request.Request(urlpre)
            response = request.urlopen(req)
            raw_data = response.read().decode('utf-8')
            json_data = json_pattern.search(raw_data).group(1)
            data = json.loads(json_data)
            return data
        except urllib.error as e:
            print("%d"%e.code)
            return None

    def build_post_data(self, data):
        rsa_e = 65537  # 0x10001
        key = rsa.PublicKey(int(data['pubkey'], 16), rsa_e)
        pw_string = str(data['servertime']) + '\t' +str(data['nonce']) + '\n' + self.password
        pw_encypted = rsa.encrypt(pw_string.encode('utf-8'), key)
        # password = ''
        passwd = binascii.b2a_hex(pw_encypted)
        # print(passwd)
        post_data = {
            "entry": "weibo",
            "gateway": "1",
            "from": "",
            "savestate": "7",
            "useticket": "1",
            "pagerefer": "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F",
            "vsnf": "1",
            "su": self.get_encrypted_name(),
            "service": "miniblog",
            "servertime": data['servertime'],
            "nonce": data['nonce'],
            "pwencode": "rsa2",
            "rsakv": data['rsakv'],
            "sp": passwd,
            "sr": "1366*768",
            "encoding": "UTF-8",
            "prelt": "61",
            "url": "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
            "returntype": "META"
        }
        data = urllib.parse.urlencode(post_data).encode('utf-8')
        return data

    def login(self):
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
        self.enableCookies()
        data = self.get_prelogin_args()
        post_data = self.build_post_data(data)

        req1 = request.Request(url=url, data=post_data, headers=self.headers)
        respon1 = request.urlopen(req1)
        html = respon1.read().decode('gbk')

        # print(html)
        p1 = re.compile('location\.replace\(\'(.*?)\'\)')
        p2 = re.compile(r'"userdomain":"(.*?)"')

        login_url = re.findall(p1, html)
        # print(login_url)
        req2 = request.Request(login_url[0], headers=self.headers)
        respon2 = request.urlopen(req2)
        html2 = respon2.read().decode('gb2312')

        login_url2 = 'http://weibo.com/' + p2.search(html2).group(1)
        req3 = request.Request(login_url2, headers=self.headers)
        respon3 = request.urlopen(req3)
        html3 = respon3.read().decode('utf-8')

        '''
        req_test = request.Request(url_test, headers=self.headers)
        respon_test = request.urlopen(req_test).read().decode('utf-8')
        data = json.loads(respon_test)
        '''


        return print("Login success!")


if __name__ == '__main__':
    log = launcher()
    page = log.login()

    def get_baic(url):
        req = request.Request(url)
        respon = request.urlopen(req).read().decode('utf-8')
        data = json.loads(respon)
        return data

    def zhuqu_com(url):
        comment = []
        page_num = get_baic(url)['data']['page']['totalpage']
        for i in range(1, page_num, 1):
            url_page = url + '&page=' + str(i)
            html = get_baic(url_page)['data']['html']
            soup = BeautifulSoup(html, 'html.parser')
            wb_text = soup.find_all('div', class_='WB_text')
            for b in wb_text:
                alast = [c.text for c in b.select('a')]
                alast.append(b.contents[-1])
                comment.append(alast)
        pg = []
        for p in range(len(comment)):
            pp = [comment[p][0], comment[p][-1]]
            pg.append(pp)
        com_data = pd.DataFrame(pg, columns=['WB_name', 'comment'])
        return com_data

    url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4125593912643223&root_comment_max_id=152564300049724&root_comment_max_id_type=0&root_comment_ext_param='

    data = zhuqu_com(url)
    print(data.comment)







