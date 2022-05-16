# 計算時間は small 8秒, medidum 10分50秒 ,large 3.6時間でした　->1単語1秒程度
# 実行環境では"week1"のファイル内にテキストデータを格納しています、ご自身の環境に合わせてパスの指定を変えてください
# inputはテキストファイルからの入力を想定しています

import collections
# ------------ファイル指定------------
# inputファイルの指定
INPUT_FILE = "small.txt"

# 辞書ファイルの読み込み
TEXT_FILE = "week1\words.txt"
# -----------------------------------


f = open(TEXT_FILE, "r")
dictionary = f.read().split("\n")
dictionary.remove('')  # 空白が一つ生まれるのでここで駆逐する
f.close()

#ソートされた新しい辞書の作成 / 元の辞書と紐づけ
new_dictionary = []
for w in dictionary:
    new_dictionary.append([w.strip(), collections.Counter(w)])
new_dictionary = sorted(new_dictionary, key=lambda x: x[0])  # 一番目の要素でソートする

# テキストのinputと各文字列における文字数のカウント
def input_texts(file):
    f = open(file, "r")
    f = f.read().split("\n")
    f.remove('')

    lists = []
    for w in f:
        lists.append(collections.Counter(w))

    return lists


#アナグラムの探索 / 最大スコアを持つアナグラムの出力
def anagram_search(random_word, new_dictionary):

    ans = 0
    max_anagram = "a"

    for word in new_dictionary:
        # その文字列のカウント配列を抽出
        counter = sorted(word[1].most_common(), key=lambda x: x[0])

        flag = True

        # ここで一つずつ探索 -> 文字カウントをそれぞれ二分探索したらもっと早いかも？ただループ文が増えてもっと遅くなる、、、各要素での二分探索がよくわからない、、、と迷ったのでとりあえず線形探索しました
        for i in range(len(counter)):
            character = counter[i][0]

            # 辞書のある文字のカウントがinputの文字カウントより下回っていたらアナグラムを作成することはできない
            if counter[i][1] > random_word[character]:
                flag = False
                break

        if flag:
            count = score_calc(word[0])

            # 得点の比較
            ans = max(ans, count)

            # 最大スコアが更新されたときに文字列も更新する
            if count == ans:
                max_anagram = word[0]

    return ans, max_anagram

# スコア計算
def score_calc(anagram):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]  # 得点表

    count = 0
    score_counter = collections.Counter(anagram)

    # SCORESに従って得点を付与
    for i in range(97, 123):
        count += score_counter[chr(i)]*SCORES[i-97]

    return count

# テキストファイルに出力
def output(outputname, anagrams):
    f = open("week1/"+str(outputname)+"_answer.txt", "w")

    # 最大スコアのアナグラムを書き込む
    for anagram in anagrams:
        f.write(anagram+"\n")

    f.close()


# ------------ここからメイン↓------------

text = input_texts("week1/"+INPUT_FILE)

# outputファイル用にINPUT_FILEから名前を抽出する
target = '.txt'
idx = INPUT_FILE.find(target)
outputname = INPUT_FILE[:idx]

anagrams = []

#テキスト内の単語ごとにアナグラム探索・maxスコアを持つアナグラムを配列に格納
for random_word in text:
    ans, max_anagram = anagram_search(random_word, new_dictionary)
    anagrams.append(max_anagram)

# ファイルの出力
output(outputname, anagrams)