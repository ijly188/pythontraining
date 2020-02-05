# 檔案操作流程
# 檔案開啟 > 讀取或寫入 > 關閉檔案

# 檔案物件 = open(檔案路徑, mode=開啟模式)
# 這樣可以得到一個檔案物件，就可以操作這個檔案了
# 開啟模式：讀取模式 - r, 寫入模式 - w, 讀寫模式 - r+

# 讀取檔案
# 讀取全部文字：檔案物件.read() 一次讀取全部文字

# 一次讀取一行
# for 變數 in 檔案物件:
#     從檔案依序讀取每行文字到變數中

# 一次讀取一行
# for 變數 in 檔案物件:
#     從檔案依序讀取美航文字到變數中

# 讀取 json 格式
# import json
# 讀取到的資料 = json.load(檔案物件)

# 寫入文字
# 檔案物件.write(字串)

# 寫入換行符號
# 檔案物件.write("這是範例文字\n")

# 寫入 json 格式
# import json
# json.dump(要寫入的資料, 檔案物件)

# 關閉檔案 - 這樣才可以釋放記憶體資源
# 檔案物件.close()

# 最佳實務語法
# with open(檔案路徑, mode=開啟模式) as 檔案物件:
#     讀取或寫入檔案的
# 以上區塊會自動、安全的關閉檔案
# 跟 try catch 內容相關

# 儲存檔案
# 當原本沒有這隻檔案的時候就會自動幫你新建這隻檔案
# 有檔案的時候就會把原本的內容全部複寫
# file = open("data.txt", mode="w", encoding="utf-8")       # 開啟
# file.write("Hello File\nSecond Line")                     # 操作
# file.write("測試中文\n好棒棒")                              # 操作
# file.close()                                              # 關閉
# 現在這樣做完因為沒有把檔案關就又在做寫入，會變成
# 如果這邊只有純中文的話會變成用big5就會碰到utf-8問題了
# Hello File
# Second Line測試中文
# 好棒棒
# 處理中文問題有可能牽涉到編碼問題，現在中文最常用的是utf-8
# 用最佳寫法去做上面的事
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("5\n3")

# 讀取檔案
# 如果檔案不存在會報錯：FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data = file.read()
# print(data)

# 逐行把資料讀出來以後再做計算
# sum = 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file:
#         sum += int(line)
# print(sum)

# 使用 JSON 格式讀取、複寫檔案
# config.json的檔案內容為：{"name": "My Name","version": "1.2.5"}
import json

with open("config.json", mode="r") as file:
    data = json.load(file)
# python字典的操作只能用[]去讀key不像js可以用.的方式去讀取
print(data)
print("name:", data['name'])
data["name"] = "New Name"
print("name:", data['name'])
print("version:", data['version'])

# 確定資料正確以後把資料複寫回原本的json檔案
with open("config.json", mode="w") as file:
    json.dump(data, file)
# 這樣就可以回寫進檔案了