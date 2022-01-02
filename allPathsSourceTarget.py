from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph):
        paths = []
        if not graph or len(graph) == 0:
            return paths
        end_node = len(graph) - 1
        queue = deque([[0]])
        while queue:
            cur_path = queue.popleft()
            print(cur_path)
			
            cur_node = cur_path[-1]
			
            if cur_node == end_node:
                paths.append(cur_path)
                continue
            for nghbor in graph[cur_node]:
				# join each neighbor into the current_path and add it to the queue
                queue.append([*cur_path, nghbor])
        return paths
s=Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))