import random

quizzes = {}
quizzes['問題1'] = {'問題文':'サザエの旦那の名前は？', '選択肢':['マスオ', 'ますお',], '正解':'ますお'}
quizzes['問題2'] = {'問題文':'カツをの妹の名前は？', '選択肢':['ワカメ','わかめ',], '正解':'わかめ'}
quizzes['問題3'] = {'問題文':'タラオはカツオから見てどんな関係？', '選択肢':['甥', 'おい', '甥っ子','おいっこ'], '正解':'おい'}


key, value = random.choice(list(quizzes.items()))
print(key, value['問題文'])
print('選択肢 ', end='')
for i in range(len(value['選択肢'])):
    print(f"{i+1}.'{value['選択肢'][i]}' ", end='')
print('')


answer = int(input('解答を選択肢の番号で入力してください>'))


if value['選択肢'][answer-1] == value['正解']:
    print('正解！')
else:
    print(f"はずれ。正解は{value['正解']}でした")