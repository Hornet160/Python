import random

from game_data import data
from art import logo,vs
#format the data
def data_formation(account):
    account_name=account["name"]
    account_des=account["description"]
    account_location=account["country"]
    return f"{account_name}, a {account_des}, from {account_location}"
#Make comparison
def data_compparison(account):
    account_followers=account['follower_count']
    return account_followers

def check_answer(user, a_followers, b_followers):
    if a_followers>b_followers:
        return user=='a'
    else:
        return user=='b'

score=0
#print the logo
print(logo)
account_b=random.choice(data)
should_continue=True
while should_continue:
#choose random person
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {data_formation(account_a)}")
    print(f"Compare B: {data_formation(account_b)}")

    guess= input("Who has more followers? Type 'A' or 'B' : ").lower()
    print("\n"*20)
    print(logo)
    #assign the returned followers in a variable
    a_follower=data_compparison(account_a)
    b_follower=data_compparison(account_b)
    is_correct=check_answer(guess,a_follower,b_follower)
    if is_correct:
        score+=1
        print(f"You're right! Current score:{score}")
    else:
        print(f"You're Wrong! Your total score is:{score}")
        should_continue=False