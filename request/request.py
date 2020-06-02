import requests
import json

#verify=False忽略证书
proxies = {"http": "http://218.73.141.2:43322"}
kw = {'wd':'长城'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36",
           "Cookie": "PSTM=1574481445; BD_UPN=12314753; BIDUPSID=4CD5ACF1911ADC42245E98DCD271C695; BAIDUID=AC8C6714D17504DFFD947389554E196B:FG=1; BDUSS=XctUlFYN0p6ZEozZnc0NnBDVXRzeTUzeEN0S3J3Wlh4OUlHYTNYUmVsMDdRQUJlRVFBQUFBJCQAAAAAAAAAAAEAAABl2j6bztIyODQ2NjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADuz2F07s9hdN; MCITY=-131%3A; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31657_1423_31672_21085_31596_31463_31321_30824; H_PS_645EC=6fd6S7UhhGC7hdSNjKK1LF9msHgwEv0VzJt8pJcIzSI5FDjZLYNvzzRJzD0wlVeXTUNU; delPer=0; BD_CK_SAM=1; PSINO=3; BDSVRTM=104; WWW_ST=1589645411073"}
response = requests.get("https://www.baidu.com/s", headers=headers, params=kw, verify=False, timeout=10)
print(response.status_code)
print(response.request.url)
print(response.request.headers)
print(response.content.decode())
#百度翻译，pc端有些请求参数不好找可以试试移动端
data = {
    "kw": "人生苦短"
}

response = requests.post("https://fanyi.baidu.com/sug", data=data, headers=headers, proxies=proxies)
j = json.loads(response.content.decode("utf-8"))
print(response.content.decode("utf-8"))
print(j["data"][0]["v"])

# post_data = {"email": "18250183809", "password": "wqf007wqf"}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36"}
# cookieStr = "Cookie: anonymid=ka9x42ua-xav2u4; depovince=GW; _r01_=1; ick_login=a52be4db-57ba-4ee8-b20b-f03792e13741; taihe_bi_sdk_uid=abf4f5bfae0ed4ae27d832c85ab48bc5; taihe_bi_sdk_session=ecd7e8c0d0ef5e36ec26a7a2c6c39af7; ick=8615a26b-c8dc-446c-bc6e-b0540babae36; XNESSESSIONID=41d525f0a56e; jebe_key=03eb9e82-ce6c-49b6-94ab-b3de15f977d9%7C18295868e30dc41fe1f59d2c16ce2606%7C1589651091285%7C1%7C1589651092999; wp_fold=0; first_login_flag=1; ln_uact=18250183809; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=fd48ad5b-87a3-429a-8792-4530c94daec7|||||; _de=676DFD3F3812BEC5ABFE433B38007F56; p=055f31f8290c185be11763271b6bd1360; t=0831c5b1f22748c5b7b19cbcf9601f210; societyguester=0831c5b1f22748c5b7b19cbcf9601f210; id=974451710; xnsid=e162ac48; ver=7.0; loginfrom=null"
# cookies = {i.split("=")[0]: i.split("=")[1] for i in cookieStr.split(";")}

#session = requests.session()
#session.post("http://www.renren.com/PLogin.do", headers=headers, data=post_data)
#response = session.get("http://www.renren.com/974451710/profile")
# response = requests.get("http://www.renren.com/974451710/profile", headers = headers, cookies=cookies)
# print(response.content.decode())
# print(requests.utils.dict_from_cookiejar(response.cookies))
# #utl编码对应解码unquote
#
# requests.utils.quote("http://tieba.baidu.com?kw=李毅")
# with open("baidulogo.png", "wb") as f:
#     f.write(requests.get("http://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png").content)