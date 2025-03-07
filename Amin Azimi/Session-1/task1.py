def factorial(n):
    if n == 0 :
        return 1
    elif n < 0 :
        print(" bozorgtar az -1 ")
    else :
        return n * factorial(n-1)

try:
    x = int(input("adad mord nazae vared konid "))
    x = factorial(x)
    print(f"factorial = {x}")

except ValueError as VE:
    print(f"Eror: {VE}")
    
except Exception as E:
    print(f"eror nashenakhte :{E}")    