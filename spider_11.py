__author__ = 'carl'
# -*- coding: utf-8 -*-
'''
这个返回对象的字典对象，该字典描述了获取的页面情况。通常是服务器发送的特定头headers。
目前是httplib.HTTPMessage 实例。
经典的headers包含"Content-length"，"Content-type"，和其他内容。
我们来测试一下info的应用：
'''

from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://www.baidu.com'

req = Request(old_url)

response = urlopen(req)

print 'Info():'
print response.info()
