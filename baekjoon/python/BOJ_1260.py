# BOJ 1260 DFS와 BFS
from collections import deque
import sys

def DFS(dictionary, start):
    visited = []
    def dfs_recursive(node):
        if node not in visited:
            visited.append(node)
            for neighbor in sorted(dictionary.get(node, [])):
                dfs_recursive(neighbor)
    dfs_recursive(start)
    return visited

def BFS(dictionary, start):
    visited = []
    queue = deque()

    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in dictionary:
                queue.extend(sorted(dictionary[node]))  
    return visited

def main():
    N, M, V = map(int, sys.stdin.readline().split())
    # dict 이용하기
    node_dict = {}

    # 리스트 이용하기
    # node_list = [[]]
    
    for _ in range(M):
        node1, node2 = map(int, sys.stdin.readline().split())
        node_dict.setdefault(node1, []).append(node2)
        node_dict.setdefault(node2, []).append(node1)
        # setdefault(키 값, 값)
        # 키 값이 있다면 키 값 반환, 없다면 두 번째 인자 반환

    # while(M > 0):
    #     node1, node2 = map(int, sys.stdin.readline().split())
    #     if node1 not in node_dict:
    #         node_dict[node1] = [node2]
    #     else:
    #         node_dict[node1].append(node2)
    #     M -= 1
    

    print(*DFS(node_dict, V))
    print(*BFS(node_dict, V))

if __name__== "__main__":
    main()