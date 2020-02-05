# 11_package.py
# 做成 package 的資料夾結構
# -專案資料夾
#     -主程式.py
#     -封包資料夾
#         -__init__.py
#         -模組一.py
#         -模組二.py

# 這次目標是
# -專案資料夾
#     -main.py
#     -geometry
#         -__init__.py
#         -point.py
#         -line.py

# 基本語法
# import 封包名稱.模組名稱
# import 封包名稱.模組名稱 as 模組別名

# 主程式
import geometry.point

result = geometry.point.distance(3, 4)
print("距離", result)

import geometry.line as line
result = line.slope( 1, 1, 3, 3 )
print("斜率", result)
