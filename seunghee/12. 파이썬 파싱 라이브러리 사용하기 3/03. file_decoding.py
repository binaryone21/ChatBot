import urllib.request
url = "https://www.naver.com/"
data = urllib.request.urlopen(url).read()

# 바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)
