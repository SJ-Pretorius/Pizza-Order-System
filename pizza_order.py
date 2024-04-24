def calculate_pizza_cost(size,toppings_amount):
    cost = 0
    if size == "small" or size == 'Small':
        cost += 10
    elif size == 'medium' or size == 'Medium':
        cost += 12
    elif size == 'large' or size == 'Large':
        cost += 15

    if toppings_amount == 0:
        pass
    elif toppings_amount <= 2:
        cost += toppings_amount
    elif toppings_amount >= 3:
        cost += toppings_amount * 0.75
    return cost

def get_user_input():
    while True:
        size = input("Please enter size of pizza: ")
        if size == "small" or size == "Small" or size == "medium" or size == "Medium" or size == "large" or size == "Large":
            break
        else:
            print('Invalid size!')
            continue
    while True:
        toppings_amount= input('Please indicate the amount of toppings you want: ')
        if toppings_amount.isdigit() == True:
            toppings_amount = int(toppings_amount)
            break
        else:
            print('Invalid amount!')
            continue

    limit=toppings_amount
    toppings_list = ['pepperoni','sausage','pineapple','mushrooms','olives']
    selected_toppings = []

    while True:
        if toppings_amount == 0:
            break
        if limit == 0:
            break
        topping_input = input(f'Enter a topping from {toppings_list}: ')
        if topping_input in toppings_list:
            selected_toppings.append(topping_input)
            limit -= 1 
            print()
            if limit == 1:
                print(limit,'topping left!')
            elif limit >= 2:
                print(limit,'toppings left!')
            print('You have chosen',selected_toppings)
            print()
        else:
            print("Invalid topping.")

    return size, toppings_amount

while True:
    print()
    size,toppings_amount = get_user_input()
    final = calculate_pizza_cost(size,toppings_amount)

    if toppings_amount ==0:
        print()
        print("The total cost of your plain pizza is R" + str(final) + "!")
        print()
    elif toppings_amount ==1:
        print("The total cost of your pizza with 1 topping is R" + str(final) + "!")
        print()
    else:
        print("The total cost of your pizza with " + str(toppings_amount) + " toppings is R" + str(final) + "!")
        print()
    while True:
        rep = input('Do you want to work out the cost for another pizza? (Y or N) ')
        if rep == 'Y' or rep == 'y':
            break
        elif rep == 'N' or rep == 'n':
            print()
            print('Thank you. Goodbye!')
            print()
            exit()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")