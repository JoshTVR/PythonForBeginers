"""
safe_division.py — try / except
Chapter 11: Error Handling

Demonstrates:
- try / except blocks to catch errors
- Catching specific exception types (ValueError, ZeroDivisionError)
- The else clause (runs only if no exception occurred)
- The finally clause (ALWAYS runs, error or not)
- Reading the traceback — error type and message
"""

# --- Without error handling ---
# If you run this without try/except and type 'abc', it crashes:
#
# Traceback (most recent call last):
#   File "safe_division.py", line X
#     numerator = float(input(...))
# ValueError: could not convert string to float: 'abc'

# --- With error handling ---

print('--- Safe Division Calculator ---')

try:
    # Code that MIGHT fail goes inside try
    numerator = float(input('Enter numerator: '))
    denominator = float(input('Enter denominator: '))
    result = numerator / denominator

except ValueError:
    # Runs if the user types something that can't be converted to float
    print('❌ Please enter valid numbers only.')

except ZeroDivisionError:
    # Runs if denominator is zero
    print('❌ Cannot divide by zero!')

else:
    # Runs ONLY if no exception occurred (no error = success)
    print(f'✅ {numerator} ÷ {denominator} = {result:.4f}')

finally:
    # ALWAYS runs — even if there was an error
    # Great for cleanup operations
    print('Calculator session ended.')

# --- Example runs:
#
# Valid input: 10 / 4
# ✅ 10.0 ÷ 4.0 = 2.5000
# Calculator session ended.
#
# Zero denominator: 10 / 0
# ❌ Cannot divide by zero!
# Calculator session ended.
#
# Non-numeric input: 'hello' / 4
# ❌ Please enter valid numbers only.
# Calculator session ended.
