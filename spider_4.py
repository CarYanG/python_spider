__author__ = 'carl'
# -*- coding: utf-8 -*-

import urllib2

import urllib

url = "http://www.baidu.com"

data={}

data["name"]="yang"

data["language"]="python"

url_value = urllib.urlencode(data)

print url_value

full_url = url + '?' +url_value

data = urllib2.urlopen(full_url)

print data.read()

#此处使用GET方式请求