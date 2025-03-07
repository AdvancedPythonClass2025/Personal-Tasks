def factorial(n):
  
    if not isinstance(n, int):  
        raise ValueError("عدد ورودی باید یک عدد صحیح باشد.")
    if n < 0:  # بررسی اینکه عدد منفی نباشد
        raise ValueError("عدد نمی‌تواند منفی باشد.")
    if n == 0 or n == 1:  # شرط توقف
        return 1
    return n * factorial(n - 1)  
# دریافت ورودی از کاربر و مدیریت استثنا
try:
    num = int(input("عدد موردنظر را وارد کنید: "))
    result = factorial(num)
    print(f"فاکتوریل {num} برابر است با: {result}")
except ValueError as e:
    print(f"خطا: {e}")
