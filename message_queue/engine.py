from .blocking_queue import BlockingQueue
from .producer import Producer
from .consumer import Consumer
from .message import Message

class Engine:
    def __init__(self, num_producers, num_consumers):
        self.queue = BlockingQueue(maxsize=10)
        self.producers = [
            Producer(f"P{idx}", self.queue, count=5)
            for idx in range(num_producers)
        ]
        self.consumers = [
            Consumer(f"C{idx}", self.queue)
            for idx in range(num_consumers)
        ]

    def start(self):
        for c in self.consumers:
            c.start()
        for p in self.producers:
            p.start()

    def wait(self):
        for p in self.producers:
            p.join()

        for _ in self.consumers:
            self.queue.put(Message("STOP"))

        for c in self.consumers:
            c.join()
