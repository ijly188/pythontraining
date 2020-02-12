# 網路爬蟲 web crawler 基本篇
# 基本流程
# 1. 連線到特定網址，抓取資料
# 2. 解析資料，取得實際想要的部分

# 最重要的關鍵：盡可能地讓城市模仿一個普通使用者的樣子

# Cookie是：網站存放在瀏覽器中的一小段資料
# 與伺服器的互動：連線時，放在 Request Headers 中送出

# 追蹤連結
# 就是去追蹤網頁超連結，再連過去的動作
# 連續抓取頁面實務
# 解析頁面的超連結，並結合程式邏輯完成要抓的資料建構

# 目標是抓 PTT 八卦版的連結，因為他有擋一層是否滿18歲的內容，我們要繞過這層才能去抓到其他的東西
import urllib.request as req

def getData(pageurl):
    request = req.Request(pageurl, headers= {
        # "cookie": "_ga=GA1.2.1642941289.1577064811; __cfduid=d4a3cf8b226142c3dc097855ef990bc5c1581487037; _gid=GA1.2.493286021.1581487038; over18=1",
        "cookie": "over18=1",
        # 上面兩行效果一樣
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4053.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 這邊進去之後會發現整個頁面流程被 PTT 八卦版未滿 18 歲的那個部分擋住了
    # 擋住的機制是用cookie
    # 所以這個地方我們使用開發者工具去找 Application 裡面的 cookie 的地方
    # 看到 coolie 裡面的內容會看到一個 over18 = 1
    # 再度回到 Request 我們再看一次他的 Headers 裡面的 cookie 欄位會發現一樣有帶 over18 的欄位
    # print(data)

    import bs4

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 抓取上一頁的連結
    # 找到內文是 ‹ 上頁 的 a 標籤
    nextLink = root.find("a", string = "‹ 上頁")
    return nextLink["href"]

# 主程序：抓取多個頁面的標題
# 抓取 PTT 八卦版標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
# pageURL = "https://www.ptt.cc" + getData(pageURL)
# print(pageURL)
# 後面可以用遞迴去 call 方法也可以用迴圈去跑
count = 0
while count < 5:
    pageURL = "https://www.ptt.cc/" + getData(pageURL)
    count += 1