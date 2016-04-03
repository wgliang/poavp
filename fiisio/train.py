from library import normal
from library import segmentation
from library import tagger
from library import sentiment
from library import bm25
from library import frequence
from library import merger
from library import model
from library import segger
from library import textrank
from library import tnt
from library import trie

sentiment.train('./library/resource/neg.txt', './library/resource/pos.txt')
sentiment.save('sentiment.marshal')
