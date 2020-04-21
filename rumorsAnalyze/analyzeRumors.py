import pandas as pd
import  jieba
import jieba.analyse
import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import random
from translation import baidu
from googletrans import Translator



def getKeyWordsList(rumors):
    translator = Translator()
    jieba.analyse.set_stop_words('data/cn_stopwords.txt')
    tags = jieba.analyse.extract_tags(rumors, topK=100, withWeight=True, allowPOS=())
    keywords_rumors_list = []
    keywords_rumors_list_en = []
    filter_word = ["人会","越厚","有个","新冠","病毒","灯能"]
    for v, n in tags:
        if v in filter_word:
            continue
        print(v,":",n)
        eng_v = translator.translate(v).text

        keywords_rumors_list.extend([v] * int(n*100))
        keywords_rumors_list_en.extend([eng_v] * int(n * 100))
    random.shuffle(keywords_rumors_list)
    random.shuffle(keywords_rumors_list_en)
    keywords_rumors = " ".join(keywords_rumors_list)
    keywords_rumors_en = " ".join(keywords_rumors_list_en)
    return keywords_rumors,keywords_rumors_en



def generateWordCloud(keywordsstr,dist,img= None):
    # mask_pic = Image.open("")
    # mask_pic_array = np.array(mask_pic)
    font = "/System/Library/fonts/PingFang.ttc"
    wc = WordCloud(font_path = font,
                   background_color="white",
                   # mask = mask_pic_array,
                   contour_width=5,
                   contour_color="lightblue",
                   )


    wc.generate(keywordsstr)
    wc.to_file(dist)
if __name__ == '__main__':
    # read csv
    csv_data = pd.read_csv("./data/DXYRumors.csv")
    rumors_list = csv_data["title"]
    # get all the rumors
    rumors = " ".join(rumors_list)
    #remove all the  numbers
    rumors = re.sub(u'\d', '', rumors)
    #get the keyword list string
    keywords_rumors,keywords_rumors_en =   getKeyWordsList(rumors)
    # generateWordCloud(keywords_rumors,"keywords.png")
    generateWordCloud(keywords_rumors_en, "keywords_en.png")






