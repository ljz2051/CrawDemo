__author__ = 'LiJinZhong'
import requests
import re
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 300)
        print(r.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        print(plt[:10])
        print(tlt[:10])
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append((price,title))
    except Exception :
        print("error")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = "键盘"
    depth = 2
    start_url = " https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(i*48)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)
main()
