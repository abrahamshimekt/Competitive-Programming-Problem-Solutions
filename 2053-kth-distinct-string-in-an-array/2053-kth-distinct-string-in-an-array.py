class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_hashmap = Counter(arr)
        distinict = []
        for string in arr_hashmap:
            if arr_hashmap[string] == 1:
                distinict.append(string)
        return distinict[k-1] if k<= len(distinict) else ""