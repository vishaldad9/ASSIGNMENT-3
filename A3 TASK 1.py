def factorial(n):
    if n < 2 :
        return 1
    else:
        return n*(factorial(n-1))
n=int(input("Enter the number : "))
result= factorial(n)

print("factorial of", n , "is", result)



