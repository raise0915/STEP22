# はじめに
大変遅くなってしまって申し訳ないです、、、<br>

# 宿題の概要
## **深さ優先探索(DFS)と幅優先探索(BFS)で'Google' から ' 渋谷' までのwikipediaの検索経路が存在するかどうかを判定する**<br>

<br>

## 深さ優先探索(DFS)
スタックを用いて探索しました。
再帰を用いたら早いんだろうなと思いつつぐるぐるしすぎてエラーを吐いたので、おとなしく愚直にやっています<br>
探索順序は以下のようになります。<br>



## 幅優先探索(BFS)
DFSとやり方は似ていますが、stuckではなくqueを用いています


# コードについて

## コードの配置
your favorite directory<br>
(好きなところにおいてください<br>
├── data<br>
│   ├── graph_small.png<br>
│   ├── links_small.txt<br>
│   ├── links.txt<br>
│   ├── pages_small.txt<br>
│   └── pages.txt<br>
├── README.md<br>
├── homework-4.py<br>

※「your favorite directory」までのパス名を把握しておいてください

## 実行方法
Python
テスト環境：python 3.9.2
以下のように行ってください

`python homework-4.py`

その後、
`Choose small(1) or normal(2) : `と出てくるので好きな方の数字を入力してください。

`Type your directory for「data」file : `では「data」フォルダまでのパスを入力してください (例：week4/data)

その後、深さ優先探索か幅優先探索かの選択を行います。<br>
`Choose the solution, DFS(1) or BFS(2) : ` 好きな方を入力して下さい。

`Type Start and Target Values (EX:Google 渋谷) : `で最初の単語と最終的に辿り着くか調べたい単語について入力してください。<br>
`「最初の単語(半角スペース)目標単語」`という風に入力してください。<br>
単語がテキスト内に存在しない場合は繰り返し入力するよう促されます。


経路が見つかった場合`Found`、見つからない場合は`Not Found`と出力されます





