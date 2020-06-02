import requests
import json
import re


class MusicSpiwer:
    def __init__(self, music, direction="D://KuGou//"):
        self.music = music
        self.direction = direction
        self.dataSource = ["netease", "kugou", "xiami"]
        self.sourceIndex = 0

    def getMusicId(self):
        musicId = None
        for i in range(self.dataSource.__len__()):
            try:
                data = {"types": "search", "count": 20, "source": self.dataSource[i], "name": self.music}
                response = requests.post(
                    url="http://www.gequdaquan.net/gqss/api.php?callback=jQuery111307203118624950957_1589700946929",
                    data=data)
                if response.status_code != 200:
                    continue
                else:
                    ret = re.findall("jQuery111307203118624950957_1589700946929\((.*)\)", response.content.decode())[0]
                    musicJson = json.loads(ret)
                    if musicJson.__len__() != 0:
                        musicId = musicJson[0]["id"]
                        self.sourceIndex = i
                        return musicId
                    else:
                        continue
            except:
                pass
            return musicId

    def getMusicUrl(self, musicId):
        url = "http://www.gequdaquan.net/gqss/api.php?callback=jQuery111307203118624950957_1589700946929"
        data = {
            "types": "url",
            "id": musicId,
            "source": self.dataSource[self.sourceIndex]
        }
        try:
            response = requests.post(url=url, data=data)
            ret = re.findall("jQuery111307203118624950957_1589700946929\((.*)\)", response.content.decode())[0]
            musicJson = json.loads(ret)
            return musicJson["url"]
        except:
            return None

    def writeFile(self, musicUrl):
        li = musicUrl.split(".", -1)
        li.reverse()
        filName = self.direction + self.music + "." + li[0]
        print(filName)
        content = requests.get(musicUrl).content
        with open(filName, "wb") as f:
            f.write(content)

    def run(self):
        musicId = self.getMusicId()
        print(musicId)
        musicUrl = self.getMusicUrl(musicId)
        print(musicUrl)
        self.writeFile(musicUrl)
        pass


if __name__ == "__main__":
    music = MusicSpiwer("伤声")
    music.run()
