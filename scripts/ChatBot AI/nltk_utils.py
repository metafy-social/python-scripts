import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentece, all_words):
    tokenized_sentece = [stem(w) for w in tokenized_sentece]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, w in enumerate(all_words):
        if w in tokenized_sentece:
            bag[index] = 1
    return bag
# a = "How are you?"
# print(a)
# a = tokenize(a)
# print(a)

# words = ["Organize", "organizes", "organizing"]
# stemmed_word = [stem(w) for w in words]
# print(stemmed_word)

# sentence =['hello','how', 'are', 'you']
# words = ['hi','hello','I', 'you','bye', 'thank', 'cool']
# bag = bag_of_words(sentence, words)
# print(bag)
