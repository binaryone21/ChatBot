from konlpy.tag import Hannanum

hannanum = Hannanum()

wordList = hannanum.analyze(u'롯데마트의 흙마늘 양념 치킨이 논란이 되고 있다.')
print(wordList)