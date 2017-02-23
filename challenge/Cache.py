import numpy as np

class Cache:
    
    def __init__(self, id_, size_):
        self.id = id_
        self.size = size_
        
    def getID(self):
        return self.id
    def getSize(self):
        return self.size