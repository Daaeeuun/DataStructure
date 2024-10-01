#7.2 선택정렬
def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1)

def printStep(arr, val):
    print("  Step %2d = " %val, end="")
    print(arr)



#삽입정렬
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>=0 and a[j]>key:
            A[j+1] = A[j]   #항목들을 뒤로 한 칸씩 이동
            j -= 1
        A[j+1] = key
        printStep(A, i)       

a = [3, 5, 9, 6, 2, 7, 8]

#버블정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if(A[j]>A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True

        if not bChanged: break #교환이 더이상 없으면 종료
        printStep(A, n-i)

# selection_sort(a)
# insertion_sort(a)     
bubble_sort(a)     

#7.3 정렬응용: 집합 다시보기
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
    
    def insert(self, elem):      #정렬된 상태를 유지하면서 elem 삽입
        if elem not in self.items: return  #중복요소는 삽입x
        for idx in range(len(self.items)):
            if elem < self.items[idx]:
                self.items.insert(idx, elem)
                return
        self.items.append(len)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):  
        newSet = Set()
        a = 0, b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = self.items[b]
            if valueA<valueB:
                newSet.items.append(valueA)
                a += 1
            elif valueA>valueB:
                newSet.items.append(valueB)
                b += 1
            else:   #중복되는 요소
                newSet.items.append(valueA)
                a += 1
                b += 1
            while a<len(self.items):
                newSet.items.append(self.items[a])
                a += 1
            while b < len(self.items):
                newSet.items.append(self.items[b])
                b += 1
            return newSet
            


        
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
    
    def __eq__(self, setB): #두 집합 self, setB가 같은 집합인가?
        if self.size() != setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        return True
    
