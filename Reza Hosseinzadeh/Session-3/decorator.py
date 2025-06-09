import os

def CClear():

    if os.name == "nt" :      
        os.system("cls")
    else :  
        os.system("clear")