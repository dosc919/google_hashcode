# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:14:29 2017

@author: dom,jantschi,marcel,stef
"""

filename_example = 'input/example.in'
filename_small = 'input/small.in'
filename_medium = 'input/medium.in'
filename_big = 'input/big.in'

with open(filename, mode='r') as file: # b is important -> binary
    fileContent = file.read()
file.close()

print(fileContent)




print("done")