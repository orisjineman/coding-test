# DFS 예제
# 5-8.jpeg 그래프 이미지 참고
def dfs(graph, v, visited):  # v: 현재 노드
    # 현재 노드(v)를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for linked_node_num in graph[v]:
        if not visited[linked_node_num]:
            dfs(graph, linked_node_num, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# 인접 리스트 방식
graph = [
    [],
    [2, 3, 8],  # 1번 노드
    [1, 7],  # 2번 노드
    [1, 4, 5],  # 3번 노드
    [3, 5],  # 4번 노드
    [3, 4],  # 5번 노드
    [7],  # 6번 노드
    [2, 6, 8],  # 7번 노드
    [1, 7]  # 8번 노드
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
