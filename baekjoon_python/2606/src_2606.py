# 문제 : https://www.acmicpc.net/problem/2606

def dfs(graph, v, visited):  # v: 현재 노드
    # 현재 노드(v)를 방문 처리
    visited[v] = True
    global cnt

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for linked_node_num in graph[v]:
        if not visited[linked_node_num]:  # 아직 방문하지 않은 노드만 방문
            dfs(graph, linked_node_num, visited)
            cnt += 1


def make_rels(edge_cnt):
    rels = [[] for _ in range(edge_cnt)]
    for i in range(edge_cnt):
        rel = list(map(int, input().split(' ')))
        rels[i] = rel

    return rels


def make_graph(node_cnt, rels):
    graph = [[] for _ in range(node_cnt + 1)]

    # 인접 리스트 방식
    for i in range(len(rels) * 2):
        if i < len(rels):
            idx = i

            graph[rels[idx][0]].append(rels[idx][1])
        else:
            idx = abs(len(rels) - i)

            graph[rels[idx][1]].append(rels[idx][0])

    return graph


node_cnt = int(input())
edge_cnt = int(input())

rels = make_rels(edge_cnt)
graph = make_graph(node_cnt, rels)

# node_cnt = 7
# edge_cnt = 6
#
# rels = [
#     [1, 2],
#     [2, 3],
#     [1, 5],
#     [5, 2],
#     [5, 6],
#     [4, 7]
# ]

visited = [False] * (node_cnt + 1)

# 그래프 원소 정렬
for i in range(len(graph)):
    graph[i].sort()

cnt = 0
dfs(graph, 1, visited)
print(cnt)
