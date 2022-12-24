n = int(input())
for index in range(n):
    num_colors,curr = input().split()
    colors = input()
    colors += colors
    garanted_time = 0
    # fast = 0
    # for slow in range(int(num_colors)):
    #     while colors[fast] != 'g' or slow > fast:
    #         fast +=1
    #     if colors[slow] == curr:
    #         garanted_time  = max(garanted_time,fast-slow)
    # print(garanted_time)
        
    slow = fast = 0
    while slow < int(num_colors):
        if colors[fast] != 'g' or slow > fast:
            fast +=1
        elif colors[slow] != curr:
            slow +=1
        else:
            garanted_time = max(garanted_time,fast-slow)
            slow +=1
    print(garanted_time)
            
    
    


    