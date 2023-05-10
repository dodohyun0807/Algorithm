import sys

sys.setrecursionlimit(100000)


def solution(n, lighthouse):
    G = [[] for _ in range(n + 1)]
    V = [False for _ in range(n + 1)]

    for road in lighthouse:
        G[road[0]].append(road[1])
        G[road[1]].append(road[0])

    def dfs(node, G, V):
        V[node] = True

        leafs = [i for i in G[node] if not V[i]]

        on, off = 1, 0

        if not leafs:
            return on, off
        else:
            for leaf in leafs:
                cOn, cOff = dfs(leaf, G, V)
                on += min(cOn, cOff)
                off += cOn
            return on, off

    return min(dfs(1, G, V))
