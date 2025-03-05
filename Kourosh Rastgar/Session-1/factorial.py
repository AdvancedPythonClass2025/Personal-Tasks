def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def get_factorial():
    try:
        num = int(input("enter a number to calculate its factorial: "))
        if num < 0:
            raise ValueError("input number cant be negative")
        result = factorial(num)
        print(f"factorial of {num} is {result}")
    except ValueError as e:
        print(f"invalid input: {e}")
get_factorial()