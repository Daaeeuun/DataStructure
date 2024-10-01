# from math import *
A = [1,2,3,4,5]
print('파이썬 리스트 A의 크기는: ', len(A))

A.append(6)
A.append(7)
A.insert(0,0)
print(A)


#----------------------------------------------

items = []

def insert(pos, elem):
    items.insert(pos, elem)

def delete(pos):
    return items.pop(pos)

def getEntry(pos):
    return items[pos]

def isEmpty():
    if len(items) == 0:
        return True
    else: return False

def size(): return len(items)
# def clear(): items = []
def clear(): 
    global items
    items = []
def find(item): return items.index(item)
def replace(pos, elem): items[pos] = elem
def sort(): items.sort()
def merge(lst): items.extend(lst)

def display(msg='ArrayList: '): 
    print(msg, size(), items)

display('파이썬 리스트로 구현한 리스트 테스트')
insert(0, 10)
insert(0, 20)
insert(1, 30)
insert(size(), 40)
insert(2, 50)

display() #20 30 50 10 40

sort()
display('파이썬 리스트로 구현한 List(정렬 후)')

replace(2, 90)
delete(3)
delete(size()-1)
delete(0)
display('파이썬 리스트로 구현한 List(삭제 후)')

lst = [1,2,3]
merge(lst)
display('파이썬 리스트로 구현한 List(병합 후)')

clear()
display('파이썬 리스트로 구현한 List(정리 후)')


#---------------------클래스로 재구현
class ArrayList:
    def __init__(self):
        self.items = []
    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    def delete(self, pos):
        return self.items.pop(pos)
    def isEmpty(self):
        return self.size()==0
    def getEntry(self, pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def find(self, item):
        return self.items.index(item)
    def replace(self, pos, elem):
        self.items[pos] = elem
    def sort(self):
        self.items.sort()
    def merge(self, lst):
        self.items.extend(lst)
    def display(self, msg='ArrayList: '):
        print(msg, self.size(), self.items)

#3.6 집합의 구현
class Set:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def display(self, msg):
        print(msg, self.items)
    def contains(self, item):
        return item in self.items #in아님 반복문으로 구현
    def insert(self, elem):
        if elem not in self.items:  #집합이라 중복이 없어야 삽입가능
            self.items.append(elem)
    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):
        setC = Set()    #결과집합 생성
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def intersect(self, setB):
        setC = Set()
        for elem in setB.item:
            if elem in self.items:
                setC.items.append(elem)
        return setC
    def different(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC

#test
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('setA: ')

setB = Set()
setB.insert('빗')
setB.insert('야구공')
setB.insert('지갑')
setB.display('setB: ')


setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('setA: ')
setB.display('setB: ')