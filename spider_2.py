__author__ = 'carl'
import urllib2

req = urllib2.Request("http://www.baidu.com")

response = urllib2.urlopen(req)

this_page = response.read()

print this_page