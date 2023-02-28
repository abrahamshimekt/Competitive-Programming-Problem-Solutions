n,k,q = map(int,input().split())
recipes = []
max_temp_range = 0
for i in range(n):
    min_temp,max_temp = map(int,input().split())
    recipes.append([min_temp,max_temp ])
    max_temp_range = max(max_temp_range,max_temp)
recipes_list = [0]*(max_temp_range+2)

for recipe in recipes:
    min_temp,max_temp = recipe
    recipes_list[min_temp] +=1
    recipes_list[max_temp+1] -=1

for index in range(1,max_temp_range+2):
    recipes_list[index] += recipes_list[index-1]


for indxx in range(max_temp+2):
    if recipes_list[indxx] <k:
        recipes_list[indxx] = 0
    else:
        recipes_list[indxx] =1


for index in range(1,max_temp+2):
    recipes_list[index] += recipes_list[index-1]

for j in range(q):
    min_temp_q,max_temp_q = map(int,input().split())
    if min_temp_q > max_temp_range:
       print(0)
    elif max_temp_q > max_temp_range:
        print(recipes_list[max_temp_range]-recipes_list[min_temp_q-1])
    else:
        print(recipes_list[max_temp_q]-recipes_list[min_temp_q-1])




