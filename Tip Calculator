                             # Welcome to tip Calculator
print("Welcome to the Tip Calculator.")
bill=float(input("What was the total bill? $"))
tip_percent=int(input("What percentage tip would you like to give? 10, 12, 15? "))
calculate_tip=(tip_percent/100)+1 #Turn the tip to mathematical form
person_to_pay=int(input("How many people to split the bill? "))
payable=(bill*calculate_tip)/person_to_pay # calculate the final amount per person with tip
# two ways of rounding  regardless of no decimal points.
print(f"Each person should pay: ${payable:.2f}")
payable="{:.2f}".format(payable)
print(f"Each person should pay: ${payable}")
