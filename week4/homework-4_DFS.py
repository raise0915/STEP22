import collections

# 深さ優先探索
def dfs(start_idx,end_idx,links,pages):
  # stack
  container = collections.deque()
  container.append(start_idx)

  # 既に調べた項目かcheckしておく
  item_list = [k for k, v in pages.items()]
  value_list = [False]*len(item_list)
  check = dict(zip(item_list, value_list))

  # container の中身が存在しなくなるまで探索を続ける
  while container:
    v = container.pop() # 頭から1つ抽出

    # 既に探索済みであればスキップする
    if check[v]:
      continue

    check[v]=True # 探索check

    # 境界条件 / 目的のwordが見つかった場合は終了する
    if v == end_idx:
      return True

    for link in links:
      print(link)
      if check[link]:
        continue
      else:
        container.appendleft(link)

  return False


def main():
  pages = {}
  links = {}

  with open('week4/data/pages.txt',encoding="utf-8") as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

  with open('week4/data/links.txt',encoding="utf-8") as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}


  for k, v in pages.items():
    if v == 'Google':
      print('Google', k)
      start_idx = k
    if v == '渋谷':
      end_idx = k
 
  print(dfs(start_idx,end_idx,links,pages))




 


if __name__ == '__main__':
  main()