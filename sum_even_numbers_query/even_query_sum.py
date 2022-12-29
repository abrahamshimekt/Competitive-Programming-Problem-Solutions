def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    
        evens_place = {}
        sum_of_evens = 0
        answer = []

        # find the place where the even numbers initially found and sum them up

        for index in range(len(nums)):
            if nums[index] % 2 ==0:
                sum_of_evens += nums[index]
                evens_place[index] = nums[index]
        
        for query in queries:

            nums[query[1]] = nums[query[1]] + query[0]

            # in tthe  jth query if an odd number number changed to even 
            # we need to add the even number we get to our even sum
            # and add our new even place

            if query[1] not in evens_place and nums[query[1]]%2 == 0:

                sum_of_evens += nums[query[1]]
                answer.append(sum_of_evens)
                evens_place[query[1]] = nums[query[1]]

            # in jth query if the current query is changed the current even number to
            # another even number we need just add the val to our even sum
            # and update our even place to another value

            elif query[1] in evens_place and nums[query[1]]%2 ==0:

                sum_of_evens += query[0]
                answer.append(sum_of_evens)
                evens_place[query[1]] = nums[query[1]]

            # in the jth query if the current query changed the current even number to odd
            # then we need to decrement the evens sum by the changed even number and
            # delete the even place associated with changed value to odd

            elif query[1] in evens_place and nums[query[1]]%2 !=0:

                sum_of_evens -= evens_place[query[1]]
                answer.append(sum_of_evens)
                del evens_place[query[1]]

            else:
                answer.append(sum_of_evens)

        return answer