import threading
import queue
import time
import random
from .queue_base import QueueBase
from .message import Message

class Producer(threading.Thread):
    def __init__(self, name,message_queue:QueueBase,count=1):
        super().__init__()
        self.name=name
        self.message_queue = message_queue
        self.count = count
    
    def create_message(self,index)->Message:
        return Message(f"{self.name} message {index}")
    
    def run(self):
        for idx in range(self.count):
            msg = self.create_message(idx)
            print(f"[{self.name}] producing {msg}")
            self.message_queue.put(msg)
            time.sleep(random.random()*0.2)
            print("["+self.name+'] done')