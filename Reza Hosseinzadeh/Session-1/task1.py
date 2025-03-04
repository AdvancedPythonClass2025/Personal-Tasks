
def CClear():
    import os
    if os.name == "nt" :
        os.system("cls")
    else :
        os.system("clear")


def factrl(x):
    
    x = int(x)

    if x == 0 :
        return 1
    elif x < 0 :
        return "sahih nist"
    else :
        return (x * factrl(x-1))
   

CClear()      

while True :
           
    try :

        print("baraye mohasebe facturial adad vared konid\n\n\n\n\n")
        inpt = input("_____:")
        print(f"\n\n{inpt}! = {factrl(inpt)} \n")
        break
        
    except ValueError :

        CClear()
        print("lotfan adad vared konid\n\n")
        
    except RecursionError:

        CClear()
        print("adad vared shode bayad kochiktar az 998 bashe\n\n")

    except EOFError:

        CClear()
        print("hich vrodie daryaft nashod\n\n")

    
