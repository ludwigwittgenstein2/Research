#Targeted Sentiment Analysis

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
nltk.download('stopwords')

#Spacy
import spacy
nlp = spacy.load('en')

#Other
import re
import json
import string
import numpy as np
import pandas as pd

#Keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Activation

#load data
import pandas as pd
reviews_train = pd.read_csv("Italy.csv").astype(str)

#reviews_train
reviews_train.head()


print(reviews_train.groupby('Tweet').size().sort_values(ascending=False))

print("number of categories", reviews_train.Tweet.nunique())
