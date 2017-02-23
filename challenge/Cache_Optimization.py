# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:14:29 2017

@author: dom,jantschi,marcel,stef
"""

import numpy as np
from Cache import Cache
from Endpoint import Endpoint
from Video import Video

filename = 'input/me_at_the_zoo.in'

with open(filename, mode='r') as file: # b is important -> binary
    fileContent = file.readlines()
file.close()

init_line = fileContent[0].split(' ')
video_size_line = fileContent[1].split(' ')
first_endpoint_line = fileContent[2].split(' ')
start_endpoint_line = list()

for it in range(int(init_line[1])):
    if it == 0:
        start_endpoint_line.append(2)
    else:
        last_entry = start_endpoint_line[len(start_endpoint_line) - 1]     
        cnt_next = int(fileContent[last_entry].split(' ')[1])
        start_endpoint_line.append((last_entry + cnt_next + 1))

video_map = {}
endpoint_map = {}
cache_map = {}

for it in range(int(init_line[0])):
    video_map[it] = Video(it, int(video_size_line[it]))

for it in range(int(init_line[1])):
    nr_lat = int(fileContent[start_endpoint_line[it]].split(' ')[1])
    endpoint_map[it] = Endpoint(it, int(fileContent[start_endpoint_line[it]].split(' ')[0]))
    for it_lat in range((start_endpoint_line[it] + 1), (start_endpoint_line[it] + nr_lat)):
        cache_id = fileContent[it_lat].split(' ')[1]
        latency_tmp = fileContent[it_lat].split(' ')[0]
        endpoint_map[it].addCacheEndpointLatency(cache_id, latency_tmp)
        
        

for it in range(int(init_line[3])):
    cache_map[it] = Cache(it, 0)
    
    

#nr_cols = int(fileContent[0])
#nr_rows = int(fileContent[2])
#
#fileContent = fileContent.replace("\n", "")
#pizzaContent = fileContent[7:]
#pizzaContent = np.array(list(pizzaContent))
#pizza_matrix = np.reshape(pizzaContent, (nr_cols, nr_rows))
#
#
#print ('write file')
#out_path = 'input/output.in'
#fo = open(out_path, "w")
#
##for ind in range(0,np.size(pizza_matrix,0)):
##    fo.write( str(pizza_matrix[ind,:])+ "\n");
#  # Close file
#fo.write(str(3) + "\n" + str(0) + " " + str(0) + " "+str(2) + " " +
# str(1) + "\n" + str(0) + " " + str(2)+ " " + str(2)+ " " +
# str(2) + "\n" + str(0) + " " +str(3) + " " +str(2) + " "+ str(4))
#fo.close()

print("done")
