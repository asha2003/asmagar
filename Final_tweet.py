# Databricks notebook source
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('https://stoash.blob.core.windows.net/conash/train.csv')


# COMMAND ----------

!pip install --upgrade pip


# COMMAND ----------

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['SentimentText'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
print(corpus)
print(len(corpus))

# COMMAND ----------

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[0:1000, 1].values


# COMMAND ----------

#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Naive Bayes to the Trining set


# Predicting the Test set results
#y_pred = classifier.predict(X)

# Making the Confusion Matrix
#from sklearn.metrics import confusion_matrix
#cm = confusion_matrix(y_test, y_pred)

#print(cm)

# COMMAND ----------

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X, y)

# Predicting the Test set results
y_pred = classifier.predict(X)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, y_pred)
print(cm)




# COMMAND ----------


import pickle
filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# COMMAND ----------

# MAGIC 
# MAGIC %sh
# MAGIC /databricks/python/bin/pip install --upgrade pip
# MAGIC 
# MAGIC # COMMAND ----------
# MAGIC 
# MAGIC # MAGIC %sh
# MAGIC # MAGIC /databricks/python/bin/pip install azure

# COMMAND ----------

# MAGIC %sh
# MAGIC  /databricks/python/bin/pip install azure

# COMMAND ----------

from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

block_blob_service = BlockBlobService(account_name='stoash', account_key='e6MCWKrC7kOfidDxFaaExVaLXyIBovxREilIJKF2bl9Y8utclYhQ7OkTz63+Dnrj2lFoyH6OgTlVUs2xf8yCCQ==')
block_blob_service.create_container('conash')

#Upload the CSV file to Azure cloud
block_blob_service.create_blob_from_path('conash','finalized_model.sav','finalized_model.sav')

# COMMAND ----------


import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as doc
client = cosmos_client.CosmosClient(url_connection='https://ashcosmo.documents.azure.com:443/', auth={'masterKey': '0yhuQL8x5OamRB9s89fK3tWSYQui1xVwMTRn80WX2zuMYAsfsCp4OO9L3FkJGiJWqcB0TULaDSPavdHP2reZXA=='})

# COMMAND ----------
databaselink='dbs/dbt1'

db1 = client.ReadDatabase(databaselink)


# COMMAND ----------
options = {'offerThroughput': 400}


# Create a container
container = client.CreateContainer(db1['_self'],{'id':"abc1"},options)



# COMMAND ----------

for i in range(0,len(y_pred)):
  item1 = client.CreateItem(container['_self'], {'id': str(i+1), 'Output': y_pred[i],})
  
query = {'query': 'SELECT * FROM c'}
options = {}
options['enableCrossPartitionQuery'] = True
#options['maxItemCount'] = 2
result_iterable = client.QueryItems(container['_self'], query, options)
for item in iter(result_iterable):
  print(item['id'],item['Output'])
