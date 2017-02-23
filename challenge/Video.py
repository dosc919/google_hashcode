import numpy as np

class Video:
    
    def __init__(self, id_, size_, ):
        self.id = id_
        self.size = size_
        self.nr_request_mapping = {}
        
    def getID(self):
        return self.id
        
    def getSize(self):
        return self.size
        
    def getNrRequestMapping(self):
        return self.nr_request_mapping
        
    def addNrRequestToEnpoint(self, endpoint_id_, nr_requests_):
        self.nr_request_mapping[endpoint_id_] = nr_requests_