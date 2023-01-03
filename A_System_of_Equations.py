n,m = input().split()
constant = int(m)-pow(int(n),2)
factors = []
for index in range(1,(abs(constant//2)+1)):
    if constant % index == 0:
        factors.append(index)

pair_num = 0
for factor in factors:
    if pow(factor,4) - 2*pow(factor,2)*int(n) + factor == constant:
        pair_num +=1
    elif pow(-1*factor,4) - 2*pow(-1*factor,2)*int(n) - factor == constant:
        pair_num +=1
print(pair_num)

    
