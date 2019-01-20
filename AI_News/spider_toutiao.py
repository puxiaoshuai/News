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
brower.find_element_by_link_text('热点').click()
brower.implicitly_wait(10)
title_list,images_list,img_tvs_list,tvs_list,times_list,detaisl_urls_list=[],[],[],[],[],[]
# 获取页面新闻标题，详情页面链接，来源，评论，并添加到列表中
def get_info():
    div_ele = brower.find_elements_by_xpath('//div[@class="wcommonFeed"]')[0]
    titles = div_ele.find_elements_by_xpath('.//div[@class="title-box"]/a')
    images = div_ele.find_elements_by_xpath('.//a[@class="img-wrap"]/img')
    img_tv_url=div_ele.find_elements_by_xpath('.//a[@class="lbtn media-avatar"]/img')
    tv_name=div_ele.find_elements_by_xpath('.//a[@class="lbtn source"]')
    time_tv = div_ele.find_elements_by_xpath('.//div[@class="y-left"]/span')
    for title in titles:
        title_list.append(title.text)
        detaisl_urls_list.append(title.get_attribute('href'))
    print(len(title_list))
    for img in images:
        images_list.append(img.get_attribute('src'))
    print(len(images))
    for img in img_tv_url:
        img_tvs_list.append(img.get_attribute('src'))
    print(len(img_tvs_list))
    for tv in tv_name:
        tvs_list.append(tv.text.strip().replace("⋅",""))
    print(len(tvs_list))
    for tm in time_tv:
        times_list.append(tm.text)
    print(len(times_list))
    for index,value in enumerate(title_list):
        news=News()
        news.title=value
        news.img_url=images_list[index]
    print(news)


# 通过下拉进度条一直加载页面
def get_manyinfo():
    #brower.execute_script("window.scrollTo(0,1000);")
    # 让他滚动这么多次
    for i in range(2):
        # 滚动到底部
        print("滚动" + str(i))
        brower.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
    # 滚动完毕之后,进行数据解析.
    get_info()


def main():
    get_manyinfo()


if __name__ == "__main__":
    main()
