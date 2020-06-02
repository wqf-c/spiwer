import requests
import json
from lxml import etree


class Tieba:
    def __init__(self, tieba_name):
        self.url = "https://tieba.baidu.com/mo/q/m?word=" + tieba_name + "&page_from_search=index&tn6=bdISP&tn4=bdKSW&tn7=bdPSB&lm=16842752&lp=6093&sub4=%E8%BF%9B%E5%90%A7&pn={}&"
        self.name = tieba_name
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Mobile Safari/537.36"
        }

    def write_file(self, contentList):
        with open(self.name + ".txt", 'a', encoding='utf-8') as f:
            for content in contentList:
                f.write(json.dumps(content, indent=2, ensure_ascii=False))

    def parse_url(self, url):
        response = requests.get(url, headers=self.header)
        return response.content

    def get_content_list(self, text):
        html = etree.HTML(text)
        liList = html.xpath("//li[@class='tl_shadow tl_shadow_new ']")
        items = []
        for li in liList:
            item = {}
            item["content"] = li.xpath("./a/div/span/text()")[0] if len(li.xpath("./a/div/span/text()")) > 0 else None
            item["url"] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href")) > 0 else None
            item["imageList"] = li.xpath("./a//div[contains(@class, 'medias_item ')]/img/@src")
            items.append(item)
        return items

    def get_total_page(self):
        #通过js动态设置在页面上，所以不能通过这种方式获取页码
        #content = self.parse_url(self.url.format(0))
        #print(content)
        #print(etree.HTML(content).xpath("//input[@class='j_pager_input']/@value"))
        return 3
        #return etree.HTML(content).xpath("//input[@class='j_pager_input']/@value")[0].split('/', -1)[1]

    def run(self):
       # print('*' * 10 + self.get_total_page())
        for i in range(self.get_total_page()):
            self.write_file(self.get_content_list(self.parse_url(self.url.format(i*30))))

if __name__ == "__main__":
    tieba = Tieba("做头发")
    tieba.run()