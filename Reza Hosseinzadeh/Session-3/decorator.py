import os
import time

def CClear():

    if os.name == "nt" :      
        os.system("cls")
    else :  
        os.system("clear")

def zaman(func):
    
    def Wrapper(*args , **kwargs):
        
        zaman_shoro    = time.time()  
        funct        = func(*args , **kwargs)  
        zaman_payan      = time.time()  

        print(f"\n\nzaman ejra : {zaman_shoro - zaman_payan} sec\n\n")
        return funct
    
    return Wrapper


@zaman
def zoj_fard(adad):
    
    if adad % 2 == 0 :
        return f"\nadad {adad} Zoj hast\n"
    
    else :
        return f"\nadad {adad} Fard hast\n"
