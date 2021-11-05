"""
날짜: 2021/10/08
이름: 강병화
내용: 코딩테스트 - 그래프 탐색
"""


# 스택을 이용한 DFS


def stack_dfs(graph, start_node):

    visited = []
    stack = []

    stack.append(start_node)
    visited.append(start_node)

    # 스택에 데이터가 없어질때까지 반복
    while stack:
        current = stack[-1]
        last = graph[current][-1]
        for x in graph[current]:     # 현재노드의 인접노드 탐색
            if x not in visited:     # 인접노드가 방문하지 않았으면
                stack.append(x)       # 인접노드 스택에 저장
                visited.append(x)      # 방문스택에 저장
                break
            elif x == last:             # 현재노드의 인접노드가 마지막 노드이면
                stack.pop()
    return visited


def recursive_dfs(graph, node, visited):
    # 현재 노드 방문 처리
    visited.append(node)

    for n in graph[node]:
        if n not in visited:
            recursive_dfs(graph, n, visited)
    return visited
# 그래프 인접 리스트로 구현
graph = [[],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]]

# 깊이 우선 탐색 실행
result = stack_dfs(graph, 1)

print(result)

result2 = recursive_dfs(graph, 1, [])

print(result2)