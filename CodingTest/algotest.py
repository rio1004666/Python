from collections import deque

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


def bfs(graph,root):
    visited = []
    queue = deque([root]) # 첫 루트노드 시작은 바로 데크에 넣는다
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n) # 방문하지 않았다면 방문리스트에 넣는다
            queue += graph[n] - set(visited)
    return visited







print(bfs(graph_list,root_node))