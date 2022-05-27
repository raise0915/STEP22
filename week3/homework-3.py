#! /usr/bin/python3
def read_number(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    decimal = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * decimal
      decimal /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index

#かけ算の追加
def read_star(line,index):
  token = {'type': 'STAR'}
  return token, index + 1

#割り算の追加
def read_slash(line,index):
  token = {'type': 'SLASH'}
  return token, index + 1

# 小かっこ
def read_lpar(line,index):
  token = {'type': 'LAPAR'}
  return token, index + 1

def read_rapar(line,index):
  token = {'type': 'RAPAR'}
  return token, index + 1

#中かっこ
def read_lbrace(line,index):
  token = {'type': 'LBRACE'}
  return token, index + 1

def read_rbrace(line,index):
  token = {'type': 'RBRACE'}
  return token, index + 1

#大かっこ
def read_lsqb(line,index):
  token = {'type': 'LSQB'}
  return token, index + 1

def read_rsqb(line,index):
  token = {'type': 'RSQB'}
  return token, index + 1


def read_plus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1


def read_minus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1



def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = read_number(line, index)
    elif line[index] == '+':
      (token, index) = read_plus(line, index)
    elif line[index] == '-':
      (token, index) = read_minus(line, index)
      
    # 掛け算と割り算の追加
    elif line[index] == '*':
      (token,index) = read_star(line,index)
    elif line[index] == '/':
      (token, index) = read_slash(line, index)  

    # 小かっこ
    elif line[index] == '(':
      (token,index) = read_lpar(line,index)
    elif line[index] == ')':
      (token,index) = read_rapar(line,index)

    #中かっこ
    elif line[index] == '{':
      (token,index) = read_lbrace(line,index)
    elif line[index] == '}':
      (token,index) = read_rbrace(line,index)

    #大かっこ
    elif line[index] == '[':
      (token,index) = read_lsqb(line,index)
    elif line[index] == ']':
      (token,index) = read_rsqb(line,index)
       
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

# かっこ内の計算
def caluculate_brackets(tokens,brackets_type):

  #小/中/大かっこについて考える
  if brackets_type == "small":
    start_index = tokens.index({'type': 'LAPAR'})
    end_index = tokens.index({'type': 'RAPAR'})
  if brackets_type =="medium":
    start_index = tokens.index({'type': 'LBRACE'})
    end_index = tokens.index({'type': 'RBRACE'})
  if brackets_type =="large":
    start_index = tokens.index({'type': 'LSQB'})
    end_index = tokens.index({'type': 'RSQB'})

  # かっこの中身だけ抽出する
  calc_tokens = tokens[start_index+1 : end_index]
 
  brackets_answer = calculate_as(calculate_td(calc_tokens))

  calculated_tokens = []
  # かっこの計算後のtoken
  for i in range(len(tokens)):
    # かっこ内は計算済みなのでパス
    if i >= start_index and i < end_index:
      continue
    # 右かっこ「)」まで終わったら計算結果を新しいtokenに追加
    if i == end_index:
      calculated_tokens.append({'type': 'NUMBER','number':brackets_answer})
    # かっこの部分以外はそのまま
    else:
      calculated_tokens.append(tokens[i])

  return calculated_tokens


# 計算部分
# かけ算 / わり算の処理を行う -> その後残りの記号を足し算・引き算する
def calculate_td(tokens):
  # かけ算とわり算の処理
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 0
  has_continuity = False #*と/が連続した時用
  current_number = 0
  while index < len(tokens)-1:
    if tokens[index +1]['type'] == 'NUMBER':

        # 記号が「*」であった場合
        if tokens[index]['type'] == 'STAR':
          if has_continuity:
            tokens[current_number]['number']*= tokens[index+1]['number']
          
          else:
            tokens[index-1]['number'] *= tokens[index+1]['number']
            current_number = index-1
            has_continuity = True

        # 記号が「/」の記号であった場合
        elif tokens[index]['type'] == 'SLASH':
          # /と*の記号が数字を飛ばして連続して存在するときは先頭の数字tokenで計算する
          if has_continuity:
            try:
              tokens[current_number]['number']/= tokens[index+1]['number']
            except ZeroDivisionError:
              print("Zero Division Error")
              exit(1)            
          else:
            try:
              tokens[index-1]['number'] /= tokens[index+1]['number']
              current_number = index-1
              has_continuity = True
            # 0が後ろに来た場合は割れないのでエラーで返す
            except ZeroDivisionError:
              print("Zero Division Error")
              exit(1)

        # +と-はここでは無視
        elif tokens[index]['type'] == 'PLUS' or tokens[index]['type']== 'MINUS':
          has_continuity = False
        
        else:
          raise Exception('Invalid syntax')

    index += 1


  # tokenの作り直し -> 足し算と引き算だけにする
  new_tokens =[]
  for i in range(1,len(tokens)):
    if tokens[i]['type'] =='NUMBER':
      # +と-はそのまま追加
      if tokens[i-1]['type'] =='PLUS' or tokens[i-1]['type'] =='MINUS':
        new_tokens.append(tokens[i-1])
        new_tokens.append(tokens[i])

      # *と/の場合は記号と後半の数字は無視する
      if tokens[i-1]['type'] =='STAR' or tokens[i-1]['type'] =='SLASH':
        continue
  return new_tokens
  
  # 足し算と引き算 (サンプルそのまま)
def calculate_as(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1 

  return answer


# 計算まとめ　-> かっこがつく場合かっこ内を先に計算するようにする
# 前提条件：大かっこが存在していれば中・小かっこが、中かっこが存在していれば小かっこが存在しているものとする
def evaluate(tokens):
  # 小かっこが存在する場合
  if tokens.count({'type': 'LAPAR'}) > 0:
    for _ in range(tokens.count({'type': 'LAPAR'})) :
      tokens = caluculate_brackets(tokens,'small')

  # 中かっこが存在する場合
  if tokens.count({'type': 'LBRACE'}) > 0:
    for _ in range(tokens.count({'type': 'LBRACE'})):
      tokens = caluculate_brackets(tokens,'medium') 

  # 大かっこが存在する場合
  if tokens.count({'type': 'LSQB'}) > 0:
    for _ in range(tokens.count({'type': 'LSQB'})):
      tokens = caluculate_brackets(tokens,'large')

  #かっこが存在しない場合
  else:
    pass

  answer = calculate_as(calculate_td(tokens))

  return answer


def test(line):
  tokens = tokenize(line)
  actual_answer = evaluate(tokens)
  #eval関数は大かっこと中かっこに対応してないそうなので、大・中かっこがある場合は答えだけ出します
  try:
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
      print("PASS! (%s = %f)" % (line, expected_answer))
    else:
      print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))
  except:
    print("EXCEPTION bracketS! (%s = %f)" % (line, actual_answer))
    


# Add more tests to this function :)
def run_test():
  print("==== Test started! ====")
  test("224*5")
  test("1+2*5")
  test("1+2")
  test("1.0+2.1-3")
  test("1/2+5")
  # test("3/0+7") -> Zero Division Error判定
  test("6.5/3+2*9.5+4.00")
  test("2+2*2/2-2")
  test("3*3*3*3*3")
  test("4/4/4/4/4")
  test("(2+5)*7")
  test("(3+6)*(7+1)")
  test("(3+5)*(2+4)*(1+7)")
  test("{(8+2)*(6+5)+2}*5")
  test("[{(8+2)*(6+5)+2}+{(8+2)*(6+5)+2}]*5")
  # test("((2+4))") -> これはERROR
  test("(2+4)")
  test("1")
  print("==== Test finished! ====\n")

run_test()


while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)