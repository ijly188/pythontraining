# class就是python裡面的類別，就是oop那套，基本上可以把所有你想得到的東西封裝在class裡面，再看要怎麼去call他
# 要先定義類別 > 才能使用類別中封裝的屬性（不論程式或者變數）
# 基本語法
# class （首字大寫）類別名稱:
#     定義封裝的變數
#     定義封裝的函式

# 定義 Test 類別
# class Test:
#     x = 3      # 定義變數
#     def say(): # 定義函式
#         print("Hello")
# print(Test.x + 3)
# Test.say()

# 定義類別、與類別屬性（封裝在類別中的變數和函式）
# 定義一個類別 IO，有兩個屬性 suportedSrcs 和 read
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:     # 判斷進來的src是不是在supportedSrcs的這個列表裡面的語法
            print("Not Supported")
        else:
            print("Read from", src)
# 使用類別
# print(IO.supportedSrcs)
# IO.read("file")
IO.read(IO.supportedSrcs[1])
IO.read("internet")
