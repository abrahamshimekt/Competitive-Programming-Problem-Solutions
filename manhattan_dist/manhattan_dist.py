def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        manhattan_dist_index = {}
        position = (x,y)

        for i in range(len(points)-1,-1,-1):
            if points[i][0] == position[0] or  points[i][1] == position[1]:
                manhattan_dist = abs(points[i][0]-position[0]) + abs(points[i][1]-position[1])
                manhattan_dist_index[manhattan_dist] = i

        min_dist = float('inf')
        for manhdist in manhattan_dist_index:
            if manhdist < min_dist:
                min_dist = manhdist

        for mhd in manhattan_dist_index:
            if mhd == min_dist:
                return manhattan_dist_index[mhd]
                
        return -1