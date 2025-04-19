def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time  
        print(f"زمان اجرای تابع '{func.__name__}': {execution_time:.6f} ثانیه")
        return result
    return wrapper
  
@timing_decorator
def example_function(n):
    time.sleep(n)  
    return "پایان اجرا!"
  
