# -*- coding: utf-8 -*-
"""
Created on Mon May  4 07:55:44 2020

@author: Hamoon
"""


from gensim.models.doc2vec import Doc2Vec, TaggedDocument


def doc2vec_text(preprocessed_data, epochs):
    tagged_data = [TaggedDocument(words=_d, tags=[str(i)]) for i, _d in enumerate(preprocessed_data)]
    
    doc2vec_model = Doc2Vec(vector_size=100,
                    seed=101,
                    window=5,
                    epochs=epochs,
                    min_count=1,
                    dm =0,
                    dbow_words=1)
    doc2vec_model.build_vocab(tagged_data)
    
    #dm defines the training algorithm. If dm=1 means ‘distributed memory’ (PV-DM) and dm =0 means ‘distributed bag of words’ (PV-DBOW).
       
    for epoch in range(epochs):
        print('iteration {0}'.format(epoch))
        doc2vec_model.train(tagged_data,
                    total_examples=doc2vec_model.corpus_count,
                    epochs=doc2vec_model.iter)
        # decrease the learning rate
        # doc2vec_model.alpha -= 0.0002
        # fix the learning rate, no decay
        doc2vec_model.min_alpha = doc2vec_model.alpha
    
    doc2vec_model.save("d2v_{}.model".format(epochs))
    print("Model Saved")    
    return doc2vec_model