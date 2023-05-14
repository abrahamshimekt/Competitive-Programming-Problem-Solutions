from collections import defaultdict,deque
class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        countPre = defaultdict(int)
        preCourses = defaultdict(set)
        nextCourses = defaultdict(set)
        for pre in prerequisites:
            countPre[pre[1]] +=1
            preCourses[pre[1]].add(pre[0])
            nextCourses[pre[0]].add(pre[1])
        queue = deque()
        for course in range(numCourses):
            if countPre[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            
            for nxtCourse in list(nextCourses[course]):
                preCurrCourse = preCourses[course]
                preCurrCourse.add(course)
                preCourses[nxtCourse]= preCourses[nxtCourse].union(preCurrCourse)
                countPre[nxtCourse] -=1
                if countPre[nxtCourse] == 0:
                    queue.append(nxtCourse)
        answer = []
        for query in queries:
            a,b = query
            if a in preCourses[b]:
                answer.append(True)
            else:
                answer.append(False)
            
        return answer



