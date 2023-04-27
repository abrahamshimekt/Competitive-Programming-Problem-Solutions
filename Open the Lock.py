class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
    
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        queue = deque()

        

        queue.append(("0000",0))

        visited = {"0000"}
       
        while queue:
            currWheel,turns = queue.popleft()
            if currWheel == target:
                return turns

            for index in range(4):
                currWheelList = list(currWheel)
               

                leftWheel = currWheelList.copy()
                rightWheel = currWheelList.copy()

                leftWheel[index] = str((int(leftWheel[index])-1)%10)
                rightWheel[index] = str((int(rightWheel[index])+1)%10)
               

                left = "".join(leftWheel)
                right = "".join(rightWheel)

                if left not in visited and left not in deadends:
                    visited.add(left)
                    queue.append((left,turns+1))

                if right not in visited and right not in deadends:
                    visited.add(right)
                    queue.append((right,turns+1))
        return -1


                
