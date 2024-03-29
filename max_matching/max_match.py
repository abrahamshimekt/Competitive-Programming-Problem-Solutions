class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # since we only can pair player with low ability and trainer with
        # high training ability it is straight forward if we sort the two 
        # lists and find the pair for each player at most once and count them
        
        players.sort()
        trainers.sort()
        
        p = 0
        t = 0
        n_match = 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                n_match +=1
                p +=1
                t +=1
            else:
                t +=1
        return n_match
            

