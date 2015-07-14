__author__ = 'carl'
# -*- coding: utf-8 -*-

'''
先来解释一下urllib2中的两个个方法：info and geturl
urlopen返回的应答对象response(或者HTTPError实例)
有两个很有用的方法info()和geturl()
1.geturl()：
这个返回获取的真实的URL，这个很有用，因为urlopen(或者opener对象使用的)或许会有重定向。获取的URL或许跟请求URL不同。
以人人中的一个超级链接为例,
我们来比较一下原始URL和重定向的链接：
'''

from urllib2 import Request,urlopen,URLError,HTTPError

old_url = 'http://rrurl.cn/b1UZuP'

req = Request(old_url)

response = urlopen(req)

print 'Old url :' +old_url

print 'real url: ' +response.geturl()
