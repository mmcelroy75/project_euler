fib_seq = [1, 2]
fib_seq_even = []

while (fib_seq[-1] + fib_seq[-2]) < 4_000_000:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

for i in fib_seq:
    if i % 2 == 0:
       fib_seq_even.append(i) 

fib_seq_even_sum = sum(fib_seq_even)

print(fib_seq)
print(fib_seq_even)
print(fib_seq_even_sum)
print(len(fib_seq))
#5702886 -- 5702887
#3524576 -- 3524578
#4613732 -- 