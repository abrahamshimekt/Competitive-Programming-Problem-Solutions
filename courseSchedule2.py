class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[0] * numCourses for _ in range(numCourses)]
      
        for prerequisite in prerequisites:
            u, v = prerequisite
            matrix[u][v] = 1
        
        def floydWarshall():
            for k in range(numCourses):
                for i in range(numCourses):
                    for j in range(numCourses):
                        matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

        floydWarshall()
        answer = []
        for q in queries:
            u, v = q
            if matrix[u][v]:
                answer.append(True)
            else:
                answer.append(False)
        return answer
