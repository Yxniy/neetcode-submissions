from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 1. Initialize adjacency list and indegrees
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        completed = 0
        # 2. Build the graph and calculate indegrees
        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)
            

        # 3. Initialize queue with courses that have 0 indegree
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # TODO

        # 4. BFS
        while queue:
            course = queue.popleft()
            completed +=1
            for nei in graph[course]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
            # TODO: Update indegrees of neighboring courses
            # TODO: Enqueue courses when indegree becomes 0

        # 5. Check if all courses can be completed
        # TODO
        return completed == numCourses