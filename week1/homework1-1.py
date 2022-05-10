


original_word = input("Input the word name : ")

original_word = original_word.lower() #小文字に揃える
random_word = ''.join(sorted(original_word)) #ソートする


#辞書ファイルの読み込み
textfile = "week1\words.txt"

f = open(textfile,"r")
dictionary = f.read().split("\n")
f.close()
    
#ソートされた新しい辞書の作成 / 元の辞書と紐づけ
new_dictionary =[]
for i in range (len(dictionary)):
    w = dictionary[i]
    new_dictionary.append([''.join(sorted(w)).strip(),w.strip()])
new_dictionary = sorted(new_dictionary,key=lambda x:x[0]) #一番目の要素でソートする

#二分探索
def binary_search(random_word,new_dictionary):
    left = 0
    right = len(dictionary) -1
    anagrams = [] #アナグラムを見つけたときに格納するリスト

    while left <= right:
        middle_index = (left+right) // 2
        middle_value = new_dictionary[middle_index][0]

        if random_word < middle_value:
            right = middle_index -1 
        
        elif random_word > middle_value:
            left = middle_index + 1

        else:
           return middle_index
           # anagrams.append(dictionary[middle_index]) #random_wordと現時点での値が一致している場合はリストに追加する

    return -1


num = binary_search(random_word,new_dictionary)

if num == -1:
    print("Not found")
    exit()

else:
    anagrams = []
    anagrams.append(new_dictionary[num][1])

    #前後に存在するか確認
    center = num - 1
    while random_word == new_dictionary[center][1]:
        anagrams.append(new_dictionary[center][1])
        center -=1
    
    center = num + 1
    while random_word == new_dictionary[center][1]:
        anagrams.append(new_dictionary[center][1])
        center +=1

print ("=== RESULT ===")
print("origignal word :" ,original_word)
print("anagrams :")
for anagram in anagrams:
    print(anagram)
print ("=============")

