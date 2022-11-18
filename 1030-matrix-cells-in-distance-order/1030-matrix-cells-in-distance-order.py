class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        matrix = []
        cell_to_distance = {}
        for i in range(rows):
            for j in range(cols):
                matrix.append([i,j])
        for cell in matrix:
            distance = abs(cell[0]-rCenter) + abs(cell[1]-cCenter)
            cell_to_distance[tuple(cell)] = distance
        
        cell_to_distance = sorted(cell_to_distance.items(),key=lambda x :x[1])
        for k in range(len(cell_to_distance)):
            matrix[k] = tuple(cell_to_distance[k][0])
        return matrix
            
            
                
        