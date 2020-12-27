# -*- coding: utf-8 -*-
"""
Created on Mon May 11 03:47:31 2020

@author: Hamoon
"""

def evaluate_tp(cluster_pt, epochs):
    import numpy as np
    from collections import Counter
    num_topics = len(cluster_pt)
    most_occur=[]
    for r in range(num_topics):
        cluster_words = [item for sublist in cluster_pt[r] for item in sublist]
        counter = Counter(cluster_words)
        most_occur_ = counter.most_common(10)
        most_occur_list = [list(i) for i in most_occur_]
        for i in most_occur_list:
            i[1] = round(i[1]/len(cluster_words), 3)
        most_occur.append(most_occur_list)
    # export most_occur
    import csv
    filename='most_occur.csv'
    with open(filename, 'w', newline='', encoding = 'utf-8') as file_object:
        a = csv.writer(file_object, dialect='excel')
        for ww in most_occur:
            a.writerow([ww])

    
    
    most_occur_words=[]
    for r in range(num_topics):
        a=[]
        for w in range(10):
            a.append(most_occur[r][w][0])
        most_occur_words.append(a)
    
    from gensim.models.doc2vec import Doc2Vec
    doc2vec_model = Doc2Vec.load('d2v_{}.model'.format(epochs))
    wv_list=[]
    for r in range(num_topics):
            wv = [doc2vec_model[i] for i in most_occur_words[r]]
            wv_list.append(wv)
    
    from sklearn.metrics.pairwise import cosine_similarity
    cosine_similarity_list=[]
    for r in range(num_topics):
        cosine_similarity_ = cosine_similarity(wv_list[r])
        lower_sum = np.tril(cosine_similarity_).sum()-np.trace(cosine_similarity_)
        lower_ave = lower_sum/(cosine_similarity_.shape[0]*(cosine_similarity_.shape[0]-1)/2)
        cosine_similarity_list.append(lower_ave)
    return cosine_similarity_list


def evaluate_tp_2(cluster_pt, epochs):
    
    import numpy as np
    from collections import Counter
    num_topics = len(cluster_pt)
    most_occur_words=[]
    for r in range(num_topics):
        cluster_words = [item for sublist in cluster_pt[r] for item in sublist]
        counter = Counter(cluster_words)
        most_occur_ = counter.most_common(10)
        most_occur_words.append([i[0] for i in most_occur_])

    
    from gensim.models.doc2vec import Doc2Vec
    doc2vec_model = Doc2Vec.load('d2v_{}.model'.format(epochs))
    wv_list = [[doc2vec_model[i] for i in r] for r in most_occur_words]
    wv_list_avg = [np.average(i, axis=0) for i in wv_list]

    from sklearn.metrics.pairwise import cosine_similarity

    cosine_similarity_ = cosine_similarity(wv_list_avg)
    lower_sum = np.tril(cosine_similarity_).sum()-np.trace(cosine_similarity_)
    lower_ave = lower_sum/(cosine_similarity_.shape[0]*(cosine_similarity_.shape[0]-1)/2)
    return lower_ave