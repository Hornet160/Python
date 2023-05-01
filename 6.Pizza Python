
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


bill=0
if size.upper()=="S":
    bill+=15
if size.upper()=="M":
    bill+=20
if size.upper()=="L":
    bill+=25
    
#Now add pepperoni
if add_pepperoni.upper()=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

#Now add Chesse
if extra_cheese.upper()=="Y":
    bill+=1
print(f"Your final bill is : ${bill}.")
