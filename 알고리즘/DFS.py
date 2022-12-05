# DFS( 깊이 우선 탐색 Depth First Search ) 메소드 정의
# 스택 구조를 사용
# 시간 복잡도 O(N), N은 데이터 갯수
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된정보를 리스트 자료형으로 표현 ( 2차원 리스트 )
graph = [
    [], # 노드 번호가 1번부터이기 때문에 0번 비움
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * len(graph)

dfs(graph, 1, visited)