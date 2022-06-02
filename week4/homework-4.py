import collections
ENVIRONMENT = "week4/data"


# 深さ優先探索
def dfs(start_idx,target_idx,links,check):
  # stack
  container = collections.deque()
  container.append(start_idx)

  # containerの中身が存在しなくなるまで探索を続ける
  while container:
    v = container.pop() # 頭から1つ抽出

    # 既に探索済みであればスキップする
    if check[v]:
      continue

    check[v]=True # 探索check

    # 境界条件 / 目的のwordが見つかった場合は終了する
    if v == target_idx:
      return True

    else:
      try:
        # 次のリンクを取得
        for link in links[v]:
            if not check[link]:
              container.append(link)

      except:
        continue

  # ルートが見つからない場合はFalseを返す
  return False

# 深さ優先探索のパスを探す
def search_path():
  pass

# 幅優先探索
def bfs(start_idx,target_idx,links,check):
  # que
  container = collections.deque()
  container.append(start_idx)

  # container の中身が存在しなくなるまで探索を続ける
  while container:
    v = container.popleft() # 左から1つ抽出

    # 既に探索済みであればスキップする
    if check[v]:
      continue

    check[v]=True # 探索check

    # 境界条件 / 目的のwordが見つかった場合は終了する
    if v == target_idx:
      return True

    else:
      try:
        # 次のリンクを取得・再帰で探索
        for link in links[v]:
            if not check[link]:
              container.append(link)
      except:
        continue

  # ルートが見つからない場合はFalseを返す
  return False

#small version か normal version か選択する
def check_vesion(ENVIRONMENT='week4/data'):  
    pages = {}
    links = {}
    while True:
      choice = int(input("Choose small(1) or normal(2) : "))
      if choice == 1:
        TYPE = '_small.txt'
        break
      elif choice == 2 :
        TYPE = '.txt'
        break
      else:
        print("Type Error : Try Again")

    # linksの読み込みが遅いので待っていてください
    print("Wait a Minute......")

    with open(ENVIRONMENT+'/pages'+TYPE,encoding="utf-8") as f:
      for data in f.read().splitlines():
        page = data.split('\t')
        # page[0]: id, page[1]: title
        pages[page[0]] = page[1]

    with open(ENVIRONMENT+'/links'+TYPE,encoding="utf-8") as f:
      for data in f.read().splitlines():
        link = data.split('\t')
        # link[0]: id (from), links[1]: id (to)
        if link[0] in links:
          links[link[0]].add(link[1])
        else:
          links[link[0]] = {link[1]}

    # 既に調べた項目かcheckしておく
    item_list = [k for k, v in pages.items()]
    value_list = [False]*len(item_list)
    check = dict(zip(item_list, value_list))

    return pages,links,check

def main():
  # dataまでのパスを入力する
  ENVIRONMENT = input("Type your directory for「data」file : ")
  pages,links,check = check_vesion(ENVIRONMENT)

  q = int(input("Choose the solution, DFS(1) or BFS(2) : "))
  
  while True:
    # 開始とターゲットの単語を入力する
    start_value,target_value = map(str,input('Type Start and Target Values (EX:Google 渋谷) : ').split())

    for k, v in pages.items():
      if v == start_value:
        start_idx = k
      if v == target_value:
        target_idx = k

    # startとtagetが一緒であればTrueを返して終わり
    if start_idx == target_idx:
      ans = True
      break

    if q==1:
      try:
        ans = dfs(start_idx,target_idx,links,check)
        break
      except UnboundLocalError:
        print("Words are not found. Try again")

    if q==2:
      try:
        ans = bfs(start_idx,target_idx,links,check)
        break
      except UnboundLocalError:
        print("Words are not found. Try again")

    
  # ansによる探索結果の出力
  print('Start : {}, Target : {}'.format(pages[start_idx],pages[target_idx]))
  if ans:
    print('Found!')

    print('Shortest path is {}'.format())
  else:
    print('Not Found')

if __name__ == '__main__':
  main()