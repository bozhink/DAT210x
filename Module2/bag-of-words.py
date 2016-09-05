# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'Authman ran faster than Harry because he is an athlete.',
    'Authman and Harry ran faster and faster.'
]

corpus1 = [
    "The enchanted forest beamed with magic once the prince was born.",
    "Jinto's life changed forever when his planet surrendered without firing a single shot."
]

# Bag Of Words
bow = CountVectorizer()
X = bow.fit_transform(corpus) # Sparse Matrix

print bow.get_feature_names()

print X.toarray()
