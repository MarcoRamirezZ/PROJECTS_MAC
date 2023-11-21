import matplotlib
#matplotlib inline
#config InlineBackend.figure_format = 'svg'
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np
import string

from collections import defaultdict

from sklearn.metrics import f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

import joblib
import pickle as pkl
# from yellowbrick.classifier import ConfusionMatrix

#Functions needed for the program
###########################################################
def open_file(filename):
    with open(filename, 'r',encoding="utf8") as f:
        data = f.readlines()
    return data

def show_statistics(data):
    for language, sentences in data.items():
        
        word_list = ' '.join(sentences).split()
        
        number_of_sentences = len(sentences)
        number_of_words = len(word_list)
        number_of_unique_words = len(set(word_list))
        sample_extract = ''.join(sentences[0].split(' ')[:7])
    
        print(f'Language: {language}')
        print('-----------------------')
        print(f'Number of sentences\t:\t {number_of_sentences}')
        print(f'Number of words\t\t:\t {number_of_words}')
        print(f'Number of unique words\t:\t {number_of_unique_words}')
        print(f'Sample extract\t\t:\t {sample_extract}...\n')
        
def text_process(text):
    
    preprocessed_text = text
    preprocessed_text = text.lower().replace('-',' ')
    translation_table = str.maketrans('\n',' ', string.punctuation+string.digits)
    preprocessed_text = preprocessed_text.translate(translation_table)
    
    return preprocessed_text
###########################################################

#Code
###########################################################
#Create the trainig dictionary using files containig sentences of indicated language
data_raw = dict()
data_raw['en'] =  open_file('train_sentences.en')
data_raw['es'] =  open_file('train_sentences.es')
data_raw['fr'] =  open_file('train_sentences.fr')

#pre-process the text, remove casing, digits, carriage returns, hyphens, etc and leave only words 
data_preprocessed = {k: [text_process(sentence) for sentence in v] for k, v in data_raw.items()}

print('ORIGINAL STATISTICS TESTING')
show_statistics(data_raw)
print('PREPROCESSED STATISTICS TESTING:')
show_statistics(data_preprocessed)

#append sentences into one array, and key in another
sentences_train, y_train =[], []
for k, v in data_preprocessed.items():
    for sentence in v:
        sentences_train.append(sentence)
        y_train.append(k)
        
#transform x_train into training vector
vectorizer = CountVectorizer()
x_train = vectorizer.fit_transform(sentences_train)
x_train

#create naive bayes model and train it with the given data
naive_bayes = MultinomialNB()
naive_bayes.fit(x_train,y_train) 


#Second dictionary with validation sentences
data_val = dict()
data_val['en'] = open_file('val_sentences.en')
data_val['es'] = open_file('val_sentences.es')
data_val['fr'] = open_file('val_sentences.fr')

data_val_preprocessed = {k: [text_process(sentence) for sentence in v] for k,v in data_val.items()}

print('ORIGINAL STATISTICS VALIDATION')
show_statistics(data_val)
print('PREPROCESSED STATISTICS VALIDATION:')
show_statistics(data_val_preprocessed)

sentences_val, y_val = [], []
for k,v in data_val_preprocessed.items():
    for sentence in v:
        sentences_val.append(sentence)
        y_val.append(k)

x_val = vectorizer.transform(sentences_val)

predictions = naive_bayes.predict(x_val)
predictions

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_val, predictions, labels=['en','es','fr']))

f1_score(y_val, predictions, average='weighted')