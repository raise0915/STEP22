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

## 2-opt
2-optはランダムに選ばれた2つの組み合わせについて

# プログラムの実行方法

# 結果
以下のようになりました。(outputが自分で実装したプログラムの結果です)<br>


randomには全てのパターンにおいて勝つことができましたが、greedyよりもスコアはよくないです...

# 改善案
2-optは局地解を探索します。つまり局地的に最適解を得られても大域的には最適解を得ることができません。大域的最適解を得るにはSimulated Annealing (焼きなまし法)がいいのかなと思います。<br>
焼きなまし法は必ずしも現在の解を良解に移行するわけではなく、一定の確率で改悪解にも移行することで大域的最適解を探索します。<br>
あとは、2-opt法のままでも何回連続で解の変更が行われない場合終了するか、の回数指定によっても改善できるのかなと思います。
