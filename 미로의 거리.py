def bfs(srow,scol):
    q = []
    visited = [[0]*(N) for _ in range(N)]

    q.append((srow,scol))
    visited[srow][scol] = 0
    while q:
        (vrow,vcol) = q.pop(0) #원래는 (vrow,vcol)인데 튜플로 들어옴
        # for d in range(4):
        #     newr = vrow +dr[d]
        #     newc = vcol +dc[d]
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newr = vrow +dr
            newc = vcol +dc

            if 0<=newr<N and 0<=newc<N: #좌표가 유효한지
                if arr[newr][newc] == 3: #목표에 도달
                    return visited[vrow][vcol]
                if arr[newr][newc] == 0 and visited[newr][newc]==0:
                    q.append((newr,newc))
                    visited[newr][newc] = visited[vrow][vcol] + 1
    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    for row in range(N):  #3과 2의 위치 찾기
        for col in range(N):
            if arr[row][col] == 2:
                row1, col1 = row, col

    ans = bfs(row1,col1)
    print(f'#{tc} {ans}')


