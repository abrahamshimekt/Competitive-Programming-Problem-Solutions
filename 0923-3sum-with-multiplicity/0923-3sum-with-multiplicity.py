class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
            arr.sort()
            freq= Counter(arr)  
            res, i, l = 0, 0, len(arr)
            while i < l:  
                j, k = i, l-1 
                while j < k:  
                    if arr[i]+arr[j]+arr[k] < target:
                        j += freq[arr[j]]
                    elif arr[i]+arr[j]+arr[k] > target:
                        k -= freq[arr[k]]
                    else:  
                        if arr[i] != arr[j] != arr[k]: 
                            res += freq[arr[i]]*freq[arr[j]]*freq[arr[k]]
                        elif arr[i] == arr[j] != arr[k]:  
                            res += freq[arr[i]]*(freq[arr[i]]-1)*freq[arr[k]]//2 
                        elif arr[i] != arr[j] == arr[k]: 
                            res += freq[arr[i]]*freq[arr[j]]*(freq[arr[j]]-1)//2 
                        else:
                            res += freq[arr[i]]*(freq[arr[i]]-1)*(freq[arr[i]]-2)//6 
                        j += freq[arr[j]]
                        k -= freq[arr[k]]
                i += freq[arr[i]]  
            return res%1000000007