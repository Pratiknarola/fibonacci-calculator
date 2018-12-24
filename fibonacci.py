num = int(input("enter number of terms in fib: "))
fib = [1,1]
while (num - 2):
    number = fib[len(fib)-1] + fib[len(fib)-2]
    fib.append(number)
    num = num - 1

print(fib)