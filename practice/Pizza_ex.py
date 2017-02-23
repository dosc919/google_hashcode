# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:14:29 2017

@author: dom,jantschi,stef
"""

import numpy as np


filename = 'input/small.in'

with open(filename, mode='r') as file: # b is important -> binary
    fileContent = file.read()
file.close()

nr_cols = int(fileContent[0])
nr_rows = int(fileContent[2])

fileContent = fileContent.replace("\n", "")
pizzaContent = fileContent[7:]
pizzaContent = np.array(list(pizzaContent))
pizza_matrix = np.reshape(pizzaContent, (nr_cols, nr_rows))


print ('write file')
out_path = 'input/output.txt'
fo = open(out_path, "w")

for ind in range(0,np.size(pizza_matrix,0)):
    fo.write( str(pizza_matrix[ind,:])+ "\n");
  # Close file
fo.close()

print("done")