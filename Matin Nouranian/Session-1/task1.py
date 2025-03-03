def factorial(num):
    if num == 0 :
        return 1
    else :
        return num * factorial(num - 1)

try :
    x = int(input("lotfan addad sahih va gheyre manfi vared konid : "))
    re = factorial(x)
    if x > 0 :
        print(f"factorial = {re}")
    elif x < 0 :
        print(f"addad mosbat vared konid")
except Exception as e :
    print(f"khata : {e}")
#except :
    #print("khata lotfan addad vared konid")