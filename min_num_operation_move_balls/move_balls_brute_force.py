class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        length = len(boxes)
        min_operations = []

        for index_i in range(length):
            current_operation = 0

            for index_j in range(length):
                if index_i == index_j:
                    continue
                else:
                    if boxes[index_j] == '1':
                        current_operation += abs(index_j-index_i)

            min_operations.append(current_operation)

        return min_operations

