"""
Programmers 86971 전력망을 둘로 나누기완전탐색
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""

import sys
from itertools import permutations
input = sys.stdin.readline

from collections import deque

def solution(n, wires):
    answer = 100000
    graph = [[] for _ in range(n+1)]

    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for node1, node2 in wires:
        visited = [False for _ in range(n + 1)]
        q = deque()
        q.append(node1)
        result = 1
        visited[node1] = True
        visited[node2] = True

        while q:
            node = q.popleft()
            for ele in graph[node]:
                if not visited[ele]:
                    result += 1
                    visited[ele] = True
                    q.append(ele)

        min_value = min(result, n-result)
        max_value = n - min_value
        if answer > max_value - min_value:
            answer = max_value - min_value

    return answer