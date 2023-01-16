 def countDistinctIntegers(self, nums: List[int]) -> int:
        distnict = set()
        uniques = 0
        for num in nums:
            if num not in distnict:
                distnict.add(num)
                uniques +=1
        for num_ in nums:
            if num_ > 9:
                num_ = str(num_)[::-1]
                if int(num_) not in distnict:
                    distnict.add(int(num_))
                    uniques +=1
        return uniques