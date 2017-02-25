# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:14:29 2017

@author: dom,jantschi,marcel,stef
"""

import numpy as np
from Cache import Cache
from Endpoint import Endpoint
from Video import Video
import sys
import copy

#filename = 'input/kittens.in'
#filename = 'input/me_at_the_zoo.in'
#filename = 'input/trending_today.in'
filename = 'input/videos_worth_spreading.in'

#out_path = 'input/output_kittens.in'
#out_path = 'input/output_me_at_the_zoo.in'
#out_path = 'input/output_trending_today.in'
out_path = 'input/output_videos_worth_spreading.in'

def contains(small, big):
    for i in range(len(big)):
        if big[i] != small:
                break
        else:
            return i, i+1
    return False

def knapsack(items, maxweight):
    # Create an (N+1) by (W+1) 2-d list to contain the running values
    # which are to be filled by the dynamic programming routine.
    #
    # There are N+1 rows because we need to account for the possibility
    # of choosing from 0 up to and including N possible items.
    # There are W+1 columns because we need to account for possible
    # "running capacities" from 0 up to and including the maximum weight W.
    bestvalues = [[0] * (maxweight + 1)
                  for i in range(len(items) + 1)]

    # Enumerate through the items and fill in the best-value table
    for i, (value, weight) in enumerate(items):
        # Increment i, because the first row (0) is the case where no items
        # are chosen, and is already initialized as 0, so we're skipping it
        i += 1
        for capacity in range(maxweight + 1):
            # Handle the case where the weight of the current item is greater
            # than the "running capacity" - we can't add it to the knapsack
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                # Otherwise, we must choose between two possible candidate values:
                # 1) the value of "running capacity" as it stands with the last item
                #    that was computed; if this is larger, then we skip the current item
                # 2) the value of the current item plus the value of a previously computed
                #    set of items, constrained by the amount of capacity that would be left
                #    in the knapsack (running capacity - item's weight)
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value

                # Just take the maximum of the two candidates; by doing this, we are
                # in effect "setting in stone" the best value so far for a particular
                # prefix of the items, and for a particular "prefix" of knapsack capacities
                bestvalues[i][capacity] = max(candidate1, candidate2)

    # Reconstruction
    # Iterate through the values table, and check
    # to see which of the two candidates were chosen. We can do this by simply
    # checking if the value is the same as the value of the previous row. If so, then
    # we say that the item was not included in the knapsack (this is how we arbitrarily
    # break ties) and simply move the pointer to the previous row. Otherwise, we add
    # the item to the reconstruction list and subtract the item's weight from the
    # remaining capacity of the knapsack. Once we reach row 0, we're done
    reconstruction = []
    i = len(items)
    j = maxweight
    while i > 0:
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1

    # Reverse the reconstruction list, so that it is presented
    # in the order that it was given
    reconstruction.reverse()

    # Return the best value, and the reconstruction list
    return reconstruction


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
final_map = {} # key: cache id, list video_ids


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
        cache_id = int(fileContent[it_lat].split(' ')[0])
        latency_tmp = int(fileContent[it_lat].split(' ')[1])
        endpoint_map[it].addCacheEndpointLatency(cache_id, latency_tmp)
        
        
for it in range(int(init_line[3])):
    cache_map[it] = Cache(it, int(init_line[4]))
    
for video_id in range(len(video_map)):
    video = video_map[video_id]
    for endpoint_id in video.getNrRequestMapping():
        num_requests = video.getNrRequestMapping()[endpoint_id]
        for cacheServerID in endpoint_map[endpoint_id].getLatencyMapping():
            cache_map[cacheServerID].addEndpointList(endpoint_id)
            reward = num_requests * (endpoint_map[endpoint_id].getCenterLatency() - endpoint_map[endpoint_id].getLatencyMapping()[cacheServerID] )
            
            if video.getID() in cache_map[cacheServerID].getRewardMap():
                cache_map[cacheServerID].getRewardMap()[video.getID()] += reward
            else:
                cache_map[cacheServerID].addToRewardMap(video.getID(), reward)
                
for server_id in range(len(cache_map)):
    server = cache_map[server_id]
    endpointList = server.getEndpointList()
    endpoint_to_add_map = {}
    video_to_add_list = []
    reward_map_local = copy.deepcopy(server.getRewardMap())
    for video_id in server.getRewardMap():
        video = video_map[video_id]
        endpoints_to_add = []
        for idx in range(len(server.getEndpointList())):
            try:
                index = video.getIsCachedList().index(server.getEndpointList()[idx])            
            except ValueError:
                endpoints_to_add.append(server.getEndpointList()[idx])
                    
        
        if len(endpoints_to_add) == 0:
            del reward_map_local[video_id]
        else:
            endpoint_to_add_map[video_id] = endpoints_to_add
          
    dup_list = []
    videoID_dup_map = {}
    for video_id in reward_map_local:
        video = video_map[video_id]
        reward = reward_map_local[video_id]
        duple = (reward,video.getSize())
        videoID_dup_map[duple] = video_id
        dup_list.append(duple)
        
    new_list = knapsack(dup_list, server.getSize())
   
    for item_idx in range(len(new_list)):
       element = new_list[item_idx]
       video_id_ = videoID_dup_map[element]
       vid = video_map[video_id_]
       endpointlist = endpoint_to_add_map[video_id_]
       vid.extendIsCachedList(endpointlist)
       video_to_add_list.append(video_id_)

    final_map[server_id] =video_to_add_list 
       
       
       


# Output File
###################

fo = open(out_path, "w")

size_final = len(final_map)
fo.write(str(size_final) + "\n")

for it in range(len(final_map)):
    str_tmp = str(it) + " " + str(list(set(final_map[it])))
    str_tmp = str_tmp.replace('[', '')
    str_tmp = str_tmp.replace(']', '')
    str_tmp = str_tmp.replace(',', '')
    
    fo.write(str_tmp + '\n')
fo.close()
   
   
    
                
                
    
        
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
