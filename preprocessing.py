# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:08:45 2020

@author: Hamoon
"""

from functions import replace
from functions import lower_case
from functions import unwanted_char
from functions import mentions_hashtag_url
from functions import repeated_letters
from functions import tokenize
from functions import negation
from functions import stopword
from functions import spellchecker
from functions import unknown_word
from functions import lemmatize
from functions import slang
from functions import remove_emoji
from functions import one_char
from functions import bigrams


def preprocessing(data):

    output=[]
    output1=[]
    for i in range(len(data)):
        tweet = ' ' + data[i] + ' '
        tweet = replace(tweet)
        tweet = lower_case(tweet)
        tweet = unwanted_char(tweet)
        tweet = mentions_hashtag_url(tweet)
        tweet = remove_emoji(tweet)
        tweet = repeated_letters(tweet)
        tweet_tokenized = tokenize(tweet)
        tweet_tokenized = slang(tweet_tokenized)
        tweet_tokenized = negation(tweet_tokenized)
        tweet_tokenized = stopword(tweet_tokenized)
        # tweet_tokenized = spellchecker(tweet_tokenized)
        tweet_tokenized = unknown_word(tweet_tokenized)
        tweet_tokenized = one_char(tweet_tokenized)
        output.append(tweet_tokenized)
  
    output = bigrams(output)
    # output = lemmatize(output)
    return output