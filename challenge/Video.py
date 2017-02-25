import numpy as np

class Video:
    
    def __init__(self, id_, size_, ):
        self.id = id_
        self.size = size_
        self.nr_request_mapping = {}
        self.isCached_list = []
        
    def getID(self):
        return self.id
        
    def getSize(self):
        return self.size
        
    def getNrRequestMapping(self):
        return self.nr_request_mapping
        
    def addNrRequestToEnpoint(self, endpoint_id_, nr_requests_):
        if(endpoint_id_ in self.nr_request_mapping):
            self.nr_request_mapping[endpoint_id_] = self.nr_request_mapping[endpoint_id_] + nr_requests_
        else:
            self.nr_request_mapping[endpoint_id_] = nr_requests_
    
    def getIsCachedList(self):
        return self.isCached_list
        
    def addIsCachedList(self, endpoint_id):
        self.isCached_list.append(endpoint_id)     
        
    def extendIsCachedList(self, endpoint_list):
        self.isCached_list.extend(endpoint_list)  