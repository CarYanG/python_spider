__author__ = 'carl'
# -*- coding: utf-8 -*-

import urllib2

import urllib

url = "http://www.baidu.com"

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5 ; Windows NT)"

headers= {'User_Agent':user_agent}

values = {"name":"yang","langunage":"python"}

data = urllib.urlencode(values)

req = urllib2.Request(url,data,headers)

response = urllib2.urlopen(req)

print response.read()

'''
浏览器确认自己身份是通过User-Agent头，当你创建了一个请求对象，你可以给他一个包含头数据的字典。
下面的例子发送跟上面一样的内容，但把自身模拟成Internet Explorer。
'''