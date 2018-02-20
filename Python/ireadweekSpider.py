# ireadweek.com  爬虫
from bs4 import BeautifulSoup
import requests

class Spider:
    def __init__(self, url):
        self.url = url

    def getHTMLText(self, url):
        try:
            r = requests.get(url, timeout = 30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""

    def getnextHTMLInfo(self, html):
        if html:
            soup = BeautifulSoup(html, "html.parser")
            divLink = soup.find('div', attrs={'class': 'hanghang-shu-content-btn'})
            booklink = divLink.contents
            return booklink[1].get_attribute_list("href")

    def getInfo(self, html):
        BookListInfo = []
        if html:
            soup = BeautifulSoup(html, "html.parser")
            bookList = soup.find('ul', attrs={'class': 'hanghang-list'})
            for child in bookList:
                bookInfo = []
                if child.name == 'a':
                    b = child.li.find_all('div')
                    bookInfo.append(b[0].string)
                    bookInfo.append(b[1].string)
                    bookInfo.append(b[2].string)
                    childbook = child           # 下一个页面的链接
                    blink = childbook.get_attribute_list("href")
                    blink = 'http://ireadweek.com'+blink[0]
                    htmlbook = self.getHTMLText(blink)
                    bookhref = self.getnextHTMLInfo(htmlbook)
                    bookInfo.append(bookhref)
                if bookInfo:
                    BookListInfo.append(bookInfo)

            return BookListInfo

    def printInfo(self, List):
        mat = '{:^20}\t{:^10}\t{:^20}\t{:^40}'
        with open('bookList.txt', 'a', encoding='utf-8') as f:
            for i in List:
                try:
                    f.write(mat.format(i[0], i[1], i[2], i[3][0]) + '\n')
                except:
                    f.write('{:^20}'.format(i[0]) + '此书信息不全' + '\n')

    def SpiderRun(self):
        Indexhtml = self.getHTMLText(self.url)
        booklistinfo = self.getInfo(Indexhtml)
        self.printInfo(booklistinfo)


if __name__ == '__main__':
    for num in range(1,195):
        s = Spider('http://ireadweek.com/index.php/index/' + str(num) + '.html')
        s.SpiderRun()



