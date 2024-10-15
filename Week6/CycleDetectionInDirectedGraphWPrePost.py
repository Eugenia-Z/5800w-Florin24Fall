
Adj = [[2,3],[4],[5],[3],[4]]
pre = [0] * len(Adj)
post = [0] * len(Adj)
clock = 0

def DFS(v):
    global clock
    clock += 1
    pre[v-1] = clock
    for u in Adj[v-1]:
        if pre[u-1] == 0:  # Meaning not visit yet 
            DFS(u)
    clock += 1
    post[v-1] = clock

DFS(1)
print(pre)
print(post)