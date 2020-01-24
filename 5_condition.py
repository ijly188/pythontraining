# 判斷式
# 語法為
# if 布林值:
#     若布林值為True，執行命令
# elif 布林值二:
#     若布林值二為True，執行命令
# else:
#     若布林值為False，執行命令

# 程式範例
# x = input("請輸入數字：")       # 基本輸入為字串型態
# x = int(x)                    # 轉換為整數型態
# if x > 200:
#     print("大於 200")
# elif x > 100:
#     print("大於 100，小於 200")
# else:
#     print("小於 100")
# python 不支援 switch 語法

# if True:
#     print("True 執行")

# if False:
#     print("True 執行")
# x = input("請輸入數字：")         # 取得字串形式的使用者輸入
# x = int(x)                      # 將字串轉換成數字型態
# if x > 100:
#     print("大於 100")
# else:
#     print("小於等於 100")

# x = input("請輸入數字：")         # 取得字串形式的使用者輸入
# x = int(x)                      # 將字串轉換成數字型態
# if x > 200:
#     print("大於 200")
# elif x > 100:
#     print("大於 100，小於等於 200")
# else:
#     print("小於等於 100")

# 四則運算
n1 = int(input("請輸入數字一："))
n2 = int(input("請輸入數字二："))
op = input("請輸入運算：+, -, *, /：")

if op == "+":
    print( n1 + n2)
elif op == "-":
    print( n1 - n2)
elif op == "*":
    print( n1 * n2)
elif op == "/":
    print( n1 / n2)
else:
    print("不支援的運算")

# print(n1 + n2)