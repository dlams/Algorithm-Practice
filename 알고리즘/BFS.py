# BFS( 너비 우선 탐색 Breadth First Search ) 메소드 정의
# 큐 구조를 사용
# 시간 복잡도 O(N), N은 데이터 갯수
# 하지만 일반적으로 DFS보다 실행시간은 빠름
from collections import deque

def bfs(graph, start, visited):
    # queue를 사용하기 위해 deque 객체 생성
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # queue가 빌 때까지 계속 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

bfs(graph, 1, visited)