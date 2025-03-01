"""Factorial Calculator using Recursive Functions"""

def factorial(number: int) -> int:
    """
    Recursively Calculate Factorial.
    This function recursively calls itself to calculate the factorial.
    It raises error if the number is negative or is not an integer.
    - args:
        number: integer
    - returns:
        - Call to the function with decremented value
        - 1 if number is equal to 0
        - Integer at the end of the calculations
    """
    if number < 0: # Raise value error if number is negative
        raise ValueError("Number should be positive.")
    if number == 0: # In order to prevent zero results
        return 1
    else: # Recursively call the function with decremented value
        return number * factorial(number - 1)

while True:
    # Try to get an input from the user, convert it to an int, call the function and print the result
    try:
        user_input = int(input('Enter Number: '))
        result = factorial(user_input)
        print(result)
    except ValueError as e: # Handle the case user input is not an integer
        print(f'Error : {e}')
        continue
    except Exception as e: # Handle any other error
        print(f'Unknown Error: {e}')
        break
