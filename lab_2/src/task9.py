from collections import defaultdict


def delNodeWithChildren(tree, x):
    if x not in tree:
        return tree
    if tree[x][0] is not None:
        delNodeWithChildren(tree, tree[x][0])
    if tree[x][1] is not None:
        delNodeWithChildren(tree, tree[x][1])
    del tree[x]
    return tree


def delSubTree(n, rel, m, nodes):
    tree = defaultdict(list)
    for i in range(n):
        k, l, r = rel[i]
        tree[k] = [
            None if l == 0 else rel[l - 1][0],
            None if r == 0 else rel[r - 1][0]
        ]
    res = []
    for node in nodes:
        delNodeWithChildren(tree, node)
        res.append(len(tree))
    return res


if __name__ == "__main__":
    n = 6
    rel = [[-2, 0, 2], [8, 4, 3], [9, 0, 0], [3, 6, 5], [6, 0, 0], [0, 0, 0]]
    m = 4
    nodes = [6, 9, 7, 8]
    print(delSubTree(n, rel, m, nodes))

