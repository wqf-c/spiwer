from lxml import etree

test = '''
<div class="c-offset">
    <div class="sitelink_summary c-gap-top-small">
        <a href="http://share.renren.com/" target="_blank" class="">分享</a>
        <p class="m">人人网 校内是一个真实的社交网络,联络你和你周围的朋友。 加入人人网</p>
    </div>
    <div class="sitelink_summary c-gap-top-small sitelink_summary_last">
        <a href="http://zhibo.renren.com/" target="_blank">人人直播</a>
        <p class="m">玩真的，无套路，积聚校花、学霸的高颜值青春校园直播平台</p>
    </div>
    <div class="sitelink_summary c-gap-top-small">
        <a href="http://name.renren.com/" target="_blank" class="">同名同姓</a>
        <p class="m">有多少人与你同名同姓,想知道你姓名的年龄、地区、工作分布吗?想知道和</p>
    </div>
    <div class="sitelink_summary c-gap-top-small sitelink_summary_last">
        <a href="http://zhan.renren.com/" target="_blank">人人小站</a>
        <p class="m">绿茵最炫三人组!内马尔罗比尼奥马塞洛酷炫瞬间 播放 足球 #体育 #</p>
    </div>
    <div class="sitelink_summary c-gap-top-small ">
        <a href="http://page.renren.com/" target="_blank">人人公共主页</a>
        <p class="m">人人公共主页是一个资讯平台,通过人人公共主页可以即时收到你所关注的名</p>
    </div>
    <div class="sitelink_summary c-gap-top-small sitelink_summary_last">
        <a href="http://dev.renren.com/" target="_blank">人人网开放平台</a>
        <p class="m">人人网开放平台(Renren Open Platform)是面向开发</p>
    </div>
</div>
'''

html = etree.HTML(test)
divElem = html.xpath("//div[@class='c-offset']/div")
collec = []
for div in divElem:
    item = {"href": div.xpath("./a/@href")[0], "text": div.xpath("./a/text()")[0]}
    collec.append(item)

print(collec)