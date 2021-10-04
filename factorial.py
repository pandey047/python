def factorial(n):
    if n==0 or n==1:
        print("Factorial is :",1)
    else:
        return n * factorial(n-1)


factorial(4)