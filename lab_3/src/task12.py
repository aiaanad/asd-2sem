from collections import defaultdict


def colorLabyrinth(n, m, edges, k, colors):
    graph = defaultdict(defaultdict)
    for u, v, c in edges:
        if c in graph[u] or c in graph[v]:
            raise ValueError('Не уникальные коридоры')
        graph[u][c] = v
        graph[v][c] = u
    cur_v = 1
    for color in colors:
        if color in graph[cur_v].keys():
            cur_v = graph[cur_v][color]
        else:
            return 'INCORRECT'

    return cur_v


if __name__ == '__main__':
    n, m = 3, 2
    edges = [[1, 2, 10], [1, 3, 5]]
    k = 5
    colors = [10, 10, 10, 10, 5]
    print(colorLabyrinth(n, m, edges, k, colors))