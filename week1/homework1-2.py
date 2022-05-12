import collections
import time

t1 = time.time()
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


#アナグラムの探索 / 最大スコアを持つアナグラムの出力
def anagram_search(random_word,new_dictionary):

    ans = 0
    max_anagram = "a"

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
            count=score_calc(word[0])
     
            #得点の比較
            ans = max(ans,count)

            #最大スコアが更新されたときに文字列も更新する
            if count == ans:
                max_anagram = word[0]

    return ans,max_anagram


#スコア計算
def score_calc(anagram):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4] #得点表

    count = 0
    score_counter=collections.Counter(anagram)

    # SCORESに従って得点を付与
    for i in range(97,123):
        count+=score_counter[chr(i)]*SCORES[i-97]

    return count


#テキストファイルに出力
def output(filename,anagrams):
    f=open("week1/"+str(filename)+"answer.txt","w")
    for anagram in anagrams:
        f.write(anagram)
    f.close()


textfile = "week1\medium.txt"
a = input_texts(textfile)

total=0
anagrams=[]
for random_word in a:
    ans,max_anagram=anagram_search(random_word,new_dictionary)

    total+=ans
    anagrams.append(max_anagram)
print(total)

print(time.time()-t1)