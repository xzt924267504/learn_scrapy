
"""
教程 :
https://blog.csdn.net/dangsh_/article/details/78617178

css :
response.css('span#subject_tpc')                                    选择id为subject_tpc的span标签

response.css("div a::attr(href)")                                  查找div下面a标签的所有href的内容
response.css(".post img::attr(src)").getall()                      class= post下面img标签的所有src="xxxx"
a[title]                                                           选取所有拥有title属性的a元素
a[href*=”www.lagou.com”]                                         选取所有href属性值中包含www.lagou.com的a元素
a[href^=”http”]                                                  选取所有href属性值中以http开头的a元素
response.css(".col-mb-12 col-8")>>response.css(".col-mb-12.col-8") 碰到class有空格时, 把空格换成.就可以

a[href^=”http”]
xpath :
response.xpath('//a[contains(@href,"xxxx")]/@href').getall()       查找属性名称包含xxxx的所有的超链接，通过contains实现
response.xpath('//td[@class="mc_content"]//@href ')                利用class定位 含有这个class属性的td标签下面的所有href的内容
a=response.xpath('//a[re:test(text(),"\w{4}")]')                   利用text结合正则表达式定位
response.xpath('//td[@class="mc_content"]')
//ol[@class="page-navigator"]
response=Request("",meta = { 'dont_redirect': True})


此外，xpath还有对于html元素操作的两个实用的函数（可以用正则表达式代替）——starts-with和contains；
a=response.xpath('//span[starts-with(@title,"看官")]')
a=response.xpath('//a[contains(text(),"要匹配的蚊子")]')

response.xpath('//*[@id="main"]/div[1]/span[1]')





if next_page is not None:  # 判断是否存在下一页
     如果是相对路径，如：/page/1
     urljoin能替我们转换为绝对路径，也就是加上我们的域名
     最终next_page为：http://lab.scrapyd.cn/page/2/


    next_page = response.urljoin(next_page)


    接下来就是爬取下一页或是内容页的秘诀所在：
    scrapy给我们提供了这么一个方法：scrapy.Request()
    这个方法还有许多参数，后面我们慢慢说，这里我们只使用了两个参数
    一个是：我们继续爬取的链接（next_page），这里是下一页链接，当然也可以是内容页
    另一个是：我们要把链接提交给哪一个函数(callback=self.parse)爬取，这里是parse函数，也就是本函数
    当然，我们也可以在下面另写一个函数，比如：内容页，专门处理内容页的数据
    经过这么一个函数，下一页链接又提交给了parse，那就可以不断的爬取了，直到不存在下一页


    yield scrapy.Request(next_page, callback=self.parse)
"""
