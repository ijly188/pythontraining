# while 迴圈
# while 布林值:
#     若布林值為 True，執行命令
#     回到上方，做下一次的迴圈判斷
# n = 1
# while n <= 5:
#     print("變數 n 的資料是：", n)
#     n += 1
# 小心無限迴圈問題
# n = 1
# while True:
#     print(n)
#     n+=1
# 做一個 1 + 2 + 3 + .... + 10
# n = 1
# sum = 0
# while n <= 10:
#     sum = sum + n
#     n += 1
# print(sum)

# for 迴圈
# for 變數名稱 in 列表或字串:
#     將列表中的項目或字串中的字元逐一取出，逐一處理
# for x in [ 4, 1, 2 ]:
#     print("逐一取得列表中的資料", x)

# for x in { 4, 1, 2 }:
#     print("逐一取得列表中的資料", x)        # 幾乎可以想像成在用foreach的那個做法在parser object

# for c in "Hello":
#     print("逐一取得字串中的字元", c)

# range()
# for 變數名稱 in range(3):
# 相當於
# for 變數名稱 in [0,1,2]:
# for 變數名稱 in range(3, 6):
# 相當於
# for 變數名稱 in [3, 4, 5]:

sum = 0
for x in range( 1, 11 ):
    # sum += x
    sum = sum + x
print(sum)