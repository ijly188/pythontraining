# 載入模組
# import urllib.request as request

# with request.urlopen(網址) as response:
#     data = response.read()
# print(data)

# 網路連線
# import urllib.request as request
# src = "http://web.jour.mcu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")      #   取得銘傳大學新聞系網站的原始碼，並且使用utf-8解碼
# print(data)
# 行政院資料開放諮詢小組會議紀錄
import urllib.request as request
import json
src = "https://file.data.gov.tw/content/%E8%A1%8C%E6%94%BF%E9%99%A2%E8%B3%87%E6%96%99%E9%96%8B%E6%94%BE%E8%AB%AE%E8%A9%A2%E5%B0%8F%E7%B5%84%E6%9C%83%E8%AD%B0%E7%B4%80%E9%8C%84_.json"
with request.urlopen(src) as response:
    data = json.load(response)
# print(data + '\n\n\n')
# 取得會議名稱
# meetinglist = data['']    # 因為有些會把json做result裡面放資料所以多放這邊一層
with open('open-data.txt', 'w', encoding='utf-8') as file:
    # print('會議名稱 時間 地點 主席 出席委員 會議紀錄 簡報 附件')
    datatitle = '會議名稱 時間 地點 主席 出席委員 會議紀錄 簡報 附件'
    file.write(datatitle + '\n')
    for meetingdata in data:
        meetingname     =   meetingdata['會議名稱']
        meetingtime     =   meetingdata['時間']
        meetingplace    =   meetingdata['地點']
        meetingowner    =   meetingdata['主席']
        meetingpeople   =   meetingdata['出席委員']
        meetingrecord   =   meetingdata['會議紀錄']
        meetingppt      =   meetingdata['簡報']
        meetingfile     =   meetingdata['附件']
        # print(meetingname + ' ' + meetingtime + ' ' + meetingplace + ' ' + meetingowner + ' ' + meetingpeople + ' ' + meetingrecord + ' ' + meetingppt + ' ' + meetingfile + '\n')
        file.write(meetingname + ' ' + meetingtime + ' ' + meetingplace + ' ' + meetingowner + ' ' + meetingpeople + ' ' + meetingrecord + ' ' + meetingppt + ' ' + meetingfile + '\n')
# 把open data裡面的json接下來然後轉存成一般檔案

# 串接、擷取公開資料