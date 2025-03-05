def factorial(n):
    if n == 0 :
        return 1
    elif n < 0 :
        print("adad bozorgtar  az (-1) ra vared konid")
    else :
        return n * factorial(n-1)

try:
    x = int(input("adad mored nazar ra vared konid"))
    x = factorial(x)
    print(f"factorial = {x}")

except ValueError as VE:
    print(f"khata : {VE}")

except Exception as E :
    print(f"khatay sistm : {E}")
