__author__ = 'carl'
# -*- coding: utf-8 -*-

#post 与 get 的区别
#这两种请求是HTTP协议中常用的请求,Get请求把表单的数据显式地放在URI中,并且对
# 长度和数据值编码有所限制.Post请求把表单数据放在HTTP请求体中,并且没有长度限制.

import urllib

import urllib2

url = "http://www.baidu.com"

values = {"name":"yang","langunage":"python"}

data = urllib.urlencode(values)  #使用urllib编码

req = urllib2.Request(url,data)  # 发送请求同时传data表单

response = urllib2.urlopen(req)   #接受反馈的信息

print response.info()

print response.geturl()

this_page = response.read()

print this_page

#此处使用post方式请求











