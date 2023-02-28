T = int(input())
for t in range(T):
    n,k = map(int,input().split())
    sol = list(input())
    left = 0
    right = 0
  
    while right < n:
        while left < n and sol[left] !="1":
            left +=1
            right +=1
        if left >= n:
            break
        elif right <n and sol[right] =="1":
            l = left+1
            r = right-1
            c = k
            while l < r and c > 0:
                sol[l]="1"
                sol[r] = "1"
                l +=1
                r -=1
                c -=1
            left = right
        right +=1
    for i in range(n):
        if sol[i] != "0":
            l = i-1
            c = k
            while l > -1 and c >0:
                sol[l] = '1'
                c -=1
                l -=1
            break
    for j in range(n-1):
        if sol[j] != "0" and sol[j+1] =="0":
          
            r =1 + j
            while r < n and sol[r] != '1':
                r +=1
        
            if r >= n:
                l = j+1 
                c = k
                while l < n and c > 0:
                    sol[l] = '1'
                    l +=1
                    c -=1
                break
            break
    
    print(''.join(sol))
    


            




            
