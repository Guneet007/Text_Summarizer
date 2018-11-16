# -*- coding: utf-8 -*-

import nltk

paragraph="The Taj Mahal was built by Emperor Shah Jahan in India in Agra "

words=nltk.word_tokenize(paragraph)
tagged_words=nltk.pos_tag(words)

nammedEnt=nltk.ne_chunk(tagged_words)
nammedEnt.draw()