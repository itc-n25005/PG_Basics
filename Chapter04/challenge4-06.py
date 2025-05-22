def number():
   """
  #入力値の二乗を求めます。
  #また、メッセージと結果を出力します。
   """
   num = input("11:\n")
   result = int(num)** 2
   print(result)
number()   

def string(st):
    """
    #引数を受け取って出力します。
    """
    return print(st)
string("2 == 2")

g = 1
h = 3
i = 2

def number(a, b, c, y=7, z=5):
    """
    #３つの必須の引数と２つのオプション引数を受け取ります。
    """
    result = int(a + b + c + y + z)
    print(result)

number(g, h, i)

def division(a):
    """
    #引数として受け取った整数を２で割り、その結果を出力した。
    """
    result = a / 2
    print(int(result))
    return result
 
def multiplication(b):
    """
    #引数として受け取った整数を４で掛け、その結果を出力した。
    """
    result = b * 4
    print(int(result))
    return result

a = 8 
b = division(a)
multiplication(b)

def decimal(a):
 """
#文字列をfloat型に変換して、結果を出力する。
#また、例外処理として、NameErrorとValueErrorのときにメッセージを出力し、プログラムに返す。
 """
 try:
  """
  #エラーが発生する可能性のあるコード
  result=10/0
  print(result)
  """
  print(a)
  print(float(a))
 except ValueError:
  """
  #エラーが発生したときに実行するコード
  print("0で除算することはできません。")
  """
  print(7)
#a = str(2)
#a = str("あ")
a =str("")
decimal(a)






