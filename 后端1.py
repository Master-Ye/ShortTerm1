import string

import jieba
import numpy as np
import requests
from flask import Flask, request, send_file, Response, make_response, jsonify
from flask_cors import cross_origin
from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from PIL import Image
from wordcloud import wordcloud

app = Flask(__name__)

@app.route('/process', methods=['POST'])
@cross_origin()
def process_image():
    # 获取前端传来的图片和字符串
    image = request.files['image']
    text = request.form['text']
    mask = np.array(Image.open(image))
    print(mask)
    word_list = text.split()  # 将字符串按空格分割成单词列表
    word_set = set(word_list)
    print( word_set)
    f = open('data.txt', 'r', encoding="utf-8")
    t = f.read()
    f.close()
    ls = jieba.lcut(t)
    txt = "".join(ls)
    w = wordcloud.WordCloud(font_path='msyh.ttc', width=500, height=400, background_color='white', mask=mask,stopwords=word_set)
    w.generate(txt)
    w.to_file('grwordcloud.png')
    image_produce = w.to_image()

    buffer = BytesIO()
    image_produce.save(buffer, format='JPEG')
    processed_image = buffer.getvalue()

    return processed_image
@app.route('/cloud', methods=['POST'])
@cross_origin()
def cloud():
    # 获取前端传来的图片和字符串

    idd = request.form['id']

    url = "http://localhost:3300/comment?id="+idd+"&type=1&pageSize=50"  # 格式化输出拼接

    response = requests.get(url=url)

    response = response.json()
    print(response)
    response = response['data']['comment']['commentlist']
    print(response)
    with open('temp.txt', 'w', encoding="utf-8") as file:
        for obj in response:
            file.write(obj['rootcommentcontent'] + '\n')
    f = open('temp.txt', 'r', encoding="utf-8")
    t = f.read()
    f.close()

    ls = jieba.lcut(t)
    txt = "".join(ls)
    w = wordcloud.WordCloud(font_path='msyh.ttc', width=700, height=700, background_color='white')
    w.generate(txt)
    w.to_file('grwordcloud.png')
    image_produce = w.to_image()

    buffer = BytesIO()
    image_produce.save(buffer, format='JPEG')
    processed_image = buffer.getvalue()

    return processed_image

if __name__ == '__main__':
    app.run(debug=True)
