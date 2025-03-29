def factorial(x):
    if x == 0 :
        return 1
    if x > 0 :
        return x * factorial(x-1)

try :
    
    print(factorial(int(input())))

except ValueError as V:
    print(V)

except Exception as E :
    print(E)