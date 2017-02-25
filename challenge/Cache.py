import numpy as np

class Cache:
    
    def __init__(self, id_, size_):
        self.id = id_
        self.size = size_
        self.reward_map = {}
        self.endpoint_list = []

        
    def getID(self):
        return self.id
    def getSize(self):
        return self.size
        
    def getRewardMap(self):
        return self.reward_map
        
    def addToRewardMap(self, video_id, reward):
        self.reward_map[video_id] = reward
        
    def addEndpointList(self,endpoint_id):
        self.endpoint_list.append(endpoint_id)
        
    def getEndpointList(self):
        return self.endpoint_list
        
    def removeElementinRewardMap(self,key):
        del self.reward_map[key]