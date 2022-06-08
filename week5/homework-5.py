from common import print_tour, read_input
import numpy as np
import random
import copy

# Challenge Numbers
NUMBERS = [0,1,2,3,4,5,6]

# 2点間の距離を取得
def distance(city1,city2):
    length = np.sqrt((city1[0]-city2[0])**2+(city1[1]-city2[1])**2)
    return length

def two_opt(cities):
    points_number = len(cities) # 全部で何点あるか調べる
    new_cities = copy.deepcopy(cities)
    count_nochange = 0 #変更なしの回数

    while True:
        # ランダムに異なる2点をpick up / つながっている点も取得
        number_1 = random.randint(0,points_number-1)
        number_2 = number_1

        # number_2はnumber_1と違うものにする
        while number_2 == number_1:
            number_2 = random.randint(0,points_number-1)

        city1 = new_cities[random.randint(0,points_number-1)]

        # 一番最後を引いた場合は最初につながるようにする
        if number_1 == points_number-1:
            city2 = new_cities[0]
            index1 = 0
        else:
            city2 = new_cities[number_1+1]
            index1 = number_1+1

        city3 = new_cities[number_2]
        if number_2 == points_number-1:
            city4 = new_cities[0]
        else:
            city4 = new_cities[number_2+1]
        
        # それぞれの距離を取得
        length_old1 = distance(city1,city2)
        length_old2 = distance(city3,city4)
        length_new1 = distance(city1,city3)
        length_new2 = distance(city2,city4)

        # 今の組み合わせよりランダムで選ばれた新しい組み合わせがあればそれに更新する
        if length_new1+length_new2 < length_old1+length_old2:
                new_cities[index1] = city3
                new_cities[number_2] = city2
                count_nochange = 0

        else:
            count_nochange +=1
        
        # 一定回数以上変更がなければ操作終了
        if count_nochange >= 30:
            break
    
    # new_citiesと元のcitiesから順番を照らし合わせて出力
    result = []
    for i in range(points_number):
        result.append(cities.index(new_cities[i]))
    return result

#結果をcsvに保存 
def make_output(result,NUMBER):
    with open(f'google-step-tsp/output_{NUMBER}.csv', 'w') as file:
        file.write('index')
        file.write("\n")
        for i in range(len(result)):
            file.write(str(result[i]))
            file.write("\n")
        

def main():
    for NUMBER in NUMBERS:
        # チャレンジ番号の取得と該当するinputファイルの取得
        # NUMBER = int(input('Enter the Challenge Number from 0 to 6 : '))
        filename = f'week5/input_files/input_{NUMBER}.csv'

        # ファイル読み込み - 読み込みの関数はサンプルプログラムにあるcommon.pyのモジュールをお借りしました
        cities = read_input(filename)
        
        cities = two_opt(cities)

        # make an output file
        make_output(cities,NUMBER)
        
    

if __name__ == '__main__':
    main()
