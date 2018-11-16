# -*- coding: utf-8 -*-

import random

text="""Global warming is a long-term rise in the average temperature of the Earth's climate system, an aspect of climate change shown by temperature measurements and by multiple effects of the warming. The term commonly refers to the mainly human-caused observed warming since pre-industrial times and its projected continuation, though there were also much earlier periods of global warming. In the modern context the terms are commonly used interchangeably, but global warming more specifically relates to worldwide surface temperature increases; while climate change is any regional or global statistically identifiable persistent change in the state of climate which lasts for decades or longer, including warming or cooling. Many of the observed warming changes since the 1950s are unprecedented in the instrumental temperature record, and in historical and paleoclimate proxy records of climate change over thousands to millions of years."""

n=7

ngrams={}

# Create N Grams

for i in range(len(text)-n):
    gram=text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram]=[]
    ngrams[gram].append(text[i+n])
    
#Testing N gram Model

currentGram=text[0:n]
result=currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities=ngrams[currentGram]
    nextItem=possibilities[random.randrange(len(possibilities))]
    result+=nextItem
    currentGram=result[len(result)-n:len(result)]
    
print(result)