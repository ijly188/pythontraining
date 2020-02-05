# 獨立的程式檔案
# 把一段程式寫在一個檔案中，讓這段程式可以被重複載入使用
# 載入模組的基本語法
# 就是import 模組名稱(不加.py)
# import 名稱 as 別名

# 基本語法
# import 模組名稱 as 模組別名
# import 模組名稱
# 模組名稱/別名.函式名稱(參數資料)
# 模組名稱或別名.變數名稱

# 內建模組
# sys 模組
# 取得系統重要資訊
# 載入 sys 模組
# import sys

# 使用 sys 模組
# print(sys.platform)     # 印出作業系統
# print(sys.maxsize)      # 印出整數型態的最大值
# print(sys.path)         # 印出搜尋模組的路徑

# 載入 sys 模組
# import sys as s

# 使用 sys 模組
# print(s.platform)       # 印出作業系統
# print(s.maxsize)        # 印出整數型態的最大值
# print(s.path)           # 印出搜尋模組的路徑

# 自訂模組
# 建立幾何運算模組
# 建立檔案geometry.py，定義平面幾何運算用的函式
# 載入與使用：載入geometry模組，並使用模組中定義的功能

# 載入內建的 sys 模組並取得資訊
# import sys as system

# print(system.platform)
# print(system.maxsize)
# print(system.path)

# 建立 geometry 模組，載入使用
# 當geometry跟10_module.py同層時
# import geometry

# result = geometry.distance(1, 1, 5, 5)
# print(result)

# result = geometry.slope(1, 2, 5, 6)
# print(result)

# 調整搜尋模組的路徑
import sys
sys.path.append("modules")  # 新增了一個模組搜尋路徑，加了這行以後會在sys.path裡面會看到多了一個'modules'
print(sys.path)             # 印出模組的搜尋路徑

import geometry
print(geometry.distance(1, 1, 5, 5))