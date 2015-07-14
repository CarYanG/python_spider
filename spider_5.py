__author__ = 'carl'
# -*- coding: utf-8 -*-

import urllib2

import urllib

url = "http://www.baidu.com"

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5 ; Windows NT)"

headers= {'User_Agent':user_agent}

values = {"name":"yang","langunage":"python"}

data = urllib.urlencode(values)

req = urllib2.Request(url,data,headers)

response = urllib2.urlopen(req)

print response.read()

