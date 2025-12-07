from .queue_base import QueueBase
from .message import Message
import threading

class BlockingQueue(QueueBase):
    def __init__(self, maxsize=0):
        self._items = []
        self._maxsize = maxsize
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, message: Message):
        with self._not_full:
            while self._maxsize != 0 and len(self._items) >= self._maxsize:
                self._not_full.wait()
            self._items.append(message)
            self._not_empty.notify()

    def get(self) -> Message:
        with self._not_empty:
            while len(self._items) == 0:
                self._not_empty.wait()
            message = self._items.pop(0)
            self._not_full.notify()
            return message

    def qsize(self) -> int:
        with self._lock:
            return len(self._items)

    def isempty(self)-> bool:
        return not (self._maxsize==self.qsize())