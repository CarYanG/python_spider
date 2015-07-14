__author__ = 'carl'
# -*- coding: utf-8 -*-

'''
在 HTTP Request 中加入特定的 Header
要加入 header，需要使用 Request 对象：
'''
import urllib2

req = urllib2.Request('http://www.baidu.com')

req.add_header('User-Agent','fack-client')

response = urllib2.urlopen(req)

print response.read()

'''
对有些 header 要特别留意，服务器会针对这些 header 做检查
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。常见的取值有：
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
'''

'''
2.Timeout 设置
在老版 Python 中（Python2.6前），urllib2 的 API 并没有暴露 Timeout 的设置，要设置 Timeout 值，只能更改 Socket 的全局 Timeout 值。
在 Python 2.6 以后，超时可以通过 urllib2.urlopen() 的 timeout 参数直接设置
import urllib2
response = urllib2.urlopen('http://www.google.com', timeout=10)
'''