__author__ = 'carl'
# -*- coding: utf-8 -*-

#5.Cookie
#urllib2 对 Cookie 的处理也是自动的。如果需要得到某个 Cookie 项的值，可以这么做：

import urllib2
import cookielib

cookie = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response = opener.open('http://www.baidu.com')

for item in cookie:
    print 'Name = '+ item.name
    print 'Value = '+item.value


'''
7.得到 HTTP 的返回码
对于 200 OK 来说，只要使用 urlopen 返回的 response 对象的 getcode() 方法就可以得到 HTTP 的返回码。
但对其它返回码来说，urlopen 会抛出异常。这时候，就要检查异常对象的 code 属性了：
import urllib2
try:
    response = urllib2.urlopen('http://bbs.csdn.net/why')
except urllib2.HTTPError, e:
    print e.code

'''