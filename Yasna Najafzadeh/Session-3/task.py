import time

def zaman(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        print(f" {end_time - start_time} ")
        return result
    return wrapper
 
@zaman
def function_nemone():
    time.sleep(2)  

function_nemone()