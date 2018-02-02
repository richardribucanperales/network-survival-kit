import urllib


def browse_url(url):
  req=urllib.urlopen(url)
  f=open("data.html","wb")
  f.write(req.read())
  f.close()
browse_url("http://www.google.com")