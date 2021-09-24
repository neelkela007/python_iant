def fib(n):
    if n <= 1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
number_of_terms = 11
for i in range(number_of_terms):
    print(fib(i))
