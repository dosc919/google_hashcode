# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:14:29 2017

@author: dom,jantschi,stef
"""

filename = 'input/small.in'

with open(filename, mode='r') as file: # b is important -> binary
    fileContent = file.read()
file.close()

print(fileContent)
print("done")