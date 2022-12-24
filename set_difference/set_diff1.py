num_english = int(input())
english_students = set(input().split())
num_french = int(input())
french_students = set(input().split())
only_english = english_students - french_students
print(len(only_english))