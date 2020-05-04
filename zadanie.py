fib = [0,1]
n = int(input())
dodaj = 0
for i in range(2,n+1):
    dodaj = fib[-1] + fib[-2]
    fib.append(dodaj)

print(fib)