num_tests = int(input())
for test in range(num_tests):
    num_planets,second_machine_cost = input().split()
    planets_oribit = input().split()
    same_orbits = {}
    for orbit in planets_oribit:
        if orbit not in same_orbits:
            same_orbits[orbit] =1
        else:
            same_orbits[orbit] +=1
    total_cost  = 0
    for same_orbit in same_orbits:
        if same_orbits[same_orbit] >= int(second_machine_cost):
            total_cost += int(second_machine_cost)
        else:
            total_cost += same_orbits[same_orbit]
    print(total_cost)



