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
last_tmp = start_endpoint_line[len(start_endpoint_line) - 1]
first_video_request_indx = last_tmp + int(fileContent[last_tmp].split(' ')[1]) + 1

for it in range(first_video_request_indx, len(fileContent)):
    video_tmp, endpoint_tmp, nr_requests_tmp = fileContent[it].split(' ')
    video_map[int(video_tmp)].addNrRequestToEnpoint(int(endpoint_tmp), int(nr_requests_tmp))
    

for it in range(int(init_line[1])):
    nr_lat = int(fileContent[start_endpoint_line[it]].split(' ')[1])
    endpoint_map[it] = Endpoint(it, int(fileContent[start_endpoint_line[it]].split(' ')[0]))
    for it_lat in range((start_endpoint_line[it] + 1), (start_endpoint_line[it] + nr_lat + 1)):
        cache_id = int(fileContent[it_lat].split(' ')[1])
        latency_tmp = int(fileContent[it_lat].split(' ')[0])
        endpoint_map[it].addCacheEndpointLatency(cache_id, latency_tmp)
        
        
for it in range(int(init_line[3])):
    cache_map[it] = Cache(it, int(init_line[4]))
    
print("done")
