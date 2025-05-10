def factorial(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("عدد نمی‌تواند منفی باشد.")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except ValueError as ve:
        return f"خطا: {ve}"
    except TypeError:
        return "خطا: ورودی باید یک عدد باشد."

print(factorial(5))    
print(factorial("hello")) 
print(factorial(-3))   