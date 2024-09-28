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