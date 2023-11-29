class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy,available = [],[i for i in range(n)]

        meetings.sort()
        counter = defaultdict(int)
        
        for meeting in meetings:
            start,end = meeting
            
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(available,room)
            if available:
                room = heappop(available)
                heappush(busy,(end,room))
            else:
                finishTime , room = heappop(busy)
                heappush(busy,(finishTime+end-start,room))
            counter[room]+=1
        
        hasMostMeetingRoom = 0
        counts = 0
        
        for room in counter:
            if counter[room] > counts:
                hasMostMeetingRoom = room
                counts = counter[room]
            elif counter[room] == counts and hasMostMeetingRoom > room:
                hasMostMeetingRoom = room
        
        return hasMostMeetingRoom