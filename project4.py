#largest number will be 6 digits
#print(999*999)

palindromes = []

for i in range(100, 999):
    for n in range(100, 999):
        x = (i * n)
        if (str(x)[0] == str(x)[-1]) and (str(x)[1] == str(x)[-2]) and (str(x)[2] == str(x)[-3]):
            palindromes.append(x)

palindromes_sorted = sorted(palindromes)

print(len(palindromes_sorted))

print(palindromes_sorted[-1])
        

