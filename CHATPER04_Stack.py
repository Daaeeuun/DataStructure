class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top)==0
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def size(self): return len(self.top)
    def clear(self): 
        # global top
        self.top = []
    def __str__(self):
        return str(self.top[::-1])

s = Stack()

for i in range(1,6):
    s.push(i)
print('push 5회: ', s.top)
print('pop() --> ', s.pop())
print('pop() --> ', s.pop())
print('pop  2회: ', s.top)
s.push('홍길동')
s.push('이순신')
print('push 2회: ', s.top)




odd = Stack()
even = Stack()

for i in range(10):
    if i%2 == 0 : even.push(i)
    else: odd.push(i)

print(even)
print(odd)
for _ in range(2): even.pop()
print(even)

#4.3 스택의 응용: 괄호검사
def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('): #튜플사용
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else: 
                left = stack.pop()
                if(ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                    (ch == ")" and left != "("):
                    return False

    return stack.isEmpty()

def checkBracketsV2(lines):
    stack2 = Stack()
    for line in lines:
        for ch in line:  # 'statement' 대신 'line' 사용
            if ch in ('{', '[', '('):  # 튜플 사용
                stack2.push(ch)
            elif ch in ('}', ']', ')'):
                if stack2.isEmpty():
                    return False
                else:
                    left = stack2.pop()
                    if (ch == "}" and left != "{") or \
                       (ch == "]" and left != "[") or \
                       (ch == ")" and left != "("):
                        return False

    return stack2.isEmpty()


# 파일에서 코드 읽기 및 괄호 검사
infile = open("CHAPTER03_List.py", "r", encoding='utf-8')  # 인코딩 설정
lines = infile.readlines()
infile.close()

result = checkBracketsV2(lines)
print("CHAPTER03_List.py -->", result)


#4.4 스택의 응용: 수식의 계산
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token == '+':
                s.push(val1+val2)
            elif token == '-':
                s.push(val1-val2)
            elif token == '*':
                s.push(val1*val2)
            elif token == '/':
                s.push(val1/val2)
        else: s.push(float(token))
    return s.pop()

expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr2, '---> ', evalPostfix(expr2))