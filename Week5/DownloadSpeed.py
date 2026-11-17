import sys
from collections import deque

def bfs(cap: list[list[int]], adj: list[list[int]], source: int, sink: int) -> list[int] | None:
    """Finder en korteste sti fra source til sink i residualgrafen.
    Returnerer parent-listen (parent[v] = forrige knude på stien), eller None hvis sink ikke kan nås."""
    n = len(adj)
    parent = [-1] * n
    parent[source] = source
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if parent[v] == -1 and cap[u][v] > 0:
                parent[v] = u
                if v == sink:
                    return parent
                queue.append(v)

    return None

def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    # Kanter som (a, b, c), 0-indekseret: computer a kan sende til b med hastighed c
    edges = []
    idx = 2
    for _ in range(m):
        a, b, c = data[idx] - 1, data[idx + 1] - 1, data[idx + 2]
        edges.append((a, b, c))
        idx += 3

    source, sink = 0, n - 1

    # Residualgraf: kapacitetsmatrix + naboliste (begge retninger, så BFS kan følge baglæns kanter)
    cap = [[0] * n for _ in range(n)]
    adj = [[] for _ in range(n)]
    for a, b, c in edges:
        if cap[a][b] == 0 and cap[b][a] == 0:
            adj[a].append(b)
            adj[b].append(a)
        cap[a][b] += c

if __name__ == "__main__":
    main()