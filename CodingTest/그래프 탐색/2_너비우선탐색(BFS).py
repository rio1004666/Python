"""

날짜: 2021/10/08
이름: 강병화
내용: 코딩테스트 - 그래프 탐색

"""

from collections import deque


def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    visited.append(start_node)
    while queue:
        current = queue.popleft()
        for x in graph[current]:
            if not x in visited:
                visited.append(x)
                queue.append(x)

    return visited

graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

result = bfs(graph, 1)

print(result)