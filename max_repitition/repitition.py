chromosomes = input()
left = 0
right = 0
max_gene_sequence = 0
while right <len(chromosomes):
    if chromosomes[left] != chromosomes[right]:
        max_gene_sequence= max(max_gene_sequence,right-left)
        left = right
        right +=1
    else:
        right +=1
        if right == len(chromosomes):
            max_gene_sequence= max(max_gene_sequence,right-left)
print(max_gene_sequence)


