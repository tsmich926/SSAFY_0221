# def bfs(s):
#     Q = []
#     visited =  [0] *(N+1)
#     Q.append(s)
#     visited[s] = 1
#     while Q:
#         v = Q.pop(0) #deque 앞에 있는거 뽑아옴
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = visited[v] + 1


def dfs(s):
    st = []
    visited = [False]*(N+1)

    st.append(s)
    visited [s] =True
    while st:
        v =st.pop(-1) #뒤에 있는 얘뽑아옴
        print(v)
        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] == True

# 연습문제3
N = 7
s= '1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7'
# G = [[],[2,3],[1,4,5]... ]
lst = list(map(int,s.split(',')))
G = [[] for _ in range(N+1)]
for idx in range(0,len(lst),2):
    p1 = lst[idx]
    p2 = lst[idx+1]
    G[p1].append(p2)
    G[p2].append(p1)
print(G)
dfs(1)

#
# 1 /2 3/ 4 5 7/6 7



# def bfs(s):
#     q = []
#     visited = [0]*(N+1)
#
#     q.append(s)
#     visited [s] =1
#     while q:
#         v =q.pop(0)
#         print(v,visited[v])
#         for w in G[v]:
#             if not visited[w]:
#                 q.append(w)
#                 visited[w] == visited[v] + 1