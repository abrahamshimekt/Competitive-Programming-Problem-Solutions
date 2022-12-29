num_tests = int(input())

for test in range(num_tests):

    num_planets,second_machine_cost = input().split()
    planets_oribit = input().split()
    same_orbits = {}

    # collect planets that has the same orbit into a dictionary

    for orbit in planets_oribit:
        if orbit not in same_orbits:
            same_orbits[orbit] =1
        else:
            same_orbits[orbit] +=1

    total_cost  = 0

    # since the first machine cost only 1 Triganic pus 
    # destroy using equals to the number of planets 
    # so to destroy planets I will take the minimum cost to destroy each group of planets
    # I can take min(number of planets in oribit , second machine cost)
    
    for same_orbit in same_orbits:
        if same_orbits[same_orbit] >= int(second_machine_cost):
            total_cost += int(second_machine_cost)
        else:
            total_cost += same_orbits[same_orbit]

    print(total_cost)



