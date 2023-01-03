num_forces = int(input())
total_force = 0
x_sum=y_sum=z_sum =0
for index in range(num_forces):
    forces = input().split()
    x_sum += int(forces[0])
    y_sum += int(forces[1])
    z_sum += int(forces[2])
    
if x_sum == y_sum == z_sum == 0:
    print("YES")
else:
    print("NO")
