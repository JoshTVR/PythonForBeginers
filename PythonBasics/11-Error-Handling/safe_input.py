"""
safe_input.py — Looping Until Valid Input
Chapter 11: Error Handling

Demonstrates:
- while True loop combined with try/except
- Breaking out of the loop on success
- Raising custom exceptions with 'raise'
- Validating data with meaningful error messages
"""

# --- Pattern: keep asking until valid input ---

def get_integer(prompt):
    """Keep asking for input until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('That\'s not a whole number. Try again!')


def get_positive(prompt):
    """Keep asking until the user enters a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError('Must be a positive number.')
            return value
        except ValueError as e:
            print(f'Invalid: {e}. Try again!')


# --- Using the functions ---
age = get_integer('Enter your age: ')
print(f'In 10 years you\'ll be {age + 10} 🎂')

quantity = get_positive('How many items? ')
price = 4500
print(f'{quantity} items × ${price:,} COP = ${quantity * price:,} COP')


# --- Raising your own exceptions ---
# Use 'raise' to enforce rules in your own functions

def set_percentage(value):
    """Accept only values between 0 and 100."""
    if not isinstance(value, (int, float)):
        raise TypeError(f'Expected a number, got {type(value).__name__}')
    if value < 0 or value > 100:
        raise ValueError(f'Percentage must be 0–100, got {value}')
    return value

# Wrapping in try/except to handle it gracefully
for test in [75, 110, -5, 'abc']:
    try:
        result = set_percentage(test)
        print(f'set_percentage({test}) = {result}%  ✅')
    except (ValueError, TypeError) as e:
        print(f'set_percentage({test}) → Error: {e}  ❌')

# Output:
# set_percentage(75) = 75%  ✅
# set_percentage(110) → Error: Percentage must be 0–100, got 110  ❌
# set_percentage(-5) → Error: Percentage must be 0–100, got -5  ❌
# set_percentage(abc) → Error: Expected a number, got str  ❌
