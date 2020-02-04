# 先定義一個會印出Hello的函式
# def say(msg):
#     print(msg)
# 呼叫已經被定義好的say函式
# say('Hello Function')
# say("Hello Python")
# 到底msg這個變數裡面的執事什麼要看我們傳進去的執到底是什麼為準

# 定義一個可以做加法的函式
# def add(n1, n2):
#     result = n1 + n2
#     print(result)
# 呼叫函式
# add(3, 4)
# add(7, 8)

# def 函式名稱(參數名稱):
#    函式內部程式碼
#    return # 結束韓式，回傳None 強制結束函式
#    return 資料(數字, 字串, 布林值, 物件, 字典)

# 函式回傳None
# def say(msg):
#     print(msg)
#     return

# 呼叫函式，取得回傳值
# value = say("Hello Function")
# print(value) # 印出None

# 函式環傳字串Hello
# def add(n1, n2):
#     result = n1 + n2
#     # return "Hello"
#     return result

# 呼叫韓式，取得回傳值
# value = add(3, 4)
# print(value) # 印出Hello
# print(value) # 印出 7

# 定義函式
# 函式內部的程式，若是沒有做韓式呼叫，就不會執行
# def multiply(n1, n2):
#     print(n1 * n2)

# 呼叫函式
# multiply(3, 4)
# multiply(10, 8)
# value = multiply(3, 4)
# print(value)    # 回傳值為None，因為沒有寫回傳得值

# 定義函式
# 函式內部的程式，若是沒有做韓式呼叫，就不會執行
# def multiply(n1, n2):
#     print(n1 * n2)
#     return 10

# 呼叫函式
# value = multiply(3, 4)
# print(value)
# 會印出12再印出10

# 定義函式
# 函式內部的程式，若是沒有做韓式呼叫，就不會執行
# def multiply(n1, n2):
#     return n1 * n2

# 呼叫函式
# value = multiply(3, 4) + multiply(10, 5)
# print(value)
# 寫return的好處就是可以做整合而且復用性高

# 程式的包裝
# 把下面的兩段鬼東西變成一包
# sum = 0
# for n in range(1, 11):
#     sum += + n
# print(sum)

# sum = 0
# for n in range(1, 21):
#     sum += + n
# print(sum)

# def calculate(max):
#     sum = 0
#     for n in range(1, max + 1):
#         sum += + n
#     print(sum)

# calculate(10)
# calculate(20)
# 函式可用來做程式的包裝，同樣的邏輯可以重複利用