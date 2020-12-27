# TwitterTopicModeling
Topic modeling on tweets. Using doc2vec word embedding and k-means clustering to categorize tweets. 

The article is availabe at ***  
The goal of this code is to categorize tweets into main themes. Figure below shows the main steps of the process:  
  
  
<a href="url"><img src="https://github.com/Hamoon1987/TwitterTopicModeling/blob/main/Flowchart.png" align="left" height="300" width="200" ></a>  
1- The dataset is a collection of tweets related to a specific subject. In my case it was tweets related to COVID-19 pandemic. Database should be extracted to MySQL folder of XAMPP software. load_data.py is called in the main.py and loads the tweets.
2- The preprocessing includes converting letters to lower case, removing URL, mentions, stopwords and emojis, correcting repeated characters, tokenizing and replacing negations with NOT. preprocessing.py is called in the main.py and preprocesses the tweets.
3- Document embedding is done using doc2vec algorithm in doc2vec.py
4- Clustering is performed using k-means algorithm in clustering.py
5- Theme extraction is done manually based on most frequent words used in each cluster which is generated in evaluate.py
  
All the following steps are performed by running the main.py file. 
