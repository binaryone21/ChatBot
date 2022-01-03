from konlpy.tag import Komoran

komoran = Komoran(userdic='sample.txt') # userdic : 사용자 정의 사전 경로명

wordList = komoran.morphs(u'혹시 바람과 함께 사라지다 봤니?.')

print(wordList)