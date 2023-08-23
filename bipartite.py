from collections import defaultdict,deque
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        colors = [-1 for i in range(n)]
        dislikesGraph = defaultdict(list)

        for dislike in dislikes:
            a,b = dislike
            dislikesGraph[a].append(b)
            dislikesGraph[b].append(a)


        def bfs(person):
            queue = deque()
            queue.append(person)
            while queue:
                currPerson = queue.popleft()
                if colors[currPerson-1] == -1:
                    colors[currPerson-1] = 0
                for dislike in dislikesGraph.get(currPerson,[]):
                    if colors[dislike-1] == -1:
                        if colors[currPerson-1] == 0:
                            colors[dislike-1] = 1
                        else:
                            colors[dislike-1] = 0
                        queue.append(dislike)
                    else:
                        if colors[dislike-1] == colors[currPerson-1]:
                            return False
            return True
        
        for person in range(1,n+1):
            if colors[person-1] == -1:
                if not bfs(person):
                    return False
        return True
                







                       
            



