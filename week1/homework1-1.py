#標準入力 / 単語1つ を想定しています

# 辞書ファイルの読み込み
textfile = "week1\words.txt"
f = open(textfile, "r")
dictionary = f.read().split("\n")
f.close()

#ソートされた新しい辞書の作成 / 元の辞書と紐づけ
new_dictionary = []
for w in dictionary:
    new_dictionary.append([''.join(sorted(w)).strip(), w.strip()])
new_dictionary = sorted(new_dictionary, key=lambda x: x[0])  # 一番目の要素でソートする

#単語の入力
def input_check():
    input_flag = False
    # アルファベット判定・そうでなければ再度入力を促す
    while input_flag == False:
        input_word = input("Input the word name : ")
        if input_word.isalpha():
            input_flag = True
        else:
            print("Try Again")


    original_word= input_word.strip().lower()  # 空白を除去・小文字に揃える
    input_word = ''.join(sorted(original_word))  # ソートする
    return input_word,original_word


# 二分探索関数
def binary_search(random_word, new_dictionary):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        middle_index = (left+right) // 2
        middle_value = new_dictionary[middle_index][0]

        if random_word < middle_value:
            right = middle_index - 1

        elif random_word > middle_value:
            left = middle_index + 1

        else:
            return middle_index

    return -1  # anagramが見つからない場合は-1を返す

# ------------ここからメイン------------

random_word,original_word = input_check()
num = binary_search(random_word, new_dictionary)

# アナグラムが見つからない場合は「Not found」を返して終了
if num == -1:
    print("Not found")
    exit()

else:
    anagrams = []  # アナグラムを見つけたときに格納するリスト
    anagrams.append(new_dictionary[num][1])

    # 前後にも同一のアナグラムが存在するか確認
    center = num - 1
    while random_word == new_dictionary[center][1]:
        anagrams.append(new_dictionary[center][1])
        center -= 1

    center = num + 1
    try:
        while random_word == new_dictionary[center][1]:
            anagrams.append(new_dictionary[center][1])
            center += 1
    except:
        pass

# 結果の表示
print("=== RESULT ===")
print("origignal word :", original_word)
print("anagrams :")
for anagram in anagrams:
    print(anagram)
print("=============")