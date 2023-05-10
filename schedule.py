from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prerquisiteCount = defaultdict(int)

        postCourse = defaultdict(list)

        for course in prerequisites:
            a,b = course[0],course[1]
            prerquisiteCount[a] +=1
            postCourse[b].append(a)
        queue = deque()
        for course in range(numCourses):
            if prerquisiteCount[course] == 0:
                queue.append(course)
        if not queue:
            return False
        finishedCourse = 0
        while queue:
            course = queue.popleft()
            finishedCourse +=1
            for nextCourse in postCourse[course]:
                prerquisiteCount[nextCourse] -=1
                if prerquisiteCount[nextCourse] == 0:
                    queue.append(nextCourse)
        return finishedCourse == numCourses
        

        
            
        
        
