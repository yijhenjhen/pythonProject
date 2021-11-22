import requests
from bs4 import BeautifulSoup
import json
import os

path = "C:\\Users\\TibeMe_user\\Desktop\\Project\\article\\TSLA"
if not os.path.exists(path):
    os.mkdir(path)

userAgent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'

#取得User-Agent資格
headers = {
    #User-Agent固定寫法
    'User-Agent': userAgent
}

# https://seekingalpha.com/symbol/BYND/news?from=2020-06-30&to=2020-12-31
url = 'https://seekingalpha.com/api/v3/symbols/tsla/analysis?cacheBuster=2021-11-22&filter[since]=1593522000&filter[until]=1595011477&id=tsla&include=author%2CprimaryTickers%2CsecondaryTickers%2Csentiments&isMounting=false&page[size]=20&page[number]=1'

ss = requests.session()
res = ss.get(url, headers=headers)

jsonData = json.loads(res.text) # list of article object
#print(jsonData)
article_URL_Dic = {}
for attributes in jsonData['data']:
    article_URL_Dic.setdefault(attributes['attributes']['title'], 'https://seekingalpha.com/api/v3/news/' + (attributes['links']['self'])[10:17])
    # print(attributes['attributes']['title'])
    # print('https://seekingalpha.com/api/v3/news/' + (attributes['links']['self'])[6:13])

print(article_URL_Dic)
for singleAriticle in article_URL_Dic:

    print(singleAriticle) #print title
    singleArtUrl = article_URL_Dic.get(singleAriticle)
    print('==================================================')
    # print(singleArtUrl)  # print URL

    try:
        res = ss.get(singleArtUrl, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        content_html = soup.select('li')
        contentSave = ''
        for i in content_html:
            content = i.text
            contentSave += (content + '\n')
            #print(content)
        #print(contentSave)
        #print('===============================================' + '\n')

        try:
            with open(path + '\\' + '{}.txt'.format(singleAriticle.replace('?', '').replace('/', ' ')), 'w', encoding='utf-8') as f:
                f.write(contentSave)

        except IndexError as e:
            print(e)

        except OSError:
            pass

    except IndexError as e:
        print('wrong')


