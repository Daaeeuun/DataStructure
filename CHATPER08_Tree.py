from CHATPER05_Queue import *

class Tnode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#8.3 이진트리의 연산
#전위순회: VLR
def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)        
        preorder(n.right)

#중위순회: LVR
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

#후위순회: LRV
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

#노드개수 구하기
def count_node(n):
    if n is None:
        return 0
    else: 
        return 1+count_node(n.left) + count_node(n.right)
    
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else: return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft+1
    else:
        return hRight+1
    
#test
d = Tnode('D', None, None)
e = Tnode('E', None, None)
b = Tnode('B', d, e)
f = Tnode('F', None, None)
c = Tnode('C', f, None)
root = Tnode('A', b, c)

print('\n Inorder: ', end=' ')
inorder(root)
print('\n preorder: ', end=' ')
preorder(root)
print('\n post-order: ', end=' ')
postorder(root)
print('\n level-order: ', end=' ')
levelorder(root)
print()

#8.4 이진트리의 응용: 모르스 코드 결정트리
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
    ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
    ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
    ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
    ('8', '---..'), ('9', '----.')
]

def make_morse_tree():
    root = Tnode(None, None, None)
    for tp in table:
        code = tp[1]    #모르스 코드(.- 등)
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = Tnode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = Tnode(None, None, None)
                node = node.right

        node.data = tp[0]   #코드의 알파벳
    return root

def decode(root, code): #결정트리를 이용해 모르스 코드에 대한 문자 찾기
    node = root
    for c in code:
        if c == '.': node = node.left
        elif c== '-': node = node.right
    return node.data

def encode(ch):
    idx = ord(ch)-ord('A')  #리스트에서 해당 문자의 인덱스
    return table[idx][1]    #해당 문자의 모르스 부호 반환

#test

#8.5 최대힙 구현
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size()==0
    def Parent(self, i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def Right(self, i): return self.heap[i*2+1]
    def display(self, msg='힙트리: '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n>self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]    #삭제할 루트를 복사해 둠
            last = self.heap[self.size()]   #마지막 노드
            while(child <= self.size()):    #마지막 노드 이전까지
                #만약 오른쪽 노드가 더 크면 child를 1 증가(기본은 왼쪽 노드)
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child += 1
                if last >= self.heap[child]:    #더 큰 자식이 더 작으면
                    break                       #삽입 위치 찾음, down-heap 종료
                self.heap[parent] = self.heap[child]    #아니면 down-heap 계속
                parent = child              
                child *= 2

            self.heap[parent] = last    #맨 마지막 노드를 parent 위치에 복사
            self.heap.pop(-1)           #맨 마지막 노드 삭제
            return hroot                #저장해둔 루트 반환

print("최대힙 테스트")
if __name__ == "__main__":
    # 최대힙 객체 생성
    max_heap = MaxHeap()

    # 힙에 값 삽입
    test_values = [10, 20, 5, 7, 30, 15]
    print("삽입 과정:")
    for value in test_values:
        print(f"{value} 삽입:")
        max_heap.insert(value)
        max_heap.display()  # 현재 힙 상태 출력

    # 힙에서 최대값 삭제
    print("\n삭제 과정:")
    while not max_heap.isEmpty():
        print(f"삭제된 값: {max_heap.delete()}")
        max_heap.display()  # 삭제 후 힙 상태 출력
