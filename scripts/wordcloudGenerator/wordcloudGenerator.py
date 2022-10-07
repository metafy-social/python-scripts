import pandas as pd
import random
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk   
import string
from textblob import TextBlob 
import wordcloud  
from matplotlib import pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer 
from textblob.sentiments import NaiveBayesAnalyzer
from nltk import FreqDist

# list to decide colours of positive & negative words
pos_word_list=[]
neg_word_list=[]

class SimpleGroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

class GroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (wordcloud.get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = wordcloud.get_single_color_func(default_color)

    def get_color_func(self, word):
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

# # function to convert a csv to string format
# def csv2string(file, negative, positive):
#   s1 = "no negative"
#   s2 = "no positive"
#   dataset = pd.read_csv(file)
#   neg = dataset[negative].head(10000)
#   pos = dataset[positive].head(10000)
#   neg_list = neg.tolist()
#   random.shuffle(neg_list)
#   pos_list = pos.tolist()
#   random.shuffle(pos_list)
#   final = neg_list + pos_list
#   random.shuffle(final)
#   review = ' '.join(final).lower()
#   review = review.replace(s2,"")
#   review = review.replace(s1,"")
#   print('review string has been generated... Calling Wordcloud Generator')
#   wordcloud_generator(review)

# function to convert a csv to string format
def csv2string(file, header):
  s1 = "no negative"
  s2 = "no positive"
  dataset = pd.read_csv(file)
  rev = dataset[header].head(10000)
  rev_list = rev.tolist()
  random.shuffle(rev_list)
  review = ' '.join(rev_list).lower()
  review = review.replace(s2,"")
  review = review.replace(s1,"")
  print('review string has been generated... Calling Wordcloud Generator')
  wordcloud_generator(review)

# function to convert a text file to string format
def txt2string(file):
  s1 = "no negative\n"
  s2 = "no positive\n"
  with open(file) as f:
    review = f.read().lower()
  review = review.replace(s2,"")
  review = review.replace(s1,"")
  print('review string has been generated... Calling Wordcloud Generator')
  wordcloud_generator(review)

# function to determine the polarity of a given word
def word_polarity(tokens):
    counter=0
    for word in tokens:
        testimonial = TextBlob(word, analyzer=NaiveBayesAnalyzer())
        p = testimonial.sentiment.p_pos 
        n = testimonial.sentiment.p_neg
        print(p)
        print(n)
        print(counter)
        counter+=1
        print(word)
        print("~~~~~~~~~")
        if p>0.5:
            pos_word_list.append(word)
        elif n>0.5:
            neg_word_list.append(word)

# function that creates the wordcloud based on frequency of words
def calc_freq(tokens, color_function):
    frequency = {}
    for item in tokens:
        frequency[item] = tokens.count(item)
    cloud = wordcloud.WordCloud(color_func=color_function,width=800, height=400)
    cloud.generate_from_frequencies(frequency)
    cloud.to_file("/Users/dakshjain/Desktop/wc.png")
    print("File saved in local system...")
    return cloud.to_array()

def wordcloud_generator(text):
  nltk.download('stopwords')
  nltk.download('wordnet')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('movie_reviews')
  nltk.download('punkt')
  nltk.download('omw-1.4')

  tokenizer = RegexpTokenizer(r'\w+')
  tokens = tokenizer.tokenize(text)
  print("tokens created...")
  
  stop_words = stopwords.words('english')
  filtered_token = []
  for w in tokens:
    if w not in stop_words and len(w)>3:
      filtered_token.append(w)
  print("stop words removed...")

  lemmatizer = WordNetLemmatizer()
  lemmatized_filtered_token = []
  for w in filtered_token:
    if len(w)>3:
      lemmatized_filtered_token.append(lemmatizer.lemmatize(w))

  pos_tagged_token = nltk.pos_tag(lemmatized_filtered_token)
  
  adjective_tokens_0 = []
  for w in pos_tagged_token:
    if w[1] == 'JJ' and len(w[0])>3:
      adjective_tokens_0.append(w[0])
  print("Level 1 Adjective sorting done...")

  x = nltk.pos_tag(adjective_tokens_0)

  adjective_tokens_1 = []
  for w in x:
    if w[1] == 'JJ' and len(w[0])>3:
      adjective_tokens_1.append(w[0])
  print("Level 2 Adjective sorting done...")

  y = nltk.pos_tag(adjective_tokens_1)

  adjective_tokens_2 = []
  for w in y:
    if w[1] == 'JJ' and len(w[0])>3:
      adjective_tokens_2.append(w[0])
  print("Level 3 Adjective sorting done...")

  freq_dist = FreqDist(adjective_tokens_2)
  common_words = freq_dist.most_common(5)
  max_freq_list = []
  for w in common_words:
    max_freq_list.append(w[0])
  print("50 most common words selected for colour sorting... Polarity Finding function called...")

  word_polarity(max_freq_list)

  color_to_words = {
    		'#00ff00': pos_word_list,
    		'red': neg_word_list
	}
  default_color = 'grey'
  print("Colours associated with given words...")

  grouped_color_func = GroupedColorFunc(color_to_words, default_color)
  print("Calling Wordcloud Creator...")
  myimage = calc_freq(adjective_tokens_2,grouped_color_func)
  print("DISPLAYING THE WORDCLOUD !!")
  plt.figure( figsize=(20,10), facecolor='k')
  plt.imshow(myimage)
  plt.axis('off')
  plt.show()


# depending upon your input data call any of the 2 functions.
# For example ---

csv2string('tripadvisor_hotel_reviews.csv', 'Review')
# txt2string('file.txt')
