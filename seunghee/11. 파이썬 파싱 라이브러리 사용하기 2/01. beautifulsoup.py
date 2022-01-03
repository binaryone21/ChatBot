sample = """
<html>
    <head>
        <title>옛날 이야기</title>
    </head>

    <body>
        <p class="title"><b>옛날 이야기</b></p>

        <p class="story">
            옛날 옛적에 세명의 자매가 있었습니다.
            그들의 이름은
            <a href="http://example.com/elsie" class="sister" id="link1">엘리제</a>,
            <a href="http://example.com/lacie" class="sister" id="link2">레이시</a>,
            <a href="http://example.com/tillie" class="sister" id="link3">타일리에</a> 이었습니다.
            그들은 아주 가난하게 살았습니다.
        </p>

        <p class="story">
            ...
        </p>
    </body>
</html>


"""


from bs4 import  BeautifulSoup

# 생성자에서는 html.html을 파싱하고, 그 결과를 BeautifulSoup 객체에 반환
soup = BeautifulSoup( sample, 'html.parser') # BeautifulSoup 생성자

print(soup.find_all('a'))

print("-------------------------")

print(soup.find(id="link2"))

print("-------------------------")

for link in soup.find_all('a') :
    print(link.get('href'))

print("-------------------------")

for link in soup.find_all('a') :
    print(link.attrs['href'])

print("-------------------------")

txt = soup.get_text()
print(txt)

print("-------------------------")

# next_sibling 은 엔터도 가져온다
p1 = soup.p
p2 = p1.next_sibling.next_sibling
print(p2)

print("-------------------------")

p3 = p2.previous_sibling.previous_sibling
print(p3)

print("-------------------------")

a = soup.a
print(type(a.attrs))

print("-------------------------")
