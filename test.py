__author__ = 'carl'
import string


#url="http://www.qiushibaike.com/hot"

import urllib2
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers= {'User-Agent':user_agent}

myurl="http://www.qiushibaike.com/hot"

req = urllib2.Request(myurl,headers = headers)

myresponse = urllib2.urlopen(req)

this_page = myresponse.read()

print this_page
