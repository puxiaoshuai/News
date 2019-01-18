import requests
import json
max_behot_time = 1547790365
from app_news.models  import NewsTag,News

news_data=[]
def get_one_page(time):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    url = 'https://www.toutiao.com/api/pc/feed/?max_behot_time={}&category=__all__'.format(time)
    print(url)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            text=response.text #为str类型，需要转换成字典
            jsondata=json.loads(text)
            next_page=jsondata['next']['max_behot_time']
            tag=NewsTag()






        else:
            print("状态码错误")
    except:
        print("请求异常")
def parse_news():
    pass
def main():
    get_one_page(max_behot_time)
if __name__ == '__main__':
    main()