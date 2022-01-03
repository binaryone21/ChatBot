import urllib.request

url = "http://www.naver.com"
u = urllib.request.urlopen(url)

print(u.read())
print("---------")
print(u.info())