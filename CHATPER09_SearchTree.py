#9.2 이진탐색트리의 연산
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    #이진탐색트리 탐색연산(순환함수)
    def search_bst(n, key): #n은 루트노드의 값
        if n==None:
            return None
        elif key == n.key:
            return n
        elif key < n.key:
            return search_bst(n.left, key)
        else: 
            return search_bst(n.right, key)       
        
    #이진탐색트리 탐색연산(반복함수) 
    def search_bst_iter(n, key):
        while n != None:
            if key == n.key:
                return n
            elif key < n.key:
                n = n.left
            else:
                n = n.right
        return None
    
    #이진탐색트리 탐색연산(preorder 사용): 값을 이용한 탐색
    def search_value_bst(n, value):
        if n == None: return None
        elif value == n.value:  #값 동일->탐색성공
            return n
        res = search_value_bst(n.left, value)#왼쪽 서브트리에서 탐색
        if res is not None:
            return res
        else:                               #왼쪽 탐색 실패면
            return search_value_bst(n.right, value) #오른쪽 탐색 후 결과반환
        
    def search_max_bst(n):
        while n != None and n.right != None:
            n = n.right
        return n
    def search_min_bst(n):
        while n != None and n.left != None:
            n = n.left
        return n
    
    #삽입연산
    def insert_bst(r, n):
        if n.key < r.key:   #삽입할 노드의 키가 루트보다 작으면
            if r.left is None:  #루트의 왼쪽 자식이 없으면
                r.left = n      #n은 루트의 왼쪽 자식이 됨
                return True
            else:           #루트 왼쪽 자식이 있으면
                return insert_bst(r.left, n)    #왼쪽 자식에게 삽입하도록 함
        elif n.key > r.key: #삽입할 노드의 키가 루트보다 크면
            if r.right is None:  #루트의 왼쪽 자식이 없으면
                r.right = n      #n은 루트의 왼쪽 자식이 됨
                return True
            else:           #루트 왼쪽 자식이 있으면
                return insert_bst(r.right, n)    #왼쪽 자식에게 삽입하도록 함
        else: #키가 중복되면
            return False    #삽입하지 않음
        
    def delete_bst_case1(parent, node, root):
        if parent is None:  #삭제할 단말 노드가 루트이면
            root = None     #공백 트리가 됨
        else: 
            if parent.left == node: #삭제할 노드가 부모의 왼쪽 자식이면
                parent.left = None  #부모의 왼쪽 링크를 None
            else:                   #오른쪽 자식이면
                parent.right = None #부모의 오른쪽 링크를 None
        return root                 #root가 변경될 수도 있으므로 반환
    
    def delete_bst_case2(parent, node, root): #자식이 하나인 노드의 삭제
        if node.left is not None:   #삭제할 노드가 왼쪽 자식만 가짐
            child = node.left       #child는 왼쪽 자식
        else:                       #삭제할 노드가 오른쪽 자식만 가짐
            child = node.right      #child는 오른쪽 자식

        if node == root:            #없애려는 노드가 루트이면
            root =child             #이제 child가 새로운 루트가 됨
        else:
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        return root
    
    def delete_bst_case3(parent, node, root):
        succp = node                #후계자의 부모노드
        succ = node.right           #후계자 노드
        while(succ.left != None):   #후계자와 부모노드 탐색
            succp = succ
            succ = succ.left
        
        if(succp.left == succ):     #후계자가 왼쪽 자식이면
            succp.left = succ.right #후계자의 오른쪽 자식 연결
        else:                       #후계자가 오른쪽 자식이면
            succp.right = succ.right #후계자의 왼쪽 자식 연결
        node.key = succ.key          #후계자의 키와 값을
        node.value = succ.value      #삭제할 노드에 복사      
        node = succ                  #실제로 삭제하는 것은 후계자노드
        
        return root #일관성을 위해 root반환
        
