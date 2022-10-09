class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_heights = {}
        for i in range(len(names)):
            names_heights[heights[i]] = names[i]
        sorted_ = dict(sorted(names_heights.items(),reverse = True))
        output = []
        for height in sorted_:
            output.append(sorted_[height])
        return output
        