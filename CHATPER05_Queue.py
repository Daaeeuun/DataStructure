#선형큐
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
    def peek(self): 
        if not self.isEmpty(): return self.items[-1] #왜 -1이냐? front값 반환
    
#원형큐
MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear  = 0
        self.items = [None] * MAX_QSIZE #항목의 최대 개수만큼 빈 영역을 이미 가지고 있어야함
    
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self): self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
        
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
        
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1] #슬라이싱
        else: 
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)

q = CircularQueue()
for i in range(9): q.enqueue(i)
q.display()
# for i in range(5): q.dequeue()
for i in range(1): q.dequeue()
# q.display()
for i in range(10,14): q.enqueue(i)
q.display()



#5.5 덱의 구현: 원형큐를 상속하여.
class CircularDeque(CircularQueue): #상속   
    def __init__(self):
        super().__init__()  #부모 클래스의 생성자를 호출
    
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):   #새로운 기능: 전단삽입
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front -1
            if self.front<0: self.front = MAX_QSIZE-1
    
    def deleteRear(self):       #새로운 기능: 후단삭제
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear -1
            if self.rear < 0: self.rear = MAX_QSIZE-1
            return item
    
print("5.5실습")
dq = CircularDeque()
for i in range(9):
    if i%2==0: dq.addRear(i)
    else: dq.addFront(i)
dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9, 14): dq.addFront(i)
dq.display()

#5.6: 리스트를 사용한 우선순위 큐 구현
class PriorityQueue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    def size(self): return len(self.items)
    def clear(self): self.items = []
    def enqueue(self, item):
        self.items.append(item)

    def findMaxIndex(self):     #최대 우선순위 항목의 인덱스 반환
        if self.isEmpty(): return None
        else: 
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
            
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
        
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]
        
print("5.6실습")
q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("PQueue:", q.items)
while not q.isEmpty():
    print("MaxPriority = ", q.dequeue())
