class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        length = len(boxes)
        min_operations = []

        ones_positions = {}
        for index in range(length):
            if boxes[index] == '1':
                ones_positions[index] = '1'
        

        for index_i in range(length):
            current_operation = 0
            
            for ones_position in ones_positions:
                current_operation += abs(ones_position-index_i)

            min_operations.append(current_operation)

        return min_operations