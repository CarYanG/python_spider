__author__ = 'carl'
# -*- coding: utf-8 -*-

'''
4.Redirect
urllib2 默认情况下会针对 HTTP 3XX 返回码自动进行 redirect 动作，无需人工配置。要检测是否发生了 redirect 动作，
只要检查一下 Response 的 URL 和 Request 的 URL 是否一致就可以了。
'''
'''
import urllib2

url = 'http://www.baidu.com'
req= urllib2.Request(url)

response = urllib2.urlopen(req)

redirected = url== response.geturl()

print redirected


import urllib2
my_url = 'http://rrurl.cn/b1UZuP'
response = urllib2.urlopen(my_url)
redirected = response.geturl() == my_url
print redirected
'''
#如果不想自动 redirect，除了使用更低层次的 httplib 库之外，还可以自定义HTTPRedirectHandler 类。

import urllib2

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print "301"
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        print "302"
        pass

opener = urllib2.build_opener(RedirectHandler)

try:
    opener.open('http://rrurl.cn/b1UZuP')
except urllib2.HTTPError,e:
    print e.code

'''
6.使用 HTTP 的 PUT 和 DELETE 方法
urllib2 只支持 HTTP 的 GET 和 POST 方法，如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。
虽然如此，我们还是能通过下面的方式，使 urllib2 能够发出 PUT 或DELETE 的请求：
import urllib2
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)

'''