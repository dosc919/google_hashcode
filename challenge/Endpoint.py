import numpy as np

class Endpoint:
    
    def __init__(self, id_, center_latency_):
        self.id = id_
        self.center_latency = center_latency_
        self.latency_mapping = {}
        
    def getID(self):
        return self.id
        
    def getCenterLatency(self):
        return self.center_latency
        
    def getLatencyMapping(self):
        return self.latency_mapping
        
    def addCacheEndpointLatency(self, cache_id_, latency_):
        self.latency_mapping[cache_id_] = latency_