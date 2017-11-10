# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:16:35 2017

This Python script converts a corpus into letter-tri-gram (LGT) format.
 
@author: mohammad
"""

#!/usr/bin/python

import codecs
import re

source = codecs.open('data/input/corpus.txt', 'r', 'utf-8')  # open the input
                                                    # corpus from the  path
corpus = source.readlines()  # read the entire corpus at once
for line in corpus:  # loop the corpus line by line
    reg = re.sub(r'[^A-Za-z0-9]', '', line)  # remove all the symbols other
                        # than the 26 English letters a-Z and the 10 digits 0-9
    reg_lwr = reg.lower()  # change all the letters to lower case
    new_str = '#' + reg_lwr + '#'  # add '#' at the head and the tail of the
                                                                # text stream
    tri_gram = [new_str[i:i+3] for i in range(len(new_str)-3+1)] # make the LGT
    print(tri_gram)
