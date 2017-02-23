import numpy as np

class Cache:
    
    def __init__(self, id_, size_):
        self.id = id_
        self.size = size_
        self.reward_map = {}

        
    def getID(self):
        return self.id
    def getSize(self):
        return self.size
        
    def getRewardMap(self):
        return self.reward_map
        
    def addToRewardMap(self, video_id, reward):
        self.nr_request_mapping[video_id] = reward