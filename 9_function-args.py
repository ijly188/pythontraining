# 參數的預設資料
# def power(base, exp=0):
#     print(base**exp)     # 兩個**是幾次方的意思
# power(3, 2)              # 9
# power(4)                 # 如果上面的exp沒有給預設值為0的話，會因為沒有給exp的變數為空所以會報錯

# 使用參數名稱對應
# def divide(n1, n2):
#     print(n1/n2)
# divide(2, 4)
# divide(n2=2, n1=4)

# 無限/不定參數資料
# def avg(*numbers):
#     # print(numbers)
#     sum = 0
#     for n in numbers:
#         sum += n
#     print(sum/len(numbers))

# avg(3, 4)
# avg(3, 5, 10)
# avg(1, 4, -1, -8)
# avg(1, 1, 2)