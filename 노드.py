from collections import deque
# GG = [[],[4,3],[3,5],[1,2],[1,6],[2],[4]]

def bfs(GG,S,G): #GG간선,S시작점,G끝점,V노드개수
    queue = deque([S])
    visited[S] = 1
    while queue:
        # v =q.pop(0)
        v =queue.popleft()
        # print(v,visited[v])
        for w in GG[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1 #거리를 담아줌
                if w == G:
                    return visited[w]
    return 0
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #V개의 노드 개수 E개의 간선
    GG = [[] for _ in range(V+1)]
    for i in range(E):
        p1, p2 =map(int,input().split())   #그래프를 나타내는 작업
        GG[p1].append(p2)
        GG[p2].append(p1)
    S, G = list(map(int,input().split())) #확인용
    visited = [0] * (V + 1)

    ans = bfs(GG, S, G)
    if ans == 0:
        ans = 0
    else:
        ans = ans - 1   #간선의 갯수는 거리에서 -1해준 값이므로

    print(f'#{tc} {ans}')



