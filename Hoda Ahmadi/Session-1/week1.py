#یک تابع بازگشتی برای فاکتوریل مینویسیم
def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)

#از کاربر یه ورودی میگیریم
try:
    number = int(input("please enter valid number"))
    if number < 0:
        raise ValueError("please enter a non negative number")
    else:
        result = factorial(number)
        raise ValueError(f"the factorial of {number} is {result}")
except ValueError:
    print("incorrect please enter a valid number")


