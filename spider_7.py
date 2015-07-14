__author__ = 'carl'
# -*- coding: utf-8 -*-

import urllib2

req = urllib2.Request('http://bbs.csdn.net/callmewhy')

try:
    urllib2.urlopen(req)
except urllib2.URLError,e:
    print e.read()
    print e.code
    print e.reason



'''
HTTPError实例产生后会有一个整型'code'属性，是服务器发送的相关错误号。
Error Codes错误码
因为默认的处理器处理了重定向(300以外号码)，并且100-299范围的号码指示成功，所以你只能看到400-599的错误号码。
BaseHTTPServer.BaseHTTPRequestHandler.response是一个很有用的应答号码字典，显示了HTTP协议使用的所有的应答号。
当一个错误号产生后，服务器返回一个HTTP错误号，和一个错误页面。
你可以使用HTTPError实例作为页面返回的应答对象response。
这表示和错误属性一样，它同样包含了read,geturl,和info方法。
'''