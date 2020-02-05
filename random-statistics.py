# 載入模組
import random

data = [ 0, 1, 5, 8 ]
# 從列表中隨機選取 1 個資料
rd1 = random.choice(data)
print(rd1)

# 從列表中隨機選取 n 個資料
rd2 = random.sample(data, 2)
print(rd2)
# return [0,5]

# 隨機調換順序
# 將列表的資料「就地」隨機調換順序

# rd3 = random.shuffle(data)
# print(rd3)
# 這樣寫會報錯因為現在被改的東西是data本身，而且他們沒return所以你這樣賦值也沒有用，就是洗牌的概念
rd3 = data
random.shuffle(rd3)
print(rd3)

# 隨機亂數
# 取得 0.0 ~ 1.0 之間的隨機亂數
rd01 = random.random()
print(rd01)
rd02 = random.uniform(0.0, 1.0)            # uniform 機率相同
print(rd02)


# 常態分配亂數
# 取得平均數 100、標準差 10 的
# 常態分配亂數
rd4 = random.normalvariate(100, 10) # 取出來的值大部分都會在 100 +- 10 裡面
print(rd4)

# 統計模組
# import statistics
import statistics

# 計算列表中數字的中位數
data = [1, 4, 6, 9]
md = statistics.median(data)
print(md)

# 計算列表中數字的標準差，表達資料散佈的狀況，資料彼此之間的差距有沒有很大
st = statistics.stdev(data)
print(st)

# 平均數
meandata = statistics.mean(data)
print(meandata)