from nltk import word_tokenize
from nltk import bigrams,trigrams,ngrams

sentence = "welcome Philip Antony to the world of programming"

words = word_tokenize(sentence)
print(list(words))
print(list(bigrams(words)))
print(list(trigrams(words)))

print(list(ngrams(words,4)))
print(list(ngrams(words,5)))