graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

#깊이 우선 탐색
def dfs(graph, start, visited = set()):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

#너비 우선 탐색
import collections as cols
def bfs(graph, start):
    visited = set([start])  #맨 처음에는 start만 방문한 정점
    queue = cols.dequeue([start])   #컬렉션의 덱 객체 생성(큐로 사용)
    while queue:                    #공백이 아닐 때까지
        vertex = queue.popleft()    #큐에서 하나의 정점 vertex를 빼냄
        print(vertex, end='')       #vertex는 방문했음을 출력
        nbr = graph[vertex] - visited   #nbr: 차집합 연산 사용
        for v in nbr:               #v ∈ {인접정점} - {방문정점}
            visited.add(v)          #v는 방문
            queue.append(v)         #v를 큐에 삽입


10.4
def find_connected_component(graph):
    visited = set() #이미 방문한 정점 집합
    colorList = []  #부분 그래프별 정점 리스트

    for vtx in graph:   #그래프의 모든 정점들에 대해
        if vtx not in visited:  #방문하지 않은 정점이 있다면
            color = dfs_cc(graph, [], vtx, visited) #새로운 컬러리스트
            colorList.append(color) #컬러리스트 추가

    print("그래프 연결성분 개수 = %d" % len(colorList))
    print(colorList) #정점 리스트를 출력

def dfs_cc()

#10.5
def bfsST(graph, start):
    visited = set([start])
    queue = cols.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v] - visited
        for u in nbr:
            print("(", v, ",", u, ")", end="")
            visited.add(u)
            queue.append(u)

           