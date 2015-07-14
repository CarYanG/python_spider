__author__ = 'carl'
# -*- coding: utf-8 -*-

'''
9.表单的处理
登录必要填表，表单怎么填？
首先利用工具截取所要填表的内容。
比如我一般用firefox+httpfox插件来看看自己到底发送了些什么包。
以verycd为例，先找到自己发的POST请求，以及POST表单项。
可以看到verycd的话需要填username,password,continueURI,fk,login_submit这几项，
其中fk是随机生成的（其实不太随机，看上去像是把epoch时间经过简单的编码生成的），需要从网页获取，
也就是说得先访问一次网页，用正则表达式等工具截取返回数据中的fk项。continueURI顾名思义可以随便写，login_submit是固定的，这从源码可以看出。还有username，password那就很显然了：
'''
# -*- coding: utf-8 -*-
import urllib
import urllib2

postdata=urllib.urlencode({
'username':'汪小光',
'password':'why888',
'continueURI':'http://www.verycd.com/',
'fk':'',
'login_submit':'登录'
})

req = urllib2.Request(url = 'http://secure.verycd.com/signin', data = postdata)

result = urllib2.urlopen(req)

print result.read()

'''
11.对付"反盗链"
某些站点有所谓的反盗链设置，其实说穿了很简单，
就是检查你发送请求的header里面，referer站点是不是他自己，
所以我们只需要像把headers的referer改成该网站即可，以cnbeta为例：
#...
headers = {
    'Referer':'http://www.cnbeta.com/articles'
}
#...
headers是一个dict数据结构，你可以放入任何想要的header，来做一些伪装。
例如，有些网站喜欢读取header中的X-Forwarded-For来看看人家的真实IP，可以直接把X-Forwarde-For改了
'''