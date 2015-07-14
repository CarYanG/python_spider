__author__ = 'carl'
# -*- coding: utf-8 -*-

from urllib2 import Request,urlopen,URLError,HTTPError


req = Request('http://bbs.csdn.net/callmewhy')
try:
    response = urlopen(req)

except HTTPError, e:

    print 'the server couldn\'t fulfill the request'

    print 'Error Code: ',e.code

except URLError, e:
    print 'We failed to reach a server.'

    print 'Reason：',e.reason

else:
    print 'NO exception was raised'

# everything is fine

'''
为HTTPError或URLError做准备（异常处理方案之一)

try之后捕获异常并且将其内容打印出来。
这里要注意的一点，except HTTPError 必须在第一个，否则except URLError将同样接受到HTTPError 。
'''
