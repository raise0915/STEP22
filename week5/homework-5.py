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

    #Simulated Annealingのための変数
    T_max = 10000 #最高温度
    T_min = 0.1 #最低温度
    T = T_max #現在の温度   
    COOL = 0.98 # 温度冷却

    while T > T_min:
        # 2点をpick up / つながっている点も取得
        for index1 in range(points_number-2):                
            index2 = index1 +1
            for index3 in range(index1+2,points_number):

                # 一番最後を引いた場合は最初につながるようにする
                if index3 == points_number-1:
                    index4 = 0
                else:
                    index4 = index3 +1

                city1 = new_cities[index1]  
                city2 = new_cities[index2]
                city3 = new_cities[index3]  
                city4 = new_cities[index4]        
                
                # それぞれの距離を取得
                pre_length = distance(city1,city2) + distance(city3,city4)
                new_length = distance(city1,city3) + distance(city2,city4)

                    # 遷移確率関数
                prob = np.exp(-(np.abs(pre_length - new_length))/T)

                # 今の組み合わせがより短い or 確率的に次の解へ移動
                if pre_length > new_length or random.random() < prob:
                    new_cities[index2] = city3
                    new_cities[index3] = city2

        T*= COOL #温度冷却
    

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
