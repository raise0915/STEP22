import json 
import collections
from re import A

#辞書ファイルの読み込み
textfile = "week1\words.txt"

f = open(textfile,"r")
dictionary = f.read().split("\n")
dictionary.remove('') #空白が一つ生まれるのでここで駆逐する
f.close()
    
#ソートされた新しい辞書の作成 / 元の辞書と紐づけ
new_dictionary =[]
for w in dictionary:
    new_dictionary.append([w.strip(),collections.Counter(w)])
new_dictionary = sorted(new_dictionary,key=lambda x:x[0]) #一番目の要素でソートする



#テキストのinputとカウント
def input_texts(file):
    f = open(file,"r")
    f = f.read().split("\n")

    lists=[]
    for w in f:
        lists.append(collections.Counter(w))

    return lists


#アナグラムの探索
def anagram_search(random_word,new_dictionary):
    anagrams = []

    for word in new_dictionary:
        counter = word[1]
        flag = True
        for i in range (len(counter)):
            character = counter.most_common()[i][0]

            # 辞書のある文字のカウントがinputの文字カウントより下回っていたらアナグラムを作成することはできない
            if counter.most_common()[i][1] > random_word[character]: 
                flag = False
                break

        if flag:
            anagrams.append(word[0])

    return anagrams

#出力




a = input_texts("week1\small.txt")


    