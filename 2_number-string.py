# 數字運算
x1 = 3+6
x2 = 3-6
x3 = 3/6      # 小數除法
x4 = 3//6     # 整數除法
x5 = 7/6
x6 = 7//6
x7 = 2**3
x8 = 2**0.5   # 開根號
x9 = 7%3      # 取餘數
print(x1, x2, x3, x4, x5, x6, x7, x8, x9)

x = 2+3
print(x)
# x = x+1
# x++        # 這個會報錯
x += 1
# x -= 1
# x *= 2
# x /= 2
print(x)

# 字串運算
# s = "Hello"
# s = 'Hell\"o' + ' World' # 用跳脫字元
# s = 'Hell\"o' ' World' # 用跳脫字元
# s = 'Hell\"o\n World' # 用跳脫字元
# s = '''
# Hell\"o' + ' World
# ''' # 用跳脫字元
# s = "Hello" * 3 + "World"
# print(s)
# 字串會對內部的字元編號（索引），從 0 開始算起
s="Hello"
# print(s[0], s[3])
# print(s[1:4])
# print(s[1:])
print(s[:4])
