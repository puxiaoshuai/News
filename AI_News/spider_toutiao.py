# coding=utf8
from selenium import webdriver
import time
from AI_News import urls
from app_news.models import NewsTag,News
# 启动webdrive
base_url = 'https://www.toutiao.com'
brower = webdriver.Chrome()
brower.get(base_url)
brower.implicitly_wait(10)
# brower.maximize_window() # 最大化窗口
brower.implicitly_wait(10)
brower.find_element_by_link_text('搞笑').click()
brower.implicitly_wait(10)
news_list=[]
# 获取页面新闻标题，详情页面链接，来源，评论，并添加到列表中
def get_info():
    div_ele = brower.find_elements_by_xpath('//div[@class="wcommonFeed"]')[0]
    li_ele= div_ele.find_elements_by_xpath('.//li')
    new_tag=NewsTag(name='搞笑')
    new_tag.save()
    for li  in  li_ele:
        news =News()
        try:
           title=li.find_elements_by_xpath('.//div[@class="title-box"]/a')[0].text
        except:
            title='这是条广告'

        try:
           img=li.find_elements_by_xpath('.//a[@class="img-wrap"]/img')[0].get_attribute('src')
        except:
           img='https://p1.pstatp.com/list/190x124/pgc-image/5431394cae804ff1a34c7522b7b8d743'
        try:
            img_tv_url=li.find_elements_by_xpath('.//a[@class="lbtn media-avatar"]/img')[0].get_attribute('src')
        except:
            img_tv_url='https://p3.pstatp.com/list/190x124/pgc-image/45bebef78a464ff69770b676473e3644'
        try:
            tv_name=li.find_elements_by_xpath('.//a[@class="lbtn source"]')[0].text
        except:
            tv_name="广告位"
        try:
            time_tv=li.find_elements_by_xpath('.//div[@class="y-left"]/span')[0].text
        except:
            time_tv='暂无时间'
        news.title=title
        news.img_url=img
        news.img_tv_url=img_tv_url
        news.tv_name=tv_name.strip().replace("⋅","")
        news.time_tv=time_tv
        news.newstag=new_tag
        news.body="2018年，在以习近平同志为核心的党中央坚强领导下，各地区各部门认真贯彻落实党中央、国务院各项决策部署，坚持稳中求进工作总基调，坚持新发展理念，坚持推动高质量发展，坚持以供给侧结构性改革为主线，凝心聚力，攻坚克难，经济社会发展的主要预期目标较好完成，三大攻坚战开局良好，供给侧结构性改革深入推进，改革开放力度加大，人民生活持续改善，国民经济运行保持在合理区间，总体平稳、稳中有进态势持续显现，朝着实现全面建成小康社会的目标继续迈进。"
        news.save()
        print(news.title)
        print(news.img_url)
        print(news.tv_name)
        news_list.append(news)


# 通过下拉进度条一直加载页面
def get_manyinfo():
    #brower.execute_script("window.scrollTo(0,1000);")
    # 让他滚动这么多次
    for i in range(10):
        # 滚动到底部
        print("滚动" + str(i))
        brower.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
    # 滚动完毕之后,进行数据解析.
    get_info()


def main():
    get_manyinfo()


if __name__ == "__main__":
    main()
