from konlpy.tag import Okt

okt = Okt()

wordList = okt.morphs(u'단독 입찰보다 복수 입찰의 경우')
print(wordList)
print()

wordList = okt.nouns(u'유일하게 항공기 체계 종합개발 경험을 갖고있는 KAI는')
print(wordList)
print()

wordList = okt.phrases(u'날카로운 분석과 신뢰감 있는 진행으로')
print(wordList)
print()

wordList = okt.pos(u'이것도 되놔욬ㅋㅋㅋ')
print(wordList)
print()

wordList = okt.pos(u'이것도 되놔욬ㅋㅋㅋ', norm=True)
print(wordList)
print()

wordList = okt.pos(u'이것도 되놔욬ㅋㅋㅋ', norm=True, stem=True)
print(wordList)
print()
