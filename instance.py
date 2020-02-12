# basic 的用法

# 類別的兩種用法
# 1. 類別與類別屬性
# 2. 類別與實體物件、實體屬性
# 把兩種用法分開來看不然會搞混

# 實體物件
# 先定義類別，再透過類別建立實體物件
# 先建立實體物件，才能使用實體屬性

# 建立實體物件
# class 類別名稱:
#     # 定義初始化函式
#     def __init__(self):
#         透過操作self來定義實體屬性
#     # 定義實體方法 / 函式
#     def 方法名稱(self, 更多自訂參數):
#         方法主體，透過 self 操作實體物件
# # 建立實體物件，放入變數obj中
# obj = 類別名稱() ＃ 呼叫初始化函式

# 程式範例 1
# class Point:
#     def __init__(self):
#         self.x = 3
#         self.y = 4
# 建立實體物件
# 此實體物件包含 x 和 y 兩個實體屬性
# Point()呼叫初始化函式
# px = Point().x
# print(px)

# 程式範例 2
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# 建立實體物件
# 建立時，可直接傳入參數資料
# 要記得他封裝是包兩層
# p = Point(1, 5)
# print(p.x + p.y)

# Point 實體物件的設計：平面座標上的點
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# # 建立第一個實體物件
# p1 = Point(3, 4)
# print(p1.x, p1.y)
# # 建立第二個實體物件
# p2 = Point(5, 6)
# print(p2.x, p2.y)

# FullName 實體物件的設計：分開紀錄姓、名資料的全名
# class FullName:
#     def __init__(self, first, last):
#         self.first = first
#         self.last  = last
# name1 = FullName("C.W.", "Peng")
# print(name1.first, name1.last)
# name2 = FullName("T.Y.", "Lin")
# print(name2.first, name2.last)

# senior 的用法
# 實體物件.實體方法名稱(參數資料)
# 程式範例
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x, self.y)

# p = Point(1, 5)     # 建立實體物件
# p.show()            # 呼叫實體方法

# Point 實體物件的設計：平面座標上的點
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x, self.y)
#     def distance(self, targetX, targetY):
#         return (((self.x - targetX) ** 2) + ((self.y - targetY) ** 2)) ** 0.5
# p = Point(3, 4)
# p.show()            # 呼叫實體方法 / 函式
# result = p.distance(0, 0)    # 計算座標 3, 4 和座標 0, 0 之間的距離
# print(result)

# File 實體物件的設計：包裝檔案讀取的程式
class File:
    # 大略流程為
    # 定義檔案名稱，開啟檔案，讀取檔案，內容轉移到變數上，把檔案關掉
    def __init__(self, name):
        self.name = name
        self.file = None            # 尚未開啟檔案：初始化資料是 None，代表空
    # 實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 因為上面做的封裝以後，接下來去call這些方法可以把很多本來原型的程式變得比較簡單就可以使用

# 使用file class
# 讀取第一個檔案
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)
# 讀取第二個檔案
f2 = File("data2.txt")
f2.open()
data = f2.read()
print(data)