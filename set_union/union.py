num_english = int(input()) # number of english students
english_students = set(input().split())
num_french = int(input())  # number of english students
french_students = set(input().split())
english_or_english = english_students.union(french_students)
print(len(english_or_english))