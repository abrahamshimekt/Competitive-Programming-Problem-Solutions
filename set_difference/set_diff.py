num_english = int(input())
english_students = input().split()
num_french = int(input())
french_students = set(input().split())
only_english = 0
for students in english_students:
    if students not in french_students:
        only_english +=1
print(only_english)