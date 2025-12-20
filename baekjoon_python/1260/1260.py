'''
https://www.acmicpc.net/problem/1260

<문제>
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

<입력>
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

<출력>
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

<예제 입력 1>
4 5 1
1 2
1 3
1 4
2 4
3 4

<예제 출력 1>
1 2 4 3
1 2 3 4

<예제 입력 2>
5 5 3
5 4
5 2
1 2
3 4
3 1

<예제 출력 2>
3 1 2 5 4
3 1 4 2 5

<예제 입력 3>
1000 1 1000
999 1000

<예졔 출력 3>
1000 999
1000 999
'''

from collections import deque


def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드에 연결된 다른 노드를 재귀 방문(스택)
    for linked_node_num in graph[v]:
        if not visited[linked_node_num]:
            dfs(graph, linked_node_num, visited)


def bfs(graph, start, visited):
    # 시작 원소를 큐에 넣고 방문 처리
    queue = deque([start])
    visited[start] = True

    while queue:
        # 큐에서 원소 하나 뽑고
        v = queue.popleft()
        print(v, end=' ')

        # 뽑은 원소에 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def make_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 그래프 원소 정렬
    for i in range(len(graph)):
        graph[i].sort()

    return graph


if __name__ == "__main__":
    # n: 정점의 개수
    # m: 간선의 개수
    # v: 탐색을 시작할 정점의 번호
    n, m, v = map(int, input().split())

    graph = make_graph(n, m)

    dfs(graph, v, [False] * (n + 1))
    print()
    bfs(graph, v, [False] * (n + 1))
