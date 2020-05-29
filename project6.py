def sum_of_squares(num1):
    sum = 0
    for i in range(1, num1+1):
        sum += i**2
    return sum

def square_of_sum(num1):
    sum = 0
    for i in range(num1, 0, -1):
        sum += i
    result = sum**2
    return result
    

first = sum_of_squares(100)
    
second = square_of_sum(100)

print(first)
print(second)
print(second - first)