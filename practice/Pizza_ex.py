# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:14:29 2017

@author: dom,jantschi,marcel,stef
"""

import numpy as np

filename_example = 'input/example.in'
filename_small = 'input/small.in'
filename_medium = 'input/medium.in'
filename_big = 'input/big.in'

with open(filename_small, mode='r') as file: # b is important -> binary
    fileContent = file.read()
file.close()

nr_cols = int(fileContent[0])
nr_rows = int(fileContent[2])

fileContent = fileContent.replace("\n", "")
pizzaContent = fileContent[7:]
pizzaContent = np.array(list(pizzaContent))
pizza_matrix = np.reshape(pizzaContent, (nr_cols, nr_rows))

print("done")