__author__ = 'carl'
# -*- coding: utf-8 -*-
'''
代理（英语：Proxy），也称网络代理，是一种特殊的网络服务，允许一个网络终端（一般为客户端）通过这个服务
与另一个网络终端（一般为服务器）进行非直接的连接。
一些网关、路由器等网络设备具备网络代理功能。
一般认为代理服务有利于保障网络终端的隐私或安全，防止攻击。
'''


'''
Proxy 的设置
urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。
如果想在程序中明确控制 Proxy 而不受环境变量的影响，可以使用代理。
新建test14来实现一个简单的代理Demo：
'''
import urllib2

enable_proxy = True

proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})

null_proxy_handle = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)

else:
    opener = urllib2.build_opener(null_proxy_handle)

urllib2.install_opener(opener)

'''
这里要注意的一个细节，使用 urllib2.install_opener() 会设置 urllib2 的全局 opener 。
这样后面的使用会很方便，但不能做更细致的控制，比如想在程序中使用两个不同的 Proxy 设置等。
比较好的做法是不使用 install_opener 去更改全局的设置，而只是直接调用 opener 的 open 方法代替全局的 urlopen 方法。
'''