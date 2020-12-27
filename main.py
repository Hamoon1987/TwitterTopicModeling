# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:40:12 2020

@author: Hamoon
"""
if __name__ == "__main__":
    
    """Load raw data"""
        # Turn on Apache and MySQL
        # Install pymysql
    from load_data import load_data
    data = load_data()
      
    ##Export raw data
    # import csv
    # filename='data.csv'
    # with open(filename, 'w', newline='', encoding = 'utf-8') as file_object:
    #     a = csv.writer(file_object, dialect='excel')
    #     for i in data:
    #         a.writerow([i])

    ##Load exported raw data
    # import pandas as pd
    # dataset_ = pd.read_table("data.csv", header=None)
    # dataset_ = dataset_[0] 
    
    """Preprocessing"""
        # Libraries which should be installed:
        # conda install -c conda-forge emoji
        # nltk.download('wordnet')
        # nltk.download('stopwprds')
        # conda install -c cogsci pyspellchecker
        # conda install -c anaconda gensim
    
    from preprocessing import preprocessing
    preprocessed_data = preprocessing(data)
    
    ##Export preprocessed data
    # import csv
    # filename='preprocessed_data.csv'
    # with open(filename, 'w', newline='', encoding = 'utf-8') as file_object:
    #     a = csv.writer(file_object, dialect='excel')
    #     a.writerows(preprocessed_data)
 
    ##Load exported preprocessed data
    # import pandas as pd
    # dataset = pd.read_table("preprocessed_data.csv", header=None, skip_blank_lines=False)
    # dataset = dataset[0]
    # for itr, i in enumerate(dataset):
    #     if pd.isnull(i):
    #         del dataset_[itr]
    #         del dataset[itr]   
    # data = list(dataset_)               
    # dataset = dataset.str.split(',|\s', expand=True)
    # dataset = list(dataset.values)
    # #Remove none from list
    # preprocessed_data = []
    # for i in range(len(dataset)):
    #     dataset_row = [j for j in dataset[i] if j]
    #     preprocessed_data.append(dataset_row)
            
    """Remove new stopwords after studying the results"""   
    stop_words = ['NOT', 'pm', 
                  'corona', 'virus',
                  'get', 'go', 'got',
                  'corona_virus', 'going', 'one', 'still',
                  'far', 'like', 'thing', 'way', 'put',
                  ]
    preprocessed_data = [[word for word in tweet if word not in stop_words] for tweet in preprocessed_data]

    """Doc2vec word embedding"""
    #nltk.download('punkt')
    import numpy as np
    from doc2vec import doc2vec_text
    epochs = 10
    doc2vec_model = doc2vec_text(preprocessed_data, epochs = epochs)
    doc2vec_data = np.array([doc2vec_model.docvecs[i] for i in range(len(preprocessed_data))])
   
    ##Loading the doc2vec model
    # from gensim.models.doc2vec import Doc2Vec
    # doc2vec_model = Doc2Vec.load('d2v_{}.model'.format(epochs))
    #doc2vec_data = np.array([doc2vec_model.docvecs[i] for i in range(len(preprocessed_data))])
    
    ##Export embedded data
    # import pandas as pd
    # df = pd.DataFrame(doc2vec_data)
    # df.to_csv('doc2vec_data_English.csv', header = False, index = False)
            
    """Clustering"""
    from clustering import kmeans_cluster
    num_topics=7
    labels = kmeans_cluster(doc2vec_data, preprocessed_data)
    
    cluster_pt=[]   
    for r in range(num_topics):
        cluster_pt.append([preprocessed_data[i] for i, e in enumerate(labels) if e==r])
    
    cluster_ba=[]   
    for r in range(num_topics):
        cluster_ba.append([data[i] for i, e in enumerate(labels) if e==r])
   
    """Evaluation"""
    from evaluate import evaluate_tp
    cosine_similarity_list = evaluate_tp(cluster_pt, epochs)
    print(sum(cosine_similarity_list)/len(cosine_similarity_list))
    
    from evaluate import evaluate_tp_2
    cosine_similarity_2 = evaluate_tp_2(cluster_pt,epochs)
    print(1-cosine_similarity_2)
        
    """output"""
    import csv    
    for i in range(num_topics):
        filename='cluster_pr-{}.csv'.format(i)
        with open(filename, 'w', newline='', encoding = 'utf-8') as file_object:
            a = csv.writer(file_object, dialect='excel')
            for uu in cluster_pt[i]:
                a.writerow(uu)

    for i in range(num_topics):
        filename='cluster_ba-{}.csv'.format(i)
        with open(filename, 'w', newline='', encoding = 'utf-8') as file_object:
            a = csv.writer(file_object, dialect='excel')
            for uu in cluster_ba[i]:
                    a.writerow([uu])

      
        