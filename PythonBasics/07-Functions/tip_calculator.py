"""
tip_calculator.py — User-Defined Functions
Chapter 7: Functions

Demonstrates:
- Defining a function with def
- Parameters and default parameters
- Return values
- Calling a function multiple times (the DRY principle in action)
"""

# --- Defining a function ---
# 'def' keyword + name + parentheses + colon
# Everything indented below is the function body

def calculate_tip(bill, tip_percent=15):
    """
    Calculate the tip for a restaurant bill.

    bill       : float — total bill amount in USD
    tip_percent: int   — tip percentage (default 15%)

    Returns the tip amount as a float.
    """
    tip = bill * (tip_percent / 100)
    return tip  # sends the value BACK — different from print()


# --- Calling the function ---
# Use the return value by assigning it to a variable

tip1 = calculate_tip(50)           # uses default 15%
tip2 = calculate_tip(80, 20)       # 20% tip
tip3 = calculate_tip(120, 10)      # 10% tip

print(f'Bill: $50.00  | Tip (15%): ${tip1:.2f}')
print(f'Bill: $80.00  | Tip (20%): ${tip2:.2f}')
print(f'Bill: $120.00 | Tip (10%): ${tip3:.2f}')

# Output:
# Bill: $50.00  | Tip (15%): $7.50
# Bill: $80.00  | Tip (20%): $16.00
# Bill: $120.00 | Tip (10%): $12.00


# --- A slightly more complete version ---
def full_bill_summary(bill, tip_percent=15, people=1):
    """
    Calculate tip and split the total among a group.

    bill       : float — total bill
    tip_percent: int   — tip percentage (default 15%)
    people     : int   — number of people splitting (default 1)

    Prints a full breakdown.
    """
    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people

    print(f'--- Bill Summary ---')
    print(f'Subtotal:   ${bill:.2f}')
    print(f'Tip ({tip_percent}%): ${tip:.2f}')
    print(f'Total:      ${total:.2f}')
    if people > 1:
        print(f'Per person: ${per_person:.2f}  ({people} people)')
    print()


full_bill_summary(60)               # solo diner, default tip
full_bill_summary(200, 18, 4)       # group of 4, 18% tip
full_bill_summary(95, 20, 2)        # couple, 20% tip

# Output:
# --- Bill Summary ---
# Subtotal:   $60.00
# Tip (15%): $9.00
# Total:      $69.00
#
# --- Bill Summary ---
# Subtotal:   $200.00
# Tip (18%): $36.00
# Total:      $236.00
# Per person: $59.00  (4 people)
#
# --- Bill Summary ---
# Subtotal:   $95.00
# Tip (20%): $19.00
# Total:      $114.00
# Per person: $57.00  (2 people)
