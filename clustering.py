# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:33:57 2020

@author: Hamoon
"""


import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def kmeans_cluster(doc2vec_data, preprocessed_data):
    
    ## Find the best number of clusters
    # number_topics = range(2,41)
    # inertia_list = []
    # sill_list=[]
    # kmn_list=[]
    # for k in number_topics:
    #     kmn = KMeans(n_clusters=k, random_state = 2020, max_iter=100)
    #     kmn.fit(doc2vec_data)
    #     labels = kmn.predict(doc2vec_data)
    #     inertia_list.append(kmn.inertia_)
    #     sill_list.append(silhouette_score(doc2vec_data, labels))
    #     kmn_list.append(kmn)
    #     print('k-means number of topics: ', k)
    # plt.plot(range(1, len(inertia_list)+1), [i/1000 for i in inertia_list], marker= 'o', linestyle='-')
    # plt.ylim(60,75)
    # plt.xlim(0,20)    
    # plt.axvline(6, 0, 90, linestyle='--', c='red')
    # plt.xlabel("Number of topics", fontsize=16)
    # plt.ylabel('Inertia(×1000)', fontsize=16)
    # plt.xticks(np.arange(0, 22, step=2))
    # plt.yticks(np.arange(60, 80, step=5))   
    # plt.figure()
    # plt.plot(range(1, len(sill_list)+1), sill_list, marker= 'o', linestyle='-')
    
    num_topics=8
    kmn = KMeans(n_clusters=num_topics, random_state = 1010, max_iter=100)
    kmn.fit(doc2vec_data)
    labels = kmn.predict(doc2vec_data)

    return labels