# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:03:42 2020

@author: Hamoon
"""

import re
import emoji
from repeat_replacer import RepeatReplacer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer
import pandas as pd
from nltk.corpus import wordnet
import gensim

def replace(tweet):
    tweet = tweet.replace("’", " ")
    tweet = tweet.replace("“", '')
    tweet = tweet.replace("”", '')
    return tweet

def lower_case(tweet):
    """Lower case"""
    tweet = tweet.lower()
    return tweet

def unwanted_char(tweet):
    """Remove unwanted characters"""
    unwanted = ['&amp;', '.', '!', '?', '&', '£', ',', ':', '...', '..','️',
                '$', '(', ')', '*', '+', '=', '-', ' rt ','"', ';',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    unwanted1 = [' st ', ' rd ', ' th ', ' nd ', "'", '\n']
    for letter in unwanted:
        tweet = tweet.replace(letter, '')
    for letter in unwanted1:
        tweet = tweet.replace(letter, ' ')
    tweet = re.sub(r"\S+… ", "", tweet)
    return tweet
    
def mentions_hashtag_url(tweet):
    """Remove mensions and hashtags and URL"""
    
    tweet = re.sub(r"#covid\S+|#covid", "", tweet)
    tweet = re.sub(r"#corona\S+|#corona", "", tweet)                   
    # tweet = re.sub(r"#\S+ ", "", tweet)   
    tweet = re.sub(r"@\S+ ", "", tweet)
    tweet = re.sub(r"http\S+ ", "", tweet)   
    
    return tweet

def repeated_letters(tweet):
    """Remove repeating characters"""
    repeat = RepeatReplacer()
    match = re.findall(r'(\w*)(\w)(\2)(\w*)', tweet)
    if match:
        for ii in range(len(match)):
            a = ''.join(match[ii])
            tweet = re.sub(a, repeat.replace(a), tweet)
    return tweet

def tokenize(tweet):
    """Tokenize"""
    tknzr = TweetTokenizer()
    tweet_tokenized = tknzr.tokenize(tweet)  
    return tweet_tokenized

def negation(tweet_tokenized):
    """Negation to NOT"""
    negation_words= ["n't", "can't", "don't","never",
                     "no", "cannot", "doesn't", "couldn't", "not",
                     "isn't", "wouldn't", "shouldn't"]
    j = 0
    for word in tweet_tokenized:
        if word in negation_words:
            tweet_tokenized[j]='NOT'
        j+=1
    return tweet_tokenized 
      
def stopword(tweet_tokenized):
    """Remove stopwords"""   
    stop_words = stopwords.words('english')
    # stop_words = stop_words + ['NOT', 'pm', 'corona', 'virus', 'get', 'go', 'got']
    tweet_tokenized = [word for word in tweet_tokenized if word not in stop_words]
    return tweet_tokenized


def spellchecker(tweet_tokenized):
    """Correct spelling errors"""
    spell = SpellChecker()
    k = 0
    for word in tweet_tokenized:
        cor_word = spell.correction(word)
        tweet_tokenized[k] = cor_word
        k+=1 
    return tweet_tokenized
    
def unknown_word(tweet_tokenized):
    """Remove the unknown words except hashtags"""
    a=list(tweet_tokenized)
    for word in a:
        if word[0] != '#':
            if not wordnet.synsets(word):
                tweet_tokenized.remove(word)
    return tweet_tokenized

def lemmatize(output_bigram):
    """lemmatization"""
    lemma = WordNetLemmatizer()
    output_lemma = []
    for tweet_tokenized in output_bigram:
        k = 0
        for word in tweet_tokenized:
            lemma_word = lemma.lemmatize(word)
            tweet_tokenized[k] = lemma_word
            k+=1
        output_lemma.append(tweet_tokenized)
    return output_lemma   

def slang(tweet_tokenized):
    """Replace slang with its meaning"""
    m=0
    df_slang = pd.read_excel('slang_dict.xlsx', header=None)
    df_slang_T = df_slang.set_index(0).T
    slang_dict = df_slang_T.to_dict('records')
    for word in tweet_tokenized:
       m+=1
       if word in slang_dict[0]:
           tweet_tokenized.remove(word)
           slang_definition = slang_dict[0][word]
           slang_definition = tokenize(slang_definition)
           tweet_tokenized[m-1:m-1] = slang_definition

    return tweet_tokenized

def remove_emoji(tweet):
    """ remove emojies"""
    tweet = re.sub(emoji.get_emoji_regexp(), r"", tweet)
    return tweet

def one_char(tweet_tokenized):
    """remove tokens with one char"""

    a=list(tweet_tokenized)
    for word in a:
        if len(word) == 1 :
            tweet_tokenized.remove(word)
    return tweet_tokenized

def bigrams(output):
    # Train bigram. higher threshold fewer phrases
    bigram = gensim.models.Phrases(output, min_count=10, threshold=15)
    # Create bigrams
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return [bigram_mod[doc] for doc in output]