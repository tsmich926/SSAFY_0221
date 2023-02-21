# def BFS (G,v,n): #그래프G,탐색 시작지점v
#     visited = [0] *(n+1) #정점의 개수
#     queue = []
#     queue .append()


# 연습문제3)
#너비우선탐색으로 경로를 출력
# 7,8
# 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
def BFS(v,N):
    visited = [0]*(N+1) #visited 생성
    q = [v] #큐생성
     #시작점 인큐
    visited[v] = 1 #시작점 인큐표시
    while q:
        t = q.pop(0) #디큐
        print(t,end= ' ') #t에서 처리할 일
        for v in adjL[t] :
            if visited[v]== 0:
                q.append(v) #인큐                                    #t에 인접이고 방문한적 없는 v
                visited[v] = visited[t]+1 #인큐되었음을 표시
    print()
    print(visited)
    v,E = map(int,input().split())#정점,엣지
    arr = list(map(int,input().split()))
    adjL = [[] for _ in range(v+1)]
    for i in range(E):
        n1, n2 = arr[i*2],arr[i*2+1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)
BFS(1,V)