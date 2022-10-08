## analysing text, to predict whether the rest review is positive or not

#supervised learning..

# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import streamlit as st
#importing dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

#Cleaning the texts .. remove stopwords etc, stemming.. similar words like love or loved
# makes all in small letters
# sparse matrix
#Bag of words basis

#First cleaning is applied to the first record only
import re   #library used in cleaning
review = re.sub('[^a-zA-Z]',' ',dataset['Review'][0]) #.. removing letters other than a to z
review = review.lower()  # at this stage Review is availble in the form of a string
#remove non significant words
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
review = review.split()  # the split finction converts the string into list
review = [word for word in review if not word in set(stopwords.words('english'))]

#Stemming .. replace words which are similar like love and loved to the root word like love
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
ml = []
for word in review:
    st = ps.stem(word)
    ml.append(st)
review = ml

#joining the words to make a string of cleaned words
review = ' '.join(review) # list is converted back to string
    

corpus = []
corpus.append(review) # string is put back into a list (as a combined string)
# print(len(corpus))
##---------------------------------
#Now the above cleaning is applied to all the remaning records from index 1 to 999

for i in range(1,1000):
    review1 = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review1 = review1.lower()
    review1 = review1.split()
    review1 = [word for word in review1 if not word in set(stopwords.words('english'))]
    ml1 = []
    for word in review1:
        st1 = ps.stem(word)
        ml1.append(st1)
        review1 = ml1
    review1 = ' '.join(review1)
    corpus.append(review1)
##-----------------------------------
#  To create a bag of words model
#  it is same as creating a sparse matrix through the process of tokenisation
# ie to create a separate column for each of the word
# so finally what we get is a review, column for each word and its frequency
# The sparse matrix would essentially contain all the required features / feature matrix
#   Once we get the above bag of words, we shud be apply the classification template
# this process is handled through a class called as countvectorizer


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X10 = cv.fit_transform(corpus)
# print(cv.get_feature_names())
X1 = X10.toarray()

y = dataset.iloc[:, 1].values
##-----------------------------------
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
# plt.hist(X_train)
plt.hist(y_train, label='positive (1) and negative (0)')
plt.legend()
plt.show()


# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix: \n', cm)
acc_cm =(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
print('Accuracy of the model based on confusion matrix: ', acc_cm)
acc_score1 = accuracy_score(y_test, y_pred)
print('Accuracy score of the model: ', acc_score1)



#- ------------------------------------------------------------
#classifying the sehensence entered by the user based on the above model

userinput = input("Enter your input :     ")
# userinput = st.text_area("Enter your input :     ")

review2 = re.sub('[^a-zA-Z]',' ',userinput) #.. removing letters other than a to z
review2 = review2.lower()

review2 = review2.split()
review2 = [word for word in review2 if not word in set(stopwords.words('english'))]

ml13 = []
for word in review2:
    st13 = ps.stem(word)
    ml13.append(st13)
    review2 = ml13

#joining the words to make a string of cleaned words
review2 = ' '.join(review2)

import copy
corpus_copy = copy.deepcopy(corpus)
corpus_copy.append(review2)

#It is necessary to put the new record below the existing records so that the new record is also
#arranged in the same manner..

cv = CountVectorizer(max_features = 1500)
X111 = cv.fit_transform(corpus_copy).toarray()

y_pred1 = classifier.predict(X111[-1:][:])
print(y_pred1)

if y_pred1 == 1:
    print("The customer feedback is positive")
else:
    print("The customer feedback is negative")

corpus_copy = []
