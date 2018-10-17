#%%
# Load pre-trained word embedding vectors

from gensim.models.keyedvectors import KeyedVectors

wordvectors_path = '/home/fcoclavero/Data/Trained Embeddings/wiki-news-300d-1M-subword.vec'
wordvectors = KeyedVectors.load_word2vec_format(wordvectors_path)


#%%
# Sanity check with simple examples

print(wordvectors["a"].shape)
print(wordvectors.most_similar_cosmul(positive=['king','woman'],negative=['man']))
print(wordvectors.most_similar_cosmul(positive=['playing','sing'],negative=['singing']))
print(wordvectors.most_similar_cosmul(positive=['stalin','germany'],negative=['russia']))


#%%
# Load annotations

import json

annotations = json.load(open('/home/fcoclavero/Data/COCO/annotations_trainval2014/captions_val2014.json', 'r'))


#%%
# De-capitalize

for annotation in annotations['annotations']:
    annotation['caption_clean'] = annotation['caption'].lower()


#%%
# Remove punctuation

punctuation = ".,¡!¿?:;"

for annotation in annotations['annotations']:
    annotation['caption_clean'] = ''.join(filter(lambda s: s not in punctuation, annotation['caption_clean']))


#%%
# Full preprocessing

from text_preprocess.utilities import Preprocess

for annotation in annotations['annotations']:
    annotation['caption_clean'] = Preprocess.full_clean(annotation['caption_clean'])


#%%
# Generate embeddings

import numpy as np

from functools import reduce

zero_vector = np.zeros(shape = wordvectors["a"].shape)

def word_vec_sum(partial, word):
    try:
        return partial + wordvectors[word]
    except: # in case of spelling errors
        return partial


def sentence_word_vec(sentence):
    tokenized = sentence.split(" ")
    return reduce(word_vec_sum, tokenized, zero_vector) / len(tokenized)


for annotation in annotations['annotations']:
    annotation['vector'] = sentence_word_vec(annotation['caption_clean'])


#%%
# TSNE projection

from sklearn.manifold import TSNE

for annotation in annotations['annotations']:
    annotation['tsne'] =  TSNE(n_components=2).fit_transform(np.vstack(annotation["vector"].values))


#%%
print(annotations['annotations'][:10])


#%%
print('hola')