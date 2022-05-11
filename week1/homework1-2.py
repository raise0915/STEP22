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
    f.remove('')

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


#スコア計算 / 一番スコアの良い文字列の抽出
def score_calc(anagrams):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4] #得点表

    ans = 0
    max_anagram = "a"

    for anagram in anagrams:
        count = 0
        score_counter=collections.Counter(anagram)

        # SCORESに従って得点を付与
        for i in range(97,123):
            count+=score_counter[chr(i)]*SCORES[i-97]
        
        #得点の比較
        ans = max(ans,count)

        #最大スコアが更新されたときに文字列も更新する
        if count == ans:
            max_anagram = anagram


    return ans,max_anagram


#テキストファイルに出力

a = input_texts("week1\medium.txt")


total=0
for random_word in a:
    anagrams=anagram_search(random_word,new_dictionary)
    ans,max_anagram=score_calc(anagrams)

    total+=ans
    print(ans,max_anagram)
print(total)

    