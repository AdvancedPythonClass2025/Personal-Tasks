def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # زمان شروع اجرا
        result = func(*args, **kwargs)  # اجرای تابع اصلی
        end_time = time.time()  # زمان پایان اجرا
        execution_time = end_time - start_time  # محاسبه زمان اجرا
        print(f"زمان اجرای تابع '{func.__name__}': {execution_time:.6f} ثانیه")
        return result
    return wrapper

# استفاده از دکوریتور
@timing_decorator
def example_function(n):
    time.sleep(n)  # شبیه‌سازی یک عملیات زمان‌بر
    return "پایان اجرا!"
  
