multiples_lst = []

i = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        multiples_lst.append(i) 

print(sum(multiples_lst[:]))

#sum is equal to 23,3168