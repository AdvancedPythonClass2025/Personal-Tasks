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

