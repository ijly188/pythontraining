# 集合的運算
# s1 = {3 ,4, 5}
# print(3 in s1)      # 如果 3 有在s1裡面的就會回true
# print(3 in s1)      
# print(10 not in s1)   

# 集合的運算
# s1 = {3,4,5}
# s2 = {4,5,6,7}
# s3 = s1 & s2          # 交集：取兩個集合中，相同的部分->{4,5}
# s3 = s1 | s2          # 聯集：取兩個集合中的所有資料，但不重複->{3,4,5,6,7}
# s3 = s1 - s2          # 差集：從 s1 中，減去和 s2 重疊的部分->{3}
# s3 = s2 - s1          # 差集：從 s2 中，減去和 s1 重疊的部分->{6, 7}
# s3 = s1 ^ s2          # 反交集：取兩個集合中，不重疊的部分，就是兩個集合取聯集後去掉交集
# print(s3)

# s = set("Hello")      # set(字串)->{'l', 'e', 'o', 'H'}，重複不進入，順序隨機
# print(s)
# print("H" in s)       # True
# print("A" in s)       # False

# 字典的運算

# dic = { 
#     "apple": "蘋果",
#     "bug": "蟲蟲"
# }
# print(dic["apple"])   # 蘋果
# dic["apple"] = "小蘋果"
# print(dic)

# print("apple" in dic) # 判斷 key 是否存在
# print("test" in dic)  # 判斷 key 是否存在
# print("test" not in dic)  # 判斷 key 是否存在

# print(dic)
# del dic["apple"]      # 刪除字典中的鍵值
# print(dic)

# dic = {x:x*2 for x in [3,4,5]}  # 從列表的資料產生字典
# print(dic)