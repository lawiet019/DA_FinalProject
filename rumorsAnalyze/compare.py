import pandas as pd
import  jieba
import jieba.analyse
import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import random
from deep_translator import GoogleTranslator
from collections import defaultdict



def getKeyWordsList(rumors):
    # translator = translator=Translator(from_lang="chinese",to_lang="english")
    jieba.analyse.set_stop_words('../data/cn_stopwords.txt')
    tags = jieba.analyse.extract_tags(rumors, topK=100, withWeight=True, allowPOS=())
    keywords_rumors_list = []
    keywords_rumors_list_en = []
    filter_word = ["人会","越厚","有个","新冠","病毒","灯能","例新冠",".%","年月日","年月日时","万例","该国","累计","达例","日时"]
    result_dict = defaultdict(int)
    for v, n in tags:
        if v in filter_word:
            continue
        else:
            result_dict[v] = n
    return







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


    print("start generating images.....")
    wc.generate(keywordsstr)
    print("start saving images.....")
    wc.to_file(dist)
if __name__ == '__main__':
    # read csv
    csv_data1 = pd.read_csv("../data/DXYNews3.csv")
    news_list1 = csv_data1["summary"]
    # get all the rumors
    news1 = " ".join(news_list1)
    #remove all the  numbers
    news1 = re.sub(u'\d', '', news1)
    #get the keyword list string
    keywords_rumors,keywords_rumors_en =   getKeyWordsList(news1)
