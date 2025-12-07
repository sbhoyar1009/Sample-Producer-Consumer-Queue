import time
import random
import threading
from .queue_base import QueueBase
from .message import Message

class Consumer(threading.Thread):
    def __init__(self,name,queue:QueueBase):
        super().__init__()
        self.name = name
        self.queue = queue
        self.running = True
    
    def process_message(self, message: Message):
        print(f"Consumer {self.name} processing message: {message}")
        time.sleep(random.random()*0.3)
    
    def run(self):
        while self.running:
            msg = self.queue.get()
            if msg.payload == 'STOP':
                print(f"[{self.name}] stopping...")
                self.running = False
                break
            self.process_message(msg)
            
