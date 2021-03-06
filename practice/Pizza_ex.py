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


print ('write file')
out_path = 'input/output.in'
fo = open(out_path, "w")

#for ind in range(0,np.size(pizza_matrix,0)):
#    fo.write( str(pizza_matrix[ind,:])+ "\n");
  # Close file
fo.write(str(3) + "\n" + str(0) + " " + str(0) + " "+str(2) + " " +
 str(1) + "\n" + str(0) + " " + str(2)+ " " + str(2)+ " " +
 str(2) + "\n" + str(0) + " " +str(3) + " " +str(2) + " "+ str(4))
fo.close()

print("done")
