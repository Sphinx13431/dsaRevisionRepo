'''
Only valid for directed graphs

scc -> lets say there is an edge from u to v
then you can reach v from u and u from v, so they are in the 
same strongly connected component

reversing the edges in a graph will not alter the scc's
'''

'''
Algorithm
1. Sort all the edges according to their finishing time
2. reverse the graph
3. Do a dfs with reversed graph
'''
from typing import List

class Solution:
    def dfs1(self, graph:List[List[int]], visited:List[bool], stack:List[int], node:int):
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                self.dfs1(graph , visited , stack , i)
        stack.append(node)

    def dfs2(self, graph:List[List[int]], visited:List[bool], node:int):
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                self.dfs2(graph , visited , i)

    def kosaraju(self, n:int, graph:List[List[int]])->int:
        '''
        return the number of scc
        '''

        ## Step1: Do the first dfs, to find the 
        ## finishing time of each node
        visited = [False] * n
        stack = []
        for i in range(n):
            if not visited[i]:
                self.dfs1(graph , visited , stack , i)

        ## step2: reverse the original directed graph
        reversedGraph = [[] for _ in range(n)]

        for u in range(n):
            for v in graph[u]:
                reversedGraph[v].append(u)
        ## step3: Do the second dfs, to find the scc
        visited = [False] * n
        sccCount = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                self.dfs2(reversedGraph , visited , node)
                sccCount += 1
        return sccCount


'''
Time complexity: O(V + E)
space complexity: O(V + E)

'''