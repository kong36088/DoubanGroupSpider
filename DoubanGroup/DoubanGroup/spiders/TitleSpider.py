import scrapy

from DoubanGroup.items import DoubangroupItem


class TitleSpider(scrapy.Spider):
    name = "title"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    current_group = ''

    def start_requests(self):
        for group in self.settings['GROUPS']:
            self.current_group = group

            current_url = 'https://www.douban.com/group/' + group + '/discussion?start=0'
            last_url = current_url
            for num in range(0, int(self.settings['CRAW_NUM']), 25):
                current_url = 'https://www.douban.com/group/' + group + '/discussion?start=' + str(num)
                self.headers['Referer'] = 'Referer:' + last_url
                last_url = current_url

                yield scrapy.Request(url=current_url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        content = response.css('.article').xpath('//tr')
        content = content[2:]
        for con in content:
            item = DoubangroupItem()

            item['url'] = con.xpath('td//@href')[0].extract()
            item['group_id'] = self.current_group
            item['title'] = con.xpath('td/a//@title')[0].extract()

            try:
                author = con.xpath('td/a')[1].xpath('text()')[0].extract()
            except:
                author = '非法名称'
            item['author'] = author

            try:
                reply_num = con.xpath('td')[2].xpath('text()')[0].extract()
            except:
                reply_num = 0

            item['reply_num'] = reply_num
            item['last_reply_time'] = con.xpath('td')[3].xpath('text()')[0].extract()
            yield item
