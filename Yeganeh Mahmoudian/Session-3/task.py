import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)
        end_time = time.time()    
        duration = end_time - start_time
        print(f"زمان اجرا: {duration:.4f} ثانیه")
        return result
    return wrapper

@measure_time
def example_function():
    time.sleep(2)  
    print("تابع اجرا شد.")

example_function()