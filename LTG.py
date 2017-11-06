# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:16:35 2017

@author: mohammad
"""

#!/usr/bin/python

import re

str = "Tom Cruise's movies."

reg = re.sub(r'[^A-Za-z0-9]', '', str)

reg_lwr = reg.lower()

new_str = '#' + reg_lwr + '#'

tri_gram = [new_str[i:i+3] for i in range(len(new_str)-3+1)]

print (tri_gram)
