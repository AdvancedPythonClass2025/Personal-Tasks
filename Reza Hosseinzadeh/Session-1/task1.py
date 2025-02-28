
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

        print("baraye mohasebe facrutiel adad vared konid\n\n\n\n\n")
        inpt = input("_____:")
        print(f"\n\n{inpt}! = {factrl(inpt)} \n")
        break
        
    except ValueError :

        CClear()
        print("lotfan adad vared konid\n\n")
        

    except Exception:

        CClear()
        print("khataye nashenakhte\n\n")
