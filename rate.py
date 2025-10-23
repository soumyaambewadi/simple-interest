# simple_interest.py
# Program to calculate Simple Interest

import sys

# If arguments are provided via command line
if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    # Fallback for local runs (manual input)
    principal = float(input("Enter the Principal amount: "))
    rate = float(input("Enter the Rate of Interest: "))
    time = float(input("Enter the Time period (in years): "))

# Calculation
simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest}")