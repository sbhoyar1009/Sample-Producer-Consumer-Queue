from abc import ABC, abstractmethod

class QueueBase(ABC):
    @abstractmethod
    def put(self, item):
        pass
    
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def isempty(self):
        pass
    
    @abstractmethod
    def qsize(self):
        pass