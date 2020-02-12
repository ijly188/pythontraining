# 網路爬蟲 web crawler 基本篇
# 基本流程
# 1. 連線到特定網址，抓取資料
# 2. 解析資料，取得實際想要的部分

# 最重要的關鍵：盡可能地讓城市模仿一個普通使用者的樣子
# 用ua等等的東西去連線
# 使用第三方套件BeautifulSoup來做資料解析Html

# 安裝套件的方法透過pip去做套件管理
# command: pip install beautifulsoup4

# 這次目標是抓ptt電影版的標題
# 用 mac 開爬蟲常常會遇到的 ssl 問題
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# 抓取 PTT 電影版的網頁原始碼(HTML)
import urllib.request as req

# 主要連結的網址 PTT 電影版
url = "https://www.ptt.cc/bbs/movie/index.html"
# 我們要加工我們headers的地方
# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4053.0 Safari/537.36"
})

# 這裡要注意一定要放上面建立的物件不能只放我們剛剛前面做的 url 網址而已不然你加的 User-Agent 不會生效
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
# 直接這樣打完以後我們的連線被拒絕了，所以我們要看一下這邊的錯誤回應
# urllib.error.HTTPError: HTTP Error 403: Forbidden
# 因為我們現在這樣的連線看起來太不像正常人類了
# 我們先打開開發人員工具，去找Network裡面來看我們目前的request
# 因為我們要看連到這個網頁本身的那個request我們要去找我們連線的時候會帶的header，透過這些東西去模擬我們是一個一般使用者
# 主要影響的是Headers裡面的Request Headers把這邊的Header帶進去看看

# 解析原始碼，取得每篇文章的標題
# 使用第三方套件beautifulsoup4
import bs4
root = bs4.BeautifulSoup(data, "html.parser")   # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
# print(root.title.string)                        # 這樣可以取得這頁的<title></title>的內容：看板 movie 文章列表 - 批踢踢實業坊
# titles = root.find("div", class_="title")       # 尋找class="title"的div標籤，但是只找到一個
# print(titles.a.string)
titles = root.find_all("div", class_="title")   # 尋找class="title"的div標籤，找到所有符合條件的標籤
# print(titles)                                   # 這樣出來的結果會是一個list，就是[]的資料，接著我們再去解這個的資料
for title in titles:
    if title.a != None:                         # 標題含有 a 標籤，就印出來
        print(title.a.string)
