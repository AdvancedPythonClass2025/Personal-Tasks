import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} to execute.")
        return result
    return wrapper


@timer_decorator
def my_function(n):
    time.sleep(n)
    return n * 2

result = my_function(2)
print(f"function result: {result}")