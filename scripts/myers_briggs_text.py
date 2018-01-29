
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB

input_test_train_df = pd.read_csv('data/mb_input_test_train.csv')
print input_test_train_df.head()


def string_to_words(input_df):
  words = []

  for index, row in input_df.iterrows():
    three_pipe_split = row['posts'].split('|||')
    merged_posts_string = ' '.join(three_pipe_split)
    words_split = merged_posts_string.split()
    words.append(words_split)

  return words


def create_working_df(input_df):
  input_df['words'] = string_to_words(input_df)
  working_df = pd.concat([input_df['type'], input_df['words']], axis=1)

  working_df.loc[working_df['type']=='INFJ','type',]=0
  working_df.loc[working_df['type']=='ENTP','type',]=1
  working_df.loc[working_df['type']=='INTP','type',]=2
  working_df.loc[working_df['type']=='INTJ','type',]=3
  working_df.loc[working_df['type']=='ENTJ','type',]=4
  working_df.loc[working_df['type']=='ENFJ','type',]=5
  working_df.loc[working_df['type']=='INFP','type',]=6
  working_df.loc[working_df['type']=='ENFP','type',]=7
  working_df.loc[working_df['type']=='ISFP','type',]=8
  working_df.loc[working_df['type']=='ISTP','type',]=9
  working_df.loc[working_df['type']=='ISFJ','type',]=10
  working_df.loc[working_df['type']=='ISTJ','type',]=11
  working_df.loc[working_df['type']=='ESTP','type',]=12
  working_df.loc[working_df['type']=='ESFP','type',]=13
  working_df.loc[working_df['type']=='ESTJ','type',]=14
  working_df.loc[working_df['type']=='ESFJ','type',]=15

  return working_df

working_df = create_working_df(input_test_train_df.head())
