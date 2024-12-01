#Task3
def fibonacci_series(n):
    a,b=0,1
    fibonacci = []
    while a <= n:
        fibonacci.append(a)
        a,b=b,a+b
    return fibonacci

n = int(input("Enter the value of n: "))
result = fibonacci_series(n)
print(f"Fibonacci series up to {n}: {result}")

#Task4
m=int(input("Enter a number:"))
for i in range(1,11):
    mul_table=m*i
    print(m,"x",i,"=",mul_table)