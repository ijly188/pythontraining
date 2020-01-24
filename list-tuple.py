# 有序可變動的列表List
# grades = [12, 60, 15, 70, 90]
# print(grades[0])                # 跟js要印出array方法一樣

# grades[0] = 55                  # 把 55 放到列表中的第一個位置
# print(grades)
# grades[1:4] = []                # 連續商除列表中編號 1 到編號 4 （不包括）的資料
# grades = grades + [12, 33]
# length = len(grades)            # 取得列表長度，就是length()的概念囉
# print(grades[1:4])
# print(grades)
# print(length)

# data = [[3,4,5],[6,7,8]]
# print(data[0][0])
# data[0][0:2] = [5,5,5]          # 可以用這樣的方式來讓我們的資料被新增哦
# print(data[0])

# 有序不可變動列表Tuple
data = (3,4,5)
# data[0] = 5                     # 錯誤：Tuple資料不可更動
# 錯誤訊息
# Traceback (most recent call last):
#   File "list-tuple.py", line 21, in <module>
#     data[0] = 5
# TypeError: 'tuple' object does not support item assignment
print(data[0:2])