import  pandas as pd
import  jieba
import jieba.analyse

from gensim import corpora, models
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
def tokenAndCleanUp(ori_list):
    return_list = []
    total_word_list = []
    for  i in range(len(ori_list)):
        ori = ori_list[i]
        seg_list = jieba.cut(ori, cut_all=True)
        seg_list = clearWord(seg_list)
        return_list.append(seg_list)
        total_word_list.extend(seg_list)
    return return_list,total_word_list



def is_Chinese(word):
    for ch in word:
        if ('\u4e00' > ch) or  (ch > '\u9fff'):
            return False
    return True

def clearWord(word_list):
    stop_words =  [line.strip() for line in open('/Users/koko/Documents/data_analytics/finalproject/data/cn_stopwords.txt').readlines() ]
    return [word for word in word_list if (word not in stop_words) and  is_Chinese(word) ]

def choosePerplexity(body_list):
    y = []
    for num_topics in range(1,50):
        dictionary = corpora.Dictionary(body_list)
        # Convert text data to index and count
        corpus = [dictionary.doc2bow(body) for body in body_list]
        corpus_tfidf = models.TfidfModel(corpus)[corpus]

        lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                          alpha=0.01, eta=0.01, minimum_probability=0.001,
                          update_every=1, chunksize=5, passes=1)
        y.append(lda.log_perplexity(corpus))
    x= range(1,50)
    x_major_locator=MultipleLocator(10)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)


    plt.plot(x,y)
    plt.title("Perplexity based on different k value")
    plt.xlabel("k")
    plt.ylabel('Perplexity')
    plt.savefig("/Users/koko/Documents/data_analytics/finalproject/result/Perplexity.png")
    plt.show()



def buildLDA(body_list):
    # build the dictory
    dictionary = corpora.Dictionary(body_list)

    M = len(body_list)
    V = len(dictionary)

    # Convert text data to index and count
    corpus = [dictionary.doc2bow(body) for body in body_list]
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
    num_topics = 5

    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                      alpha=0.01, eta=0.01, minimum_probability=0.001,
                      update_every=1, chunksize=5, passes=1)


     # get all the topic possiblilty of the doc
    doc_topics = lda.get_document_topics(corpus_tfidf)
    num_show_term = 5   # 每个主题显示几个词

    value = lda.log_perplexity(corpus)
    print("ldamodel.log_perplexity(c_test):",value)
    print('8.结果：每个主题的词分布：--')
    for topic_id in range(num_topics):
        print('主题#%d：\t' % topic_id)
        term_distribute_all = lda.get_topic_terms(topicid=topic_id)
        term_distribute = term_distribute_all[:num_show_term]
        term_distribute = np.array(term_distribute)
        term_id = term_distribute[:, 0].astype(np.int)
        print('词：\t',)
        for t in term_id:
            print(dictionary.id2token[t],)
        print('\n概率：\t', term_distribute[:, 1])









if __name__ == '__main__':
    csv_data = pd.read_csv("/Users/koko/Documents/data_analytics/finalproject/data/DXYRumors.csv")
    rumors_list = csv_data["body"]
    clear_body_list,total_word_list = tokenAndCleanUp(rumors_list)
    choosePerplexity(clear_body_list)
    # buildLDA(clear_body_list)
