import urllib2;
import json
import codecs

url = "https://macvendors.co/api/"
macadd = "BC:92:6B:A0:00:01"

request = urllib2.Request(url+macadd, headers={'User-Agent':"API Browser"})
response = urllib2.urlopen(request)
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))

print(obj['result']['company']);
print(obj['result']['address']);