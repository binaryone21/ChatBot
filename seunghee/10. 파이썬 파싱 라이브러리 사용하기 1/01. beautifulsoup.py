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

# prettiry 함수는 BeautifulSoup 에서 파싱 처리한 파서 트리를 유니코드로 리턴하는 함수
print("-----------------------------------------------------------------------")
print(soup.prettify())
print("-----------------------------------------------------------------------")
print()

# soup 객체의 데이터 탐색
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)

