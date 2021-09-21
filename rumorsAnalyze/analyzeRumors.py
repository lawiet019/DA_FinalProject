import pandas as pd
import  jieba
import jieba.analyse
import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import random
from translate import Translator




def getKeyWordsList(rumors):
    # translator = translator=Translator(from_lang="chinese",to_lang="english")
    jieba.analyse.set_stop_words('../data/cn_stopwords.txt')
    tags = jieba.analyse.extract_tags(rumors, topK=100, withWeight=True, allowPOS=())
    keywords_rumors_list = []
    keywords_rumors_list_en = []
    filter_word = ["人会","越厚","有个","新冠","病毒","灯能","例新冠",".%","年月日","年月日时","万例","该国","累计","达例","日时"]
    new_dict ={}
    word_list = []
    translator = Translator(from_lang="chinese",to_lang="english")
    for v, n in tags:
        if v in filter_word:
            continue
        if n <=0.03:
            continue

        eng_v = translator.translate(v)
        new_n = round(n,2)
        # print(eng_v," & ",new_n," \\\\")
        new_dict[eng_v] = new_n
        word_list.append(eng_v)

        keywords_rumors_list.extend([v] * int(n*100))
        keywords_rumors_list_en.extend([eng_v] * int(n * 100))
    n = len(word_list)

    k = n //2


    for i in range(12):

        # if i != k:
            print(word_list[i]," & ",new_dict[word_list[i]]," & ", word_list[i+12]," & ",new_dict[word_list[i+12]]," \\\\")
        # else:
        #     print(word_list[i]," & ",new_dict[word_list[i]]," \\\\")

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


    print("start generating images.....")
    wc.generate(keywordsstr)
    print("start saving images.....")
    wc.to_file(dist)
if __name__ == '__main__':
    # read csv
    csv_data = pd.read_csv("../data/DXYNews3.csv")
    rumors_list = csv_data["summary"]
    # get all the rumors
    rumors = " ".join(rumors_list)
    #remove all the  numbers
    rumors = re.sub(u'\d', '', rumors)
    #get the keyword lisxt string
    keywords_rumors,keywords_rumors_en =   getKeyWordsList(rumors)
    # generateWordCloud(keywords_rumors,"keywords.png")
    # generateWordCloud(keywords_rumors_en, "keywords_en4.png")
