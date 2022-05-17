# 行列計算 / グラフ作成プログラム
# homework2-1.pyによる行列計算における計算時間についてのグラフが出力されます -> 時間はかかる
# commandの部分をご自身の環境に合わせて書き換えてください

import subprocess
from matplotlib import pyplot as plt
# どこまでの行列(NUMBER * NUMBER)を測定するか設定する
NUMBER = 500

#計算時間の取得
def find_calc(n):
    # コマンドで行列式プログラムの実行
    command = 'python c:/Users/yuri1/STEP22/week2/homework2-1.py '+str(n)
    # 出力結果の抽出
    text = str(subprocess.run(command, capture_output=True).stdout)

    # 出力結果から計算時間のみ抽出
    target1 = 'time: '
    target2 = 'sec'
    idx_start = text.find(target1)
    idx_end = text.find(target2)
    time = text[idx_start+len(target1):idx_end] 

    return time

# 結果の描画
def draw_graph(results):
    x = list(range(len(results)))
    y = results

    # ラベルの設定
    plt.xlabel("Matrix Number [-]")
    plt.ylabel("Calculation Time [sec] ")

    # グラフの描画
    plt.plot(x,y)

    #保存
    plt.savefig("week2/calc_result.png")
    
# メイン関数
def main():
    # 時間結果用の配列作成
    results = []
    # 0の分を初めに追加しておく
    results.append(0)

    for i in range(NUMBER):
        results.append(float(find_calc(i)))
    draw_graph(results)

if __name__ == '__main__' :
    main()
