from nltk import pos_tag
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

sentence = "welcome Philip Anony to the world of programming"

words = word_tokenize(sentence)
print(words)
tags = pos_tag(words)
print("POST tags")
print(tags)