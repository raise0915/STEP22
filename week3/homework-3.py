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
       
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evaluate(tokens):
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 0

  # まずはかけ算 / わり算の処理を行う -> その後残りの記号を足し算・引き算する
 
  # かけ算とわり算の処理
  while index < len(tokens)-1:
    if tokens[index +1]['type'] == 'NUMBER':

        # かけ算の記号であった場合
        if tokens[index]['type'] == 'STAR':
          tokens[index-1]['number'] *= tokens[index+1]['number']

        # わり算の記号であった場合
        elif tokens[index]['type'] == 'SLASH':
        
        # 0が後ろに来た場合は割れないのでエラーで返す
          try:
            tokens[index-1]['number'] /= tokens[index+1]['number']
          except ZeroDivisionError:
            print("Zero Division Error")
            exit(1)

        # 足し算と引き算の記号はここでは無視
        elif tokens[index]['type'] == 'PLUS' or tokens[index]['type']== 'MINUS':
          pass
        
        else:
          print('Invalid syntax')
          exit(1)       
      
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
    
  # 足し算と引き算 (サンプルそのまま)
  answer = 0
  new_tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(new_tokens):
    if new_tokens[index]['type'] == 'NUMBER':
      if new_tokens[index - 1]['type'] == 'PLUS':
        answer += new_tokens[index]['number']
      elif new_tokens[index - 1]['type'] == 'MINUS':
        answer -= new_tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1 

  return answer


def test(line):
  tokens = tokenize(line)
  actual_answer = evaluate(tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
  print("==== Test started! ====")
  test("1+2*5")
  test("1+2")
  test("1.0+2.1-3")
  test("1/2+5")
  print("==== Test finished! ====\n")

run_test()


while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)