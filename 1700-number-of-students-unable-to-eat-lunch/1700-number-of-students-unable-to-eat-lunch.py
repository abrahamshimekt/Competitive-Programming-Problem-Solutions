class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # iterate through both lists and check if the the first student and the type of the sandwicth at the top of the stack is the same if they are the same remove the student from the queue and the sandwith from the stack if not add the student at the end of the queue by from its initial place
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students != []:
            if len(students) ==0:
                return len(students)
            elif sandwiches[0] == students[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                if students == deque([1]* len(students)) and sandwiches[0] !=1:
                    return len(students)
                elif students == deque([0]* len(students)) and sandwiches[0] !=0:
                     return len(students)
                else:
                    temp= students.popleft()
                    students.append(temp)
        return 0
        