def factoriel(n):
    if n == 0 :
        return 1
    elif n < 0 :
        print("adad bayad x > -1 bashad")
    else :
        return n * factoriel(n-1)

try:
    x = int(input(" adad khod ra benvisid"))
    x = factoriel(x)
    print(f"factorial = {x}")

except ValueError as VE:
    print("error")
    
except  :
    print("error nashenakhte ")