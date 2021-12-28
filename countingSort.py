#https://www.hackerrank.com/challenges/countingsort1/problem
def countingSort(arr):
    farr = [0]*(100)
    for j in arr:
        farr[j] +=1
    return farr
        