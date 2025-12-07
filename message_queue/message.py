class Message:
    def __init__(self,payload):
        self.payload = payload
    
    def __repr__(self):
        return f"Message ({self.payload})"