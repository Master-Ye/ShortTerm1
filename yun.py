import imageio
import jieba.analyse
import jieba
import numpy as np
import wordcloud


# import pandas as pd
# 载入自定义词典
from PIL import Image

# 载入自定义停止词
mask = np.array(Image.open("ikun1.png"))
print(mask)
f=open('data.txt', 'r', encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt="".join(ls)
w=wordcloud.WordCloud(font_path='msyh.ttc', width=500,height=400, background_color='white')
w.generate(txt)
w.to_file('grwordcloud1.png')
