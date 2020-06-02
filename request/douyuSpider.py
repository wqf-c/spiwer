from selenium import webdriver
import json
import time

class douyu_spider:

    def __init__(self):
        self.base_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome("D://softwareinstall//python//python36//chromedriver.exe")

    def write_file(self, content_list):
        with open("douyu.txt", 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write('\n')

    def extract_data(self):
        liList = self.driver.find_elements_by_class_name("layout-Cover-item")
        contentList = []
        for li in liList:
            item = {"title": li.find_element_by_class_name("DyListCover-intro").text,
                    "broadcaster": li.find_element_by_class_name("DyListCover-user").text,
                    "hot": li.find_element_by_class_name("DyListCover-hot").text}
            print(item)
            contentList.append(item)
        next_url = self.driver.find_elements_by_class_name("dy-Pagination-next")
        next_url = next_url[0] if len(next_url) > 0 else None
        return contentList, next_url

    def run(self):
        self.driver.get("https://www.douyu.com/directory/all")
        time.sleep(5)
        contentList, next_url = self.extract_data()
        self.write_file(contentList)
        while next_url is not None:
            next_url.click()
            time.sleep(5)
            contentList, next_url = self.extract_data()
            self.write_file(contentList)


if __name__ == '__main__':
    douyu = douyu_spider()
    douyu.run()