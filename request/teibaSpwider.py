import requests


class TiebaSpiwer:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36",
            "Cookie": "PSTM=1574481445; BD_UPN=12314753; BIDUPSID=4CD5ACF1911ADC42245E98DCD271C695; BAIDUID=AC8C6714D17504DFFD947389554E196B:FG=1; BDUSS=XctUlFYN0p6ZEozZnc0NnBDVXRzeTUzeEN0S3J3Wlh4OUlHYTNYUmVsMDdRQUJlRVFBQUFBJCQAAAAAAAAAAAEAAABl2j6bztIyODQ2NjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADuz2F07s9hdN; MCITY=-131%3A; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31657_1423_31672_21085_31596_31463_31321_30824; H_PS_645EC=6fd6S7UhhGC7hdSNjKK1LF9msHgwEv0VzJt8pJcIzSI5FDjZLYNvzzRJzD0wlVeXTUNU; delPer=0; BD_CK_SAM=1; PSINO=3; BDSVRTM=104; WWW_ST=1589645411073"}
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        pass

    def get_url_list(self):
        self.url_list = []
        for i in range(5):
            self.url_list.append(self.url_temp.format(i * 50))

    def parse_url(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()

    def save_file(self, filename, content):
        dirction = "D://code//python//spiwer//data//tieba//"
        with open(dirction + filename, "w", encoding="utf-8") as f:
            f.write(content)
            print(filename + "writed")

    def run(self):
        self.get_url_list()
        for url in self.url_list:
            content = self.parse_url(url)
            filename = "{}吧第{}页.html".format(self.tieba_name, self.url_list.index(url))
            self.save_file(filename, content)
        pass


if __name__ == '__main__':
    tiebaSpilder = TiebaSpiwer("李毅")
    tiebaSpilder.run()
