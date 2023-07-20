import jieba
import requests
import wordcloud

url = "http://localhost:3300/comment?id=624649&type=1&pageSize=50"  # 格式化输出拼接

response = requests.get(url=url)
response=response.json()
print(response)
response=response['data']['comment']['commentlist']

with open('temp.txt', 'w',encoding="utf-8") as file:
    for obj in response:
        file.write(obj['rootcommentcontent'] + '\n')
f=open('temp.txt', 'r', encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt="".join(ls)
w=wordcloud.WordCloud(font_path='msyh.ttc', width=500,height=400, background_color='white')
w.generate(txt)
w.to_file('grwordcloudn.png')