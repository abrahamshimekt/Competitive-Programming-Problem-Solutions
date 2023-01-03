num_questions = int(input())

solved_problems = 0

for question in range(num_questions):

    sure_array = input().split()
    num_ones = 0

    # count the number of ones

    for index in range(3):
        if int(sure_array[index]) == 1:
            num_ones +=1
    # if the number of ones greater than 1 meaning the are sure to solve the problem

    if num_ones >1:
        solved_problems +=1
print(solved_problems)