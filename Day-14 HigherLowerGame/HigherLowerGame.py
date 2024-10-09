# import random number and game data
from art import logo,vs
from game_data import data
import random



def formant_data(account):
    '''Takes account data and returns pritable format.'''
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"

print(logo)
#     initialize the Score with zero
score =0
game_should_continue=True
account_b=random.choice(data)
#Make game repeatable
while game_should_continue:
    #Generate Random Accounts
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A: {formant_data(account_a)}")
    print(vs)
    print(f"Compare B: {formant_data(account_b)} ")

    #Format the data into Printable format



    #Ask user for a guess
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    #Clear the screen
    print("\n" *20)
    print(logo)



    # Check if user is correct or not.


    #_Get follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)

    #give feedback on their guess
    if is_correct:
        score+=1
        print(f"You're right.Current score is {score}")
    else:
        print(f"Sorry, Try again. Your score is {score}")
        game_should_continue=False


