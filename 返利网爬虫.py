# -*- coding:utf-8 -*-
import urllib2,re
from bs4 import BeautifulSoup
import time
import socket
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#输出的内容

fanly_url = "http://zhide.fanli.com/p"#多页地址
format_url = "http://zhide.fanli.com/detail/1-"#商品链接

class Faly():
    def __init__(self):#初始化构造函数，self本身一定要位于第一位,且所有自定义函数必须有self
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        self.html_data = []#放置商品信息
    def get_html(self,start_page = 1, end_page = 10):
        for i in range(start_page,end_page):#range用来生成整数序列
            rt = urllib2.Request(fanly_url+str(i))#用地址去创建request对象，用于多页地址创建，拼接的过程fanly
            rt.add_header( 'User-Agent',self.user_agent)
            try:
                my_data = urllib2.urlopen(rt).read()#urlopen用于打开网页，read用于读取源码
                print my_data
                self.html_data.append(my_data)
                time.sleep(2)#等两秒的时间 减少爬的速度
                socket.setdefaulttimeout(15)#用来控制下载内容的时间 爬大型的网站 下载下不出来超时 就可以跳过 超时时间
            except urllib2.URLError,e:
                if hasattr(e,'reason'):#hasattr判断异常是否存在 若存在则直接打印
                    print u"连接失败",e.reason#字符串前面加u表示的是一个编码
        return str(self.html_data)


#html = Faly().get_html()
#获取商品的每一个ID
class GetData():
    def __init__(self):
        self.html = Faly().get_html()#调用网页商品的源码
        self.href = [] #放置id的列表
        self.ls = []
        self.url = []

    #获取href
    def get_hrefurl(self):
        reg = r'data-id="\d{6}"'#用来获取商品信息后来的编号正则
        result = re.compile(reg)#编译 提高效率
        tag = result.findall(self.html) #匹配
        #tag = re.findall(result,self.html)
        #print tag
        for i in tag:
            self.href.append(i)
            #print self.href #商品链接先隐藏掉
        #过滤重复信息 因为这个时候的输出有很多重复的商品id
        reg2 = r"\d{2}"
        result2 = re.findall(reg2,str(self.href))#括号里首先写正则表达式，
        if len(result2):#个数
            for data in result2:
                if data not in self.ls:#用到了ls空列表
                    self.ls.append(data)
                    url = format_url+str(data)#商品链接
                    self.url.append(url)
                    #print self.url[-1] 看商品完整链接的打印
        return self.url
a = GetData().get_hrefurl()

#获取商品的详细信息，之前的部分是对商品的过滤
class Href_mg():
    def __init__(self):
        self.list = GetData().get_hrefurl()#如何获取没一个超链接 调用函数
        self.txt_list = []#放置商品信息

    def show_mg(self):
        for item in range(len(self.list)):
            if len(self.list):
                url = str(self.list[item])
                mg = urllib2.Request(url)
                try:
                    req = urllib2.urlopen(mg).read() #每一页商品的源码
                    soup = BeautifulSoup(req,"html.parser")
                    txt = soup.find_all('h1')#使用parser的解析方式 找到所有h1的标签
                    self.txt_list.append(txt)
                    print self.txt_list
                except urllib2.URLError,e:
                    print e.reason
        return str(self.txt_list)

#data = Href_mg().show_mg()#这是调用函数 不调用没有办法使用 出错误urllib2.HTTPError: HTTP Error 506: Variant Also Negotiates
#有时候会有网络的错误 是因为我们还没有对show_mg捕获异常
if __name__ == "__main__":#判断文件的入口
    path = "yaozhi.txt"
    with open(path,'a')as file:#open打开文件 括号里先填路径 a是追加模式
        data = Href_mg().show_mg()#多页链接的内容操作
        reg4 = r'<.+?>'#匹配出很多杂七杂八的东西
        data_s=re.sub(reg4,' ',data).replace('全网最低','').replace(']','').replace(',','\n').strip().replace('  ','')
    #对不需要的东西用空格进行替换
        print data_s
        file.write(data_s)





