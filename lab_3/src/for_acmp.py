from collections import defaultdict


n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, c = map(int, input().split())
    edges.append([u, v, c])
k = int(input())
colors = list(map(int, input().split()))
graph = defaultdict(defaultdict)
for u, v, c in edges:
    graph[u][c] = v
    graph[v][c] = u

cur_v = 1
res = None
for color in colors:
    if color in graph[cur_v].keys():
        cur_v = graph[cur_v][color]
    else:
        res = 'INCORRECT'
        break

if not res: print(cur_v)
else: print(res)
