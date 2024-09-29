class Que:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
    
    