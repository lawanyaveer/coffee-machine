# coffee machine project

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is not enough {item} ")
            return False
    return True
    
def process_coin():
    print("insert coins")
    total = int(input("insert number of dimes? : "))*0.10
    total += int(input("insert number of nickels? :"))*0.05
    total  += int(input("insert number of pennies? :"))*0.01
    total += int(input("insert number of quarter? :"))*0.25
    return total


def transactions_sucessfull(money_recived,cost_of_drink):

    if money_recived >= cost_of_drink:
        change = round(money_recived - cost_of_drink)
        print(f"Here is the ${change} in change")
        print("sorry thats not enough money")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("sorry that's not enough money")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


machine_is_on = True
while machine_is_on:
        user_input = input("what would you like to have? (cappuccino/espresso/latte): ")
        if user_input == "off":
            machine_is_on = False
        elif user_input == "report":
            print(f" water : {resources['water']} ml ")
            print(f" milk : {resources['milk']} ml")
            print(f" coffee : {resources['coffee']} g ")
            print(f"money : ${profit}")
        else:
            drinks = MENU[user_input]
            if resources_sufficient(drinks['ingredients']):
                payment = process_coin()
                if transactions_sucessfull(payment,drinks['cost']):
                    make_coffee(user_input,drinks['ingredients'])
        



    
    
    
    


    





