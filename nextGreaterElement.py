def nextGreaterElement(nums1,nums2):
    result = []
    index = {x: i for i, x in enumerate (nums2)}
    for x in nums1:
        indx = index[x]
        for y in nums2[indx +1:]:
            if y > x:
                result.append(y)
                break
        else:
            result.append(-1)
    return result

