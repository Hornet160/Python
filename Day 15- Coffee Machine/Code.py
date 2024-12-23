MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made. False when ingredient insufficient'''
    for item in order_ingredients:
        if order_ingredients[item]> resources[item]:
            print(f"Sorry there in not enough {item}")
            return False
    return True
def coin_processing():
    "returns the total calculated from coin inserted"
    print("Please insert coins. ")
    total=int(input("how many quaters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.10
    total+=int(input("how many nickels?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total
def is_transaction_succesful(money_received,drink_cost):
    if money_received>drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    "deduct the required ingredients from resources"
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")
is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice== "report":
        print(f"Water{resources['water']} ml\n"
              f"Milk{resources['milk']} ml\n"
              f"Coffee{resources['coffee']} ml\n"
              f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=coin_processing()
            if is_transaction_succesful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])




