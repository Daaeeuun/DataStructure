#6.2 단순연결리스트 응용: 연결된 스택
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self): #생성자
        self.top = None #top생성 및 초기화

    def isEmpty(self): return self.top == None
    def clear(self): self.top = None #스택 초기화

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.top.data
        
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count+=1
        return count
    
    def display(self, msg='LinkedStack'):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

odd = LinkedStack()
even = LinkedStack()

#6.3 단순연결리스트 응용: 연결된 리스트
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count+=1
        return count
    def display(self, msg='LinkedList: '):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()  

    def getNode(self, pos):     #pos번째 노드 반환
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None: 
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):    #pos번째 노드의 데이터 반환
        node = self.getNode(pos)
        if node == None : return Node #찾는 데이터가 없는 경우
        else: return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem

    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data: return node
            node = node.link
        return node
    
    def insert(self, pos, elem):
        before = self.getNode(pos-1) #befor노드를 찾음
        if before == None:  #before노드가 없는 맨 앞에 삽입
            self.head = Node(elem, self.head)
        else: 
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

print("6.5")
a = LinkedList()
a.display()
a.insert(0,5)
a.insert(1,7)
a.insert(0,4)
a.display()
a.replace(2,90)
a.display()
a.delete(2)
a.delete(a.size()-1)
a.display()
a.clear()
a.display()

#6.4 원형연결리스트의 응용: 연결된 큐
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
        else: return None
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node