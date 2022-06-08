# week5 - TPS (Traveling Salesman Problem)を解こう!

## input/outputデータや説明の格納場所
[ここにある]("https://github.com/hayatoito/google-step-tsp")

中身は以下のようになっています。(リンク元から引用)

* `solver_random.py` - Sample stupid solver. You never lose to this stupid one.<br>
* `sample/random_{0-6}.csv` - Sample output files by solver_random.py.<br>
* `solver_greedy.py` - Sample solver using the greedy algorithm. You should beat this definitely.<br>
* `sample/greedy_{0-6}.csv` - Sample output files by solver_greedy.py.<br>
* `sample/sa_{0-6}.csv` - Yet another sample output files. I expect all of you will beat this one too. The solver itself is not included intentionally.<br>
* `output_{0-6}.csv` - You should overwrite these files with your program's output.<br>
* `output_verifier.py` - Try to validate your output files and print the path length.<br>
* `input_generator.py` - Python script which was used to create input files, input_{0-6}.csv<br>
* `visualizer/` - The directory for visualizer.<br>

~~You never lose to this stupid one にびびっています(プログラムを書く前)~~ <br>

## TSPとは？
TSP(Traveling Salesman Problem ;巡回セールスマン問題)は、あるものの点の集合と各2点における距離が与えられたとき、全ての点をちょうど一度ずつ巡り出発点に戻る経路が最短のものを見つける問題です。組み合わせ最適化問題。<br>
<br>

# 実装アルゴリズムの解説
2-optとなんちゃってSimulated Annealingを実装

## 2-opt
2-optは経路の中の2つの辺を選び、経路を入れ替えた結果が現在のものより短くなれば入れ替えをする、を繰り替えして最短経路を見つかるアルゴリズムです。<br>
2-optはgreedyに比べ提案される経路(解)は短くなりますが、局地的に最適解を得られても大域的には最適解を得ることができません。<br>


## Simulated Annealing
そこで、大域的最適解を得るにはSimulated Annealing (焼きなまし法)がいいのかなと思います。<br>
焼きなまし法は金属の焼きなましから得られた手法で、プログラムが回るたびに冷却率に従って温度を下げていきます。<br>
必ずしも現在の解を良解に移行するわけではなく、一定の確率で改悪解にも移行することで大域的最適解を探索します。<br>
現時点での温度を $T$、現在の解と提案された解の絶対値の差を$ΔE$とすると、確率$P$は以下のように表すことができます。

$ P = exp(-ΔE)/T $

## フローチャート
というわけでこの2つを組み合わせるとこんな感じになります。2optを一巡やるごとに冷却させています

<img src="https://user-images.githubusercontent.com/63898148/172624023-248fe36d-b604-4458-9000-60c4d259da31.png">
<br>

# 結果
以下のようになりました。(outputが自分で実装したプログラムの結果です)<br>


randomには全てのパターンにおいて勝つことができましたが、greedyよりもスコアはよくないです...

# 改善案
Simulated Annealingの結果は初期変数に大きく依存します。(最大温度・最小温度・冷却率)これらの値の設定でより良い経路が見つかると思います。<br>
冷却率は現在温度の対数をとると良いとされていますが、かなり時間がかかるので考え物です...
