# deque
# 스택과 큐의 기능을 모두 가짐
# 출입구가 양쪽에 있다
#각 문자가 요소로 된 리스트형태의 디큐 완성
from collections import deque
# dq = deque('blue')
# print(queue)
# print(dq)
# print(dq.popleft()) #가장 왼쪽 요소 출력 0번
# print(dq.pop()) #가장 오른쪽 요소 출력 -1번
#
# def bfs(G,S,visited):
#     queue = deque([S]) #큐를 만들고
#     visited[S] = True #시작지점 방문처리
#
#     #큐가 완전히 빌때까지 반복
#     while queue:
#         v = queue.popleft() #큐에서 맨 앞의 노드 하나 꺼내기
#         for i in G[v]: # 큐 맨앞에서 꺼낸 노드의 인접 노드를 모두 큐에  넣기
#             if not (visited[i]): #방문 여부 확인
#                 queue.append(i) #큐 삽입
#                 visited[i] = True #방문처리

def bfs(G,S,visited):
    queue = deque([S])
    visited[S] = True
    while queue:
        v = queue.popleft() #큐 순서대로 하나씩 꺼내기
        for i in G[v]: #인접 노드 확인
            if not visited[i]:
                queue.append(i) #큐에 넣어주고
                visited[i] = True #방문처리

G = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

# 노드별로 방문 정보를 리스트로 표현
visited = [False] * 9

# 정의한 BFS 메서드 호출(노드 1을 탐색 시작 노드로 설정)
print(bfs(G, 1, visited))