# Kirin Hardinger
# CS 333 Honors contract project
# Spring 2023

import os # to clear screen
import json # for save files
import customer
import ingredient
import inventory
from game_helper import *

def ingredients_array_to_str_array(items):
    str_array = []
    for item in items:
        str_array.append(item.get_name())
    return str_array

unlockable = [
    ingredient.Ingredient("matcha tea", "base"),
    ingredient.Ingredient("taro milk tea", "base"),
    ingredient.Ingredient("choco milk tea", "base"),
    ingredient.Ingredient("strawberry milk tea", "base"),
    ingredient.Ingredient("coconut milk tea", "base"),
    ingredient.Ingredient("mango milk tea", "base"),
    ingredient.Ingredient("strawberry boba", "boba"),
    ingredient.Ingredient("mango boba", "boba"),
    ingredient.Ingredient("lychee boba", "boba"),
    ingredient.Ingredient("peach boba", "boba"),
    ingredient.Ingredient("mango jelly", "boba"),
    ingredient.Ingredient("lychee jelly", "boba"),
    ingredient.Ingredient("whip cream", "topping"),
    ingredient.Ingredient("chocolate syrup", "topping"),
    ingredient.Ingredient("strawberry syrup", "topping"),
    ingredient.Ingredient("mango syrup", "topping"),
    ingredient.Ingredient("cocoa powder", "topping"),
    ingredient.Ingredient("matcha powder", "topping"),
]
unlock_stock = inventory.Inventory()
for item in unlockable:
    unlock_stock.add_item(item)

def initialize_save_file(shop_name):
    # searches for an existing json file with the same name as the shop
    # if it exists, it loads the data from that file
    # if it doesn't exist, it creates a new file with the shop name
    # returns the save file as a dictionary
    save_file = {}
    
    # check if save file exists
    if(os.path.isfile(f'{shop_name}.json')):
        # load save file
        with open(f'{shop_name}.json') as f:
            save_file = json.load(f)
    else:
        save_file["shop_name"] = shop_name
        save_file["day_number"] = 1
        save_file["money"] = 100
        save_file["items"] = {}
        save_file["items"]["bases"] = ["plain milk tea", "almond milk tea"]
        save_file["items"]["bobas"] = ["plain boba", "crystal boba"]
        save_file["items"]["toppings"] = []
        save_file["shops"] = {}
        save_file["shops"]["bases"] = ingredients_array_to_str_array(unlock_stock.get_bases())
        save_file["shops"]["bobas"] = ingredients_array_to_str_array(unlock_stock.get_bobas())
        save_file["shops"]["toppings"] = ingredients_array_to_str_array(unlock_stock.get_toppings())

        print("As a new shop owner, you have been given $100 to start your business.")
        print("You can use this money to unlock new, exciting ingredients!")
        print("Currently, you only have access to plain milk tea, almond milk tea, plain boba, and crystal boba.\n")

        # create save file
        with open(f'{shop_name}.json', 'w') as f:
            json.dump(save_file, f)

def update_save_file(shop_name, money, day_num, m_shop, inventory):
    # load save file
    with open(f'{shop_name}.json') as f:
        save_file = json.load(f)

    # update save file
    save_file["day_number"] = day_num
    save_file["money"] = money

    # get list of bases, bobas, toppings
    # if the ingredient is not already in the list, add it
    # if the ingredient is already in the list, do nothing
    bases = save_file["items"]["bases"]
    bobas = save_file["items"]["bobas"]
    toppings = save_file["items"]["toppings"]

    for item in inventory.get_stock():
        if(item.get_type() == "base"):
            if(item.get_name() not in bases):
                bases.append(item.get_name())
        elif(item.get_type() == "boba"):
            if(item.get_name() not in bobas):
                bobas.append(item.get_name())
        elif(item.get_type() == "topping"):
            if(item.get_name() not in toppings):
                toppings.append(item.get_name())
    
    # saves status of shop ingredients
    shop_bases = save_file["shops"]["bases"]
    shop_bobas = save_file["shops"]["bobas"]
    shop_toppings = save_file["shops"]["toppings"]

    for item in m_shop.get_stock():
        if(item.get_type() == "base"):
            if(item.get_name() not in shop_bases):
                shop_bases.append(item.get_name())
        elif(item.get_type() == "boba"):
            if(item.get_name() not in shop_bobas):
                shop_bobas.append(item.get_name())
        elif(item.get_type() == "topping"):
            if(item.get_name() not in shop_toppings):
                shop_toppings.append(item.get_name())

    # save new save file
    with open(f'{shop_name}.json', 'w') as f:
        json.dump(save_file, f)

def inventory_from_save_file(shop_name):
    # load save file
    with open(f'{shop_name}.json') as f:
        save_file = json.load(f)
    
    # create inventory
    m_inventory = inventory.Inventory()
    bases = save_file["items"]["bases"]
    bobas = save_file["items"]["bobas"]
    toppings = save_file["items"]["toppings"]
    for base in bases:
        m_inventory.add_item(ingredient.Ingredient(base, "base"))
    for boba in bobas:
        m_inventory.add_item(ingredient.Ingredient(boba, "boba"))
    for topping in toppings:
        m_inventory.add_item(ingredient.Ingredient(topping, "topping"))
    
    return m_inventory

def shop_from_save_file(shop_name):
    # load save file
    with open(f'{shop_name}.json') as f:
        save_file = json.load(f)
    
    # create inventory
    m_shop = inventory.Inventory()
    bases = save_file["shops"]["bases"]
    bobas = save_file["shops"]["bobas"]
    toppings = save_file["shops"]["toppings"]
    for base in bases:
        m_shop.add_item(ingredient.Ingredient(base, "base"))
    for boba in bobas:
        m_shop.add_item(ingredient.Ingredient(boba, "boba"))
    for topping in toppings:
        m_shop.add_item(ingredient.Ingredient(topping, "topping"))
    
    return m_shop

def load_save_file(shop_name):
    # load save file
    with open(f'{shop_name}.json') as f:
        save_file = json.load(f)
    
    return save_file

def display_shop_element(shop, inventory, type):
    color_print(f'\n*!*{type.upper()}*!*', 'b')
    print(f'Here are the {type} you can buy. ([0] to go back)')

    if type == 'bases':
        options = shop.get_bases()
        for option in options:
            if inventory.get_item_by_name(option.get_name()) != None:
                options.remove(option)
    elif type == 'bobas':
        options = shop.get_bobas()
        for option in options:
            if inventory.get_item_by_name(option.get_name()) != None:
                options.remove(option)
    elif type == 'toppings':
        options = shop.get_toppings()
        for option in options:
            if inventory.get_item_by_name(option.get_name()) != None:
                options.remove(option)

    for i in range(len(options)):
        print(f"[{i+1}] {options[i].get_name()}")

def buy_new_ingredients(shop_name, day_num, m_shop, m_inventory):
    # load save data
    save_file = load_save_file(shop_name)
    money = save_file["money"]

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print('      ___ ___ .   __      __        __   __    /')
    print('|    |__   |  \' /__`    /__` |__| /  \ |__)  / ')
    print('|___ |___  |    .__/    .__/ |  | \__/ |    .  ')

    color_print(f'\nWelcome to the ingredient shop! You have ${money} to spend today.', 'g')
    color_print("ALL items are $100 each.", 'g')
    category_choice = 1
    while category_choice != '0':
        category_choice = input("Would you like to look at [1] tea bases, [2] boba, or [3] toppings? [0] to LEAVE SHOP: ")

        while category_choice not in ['0', '1', '2', '3']:
            color_print("Invalid input. Please enter a number from 0-3.", 'r')
            category_choice = input("Would you like to look at [1] tea bases, [2] boba, or [3] toppings? [0] to LEAVE SHOP: ")

        if category_choice == '0':
            color_print("Thanks for shopping! Come back soon!", 'b')
            break
        if category_choice == '1':
            # if the player has already bought all the bases, don't show the bases
            if len(m_shop.get_bases()) == 0:
                color_print("You already have all the bases!", 'r')
                continue

            display_shop_element(m_shop, m_inventory, 'bases')
            choice = 1
            while choice != '0':
                choice = input("\nEnter your choice: ")

                while choice.isnumeric() == False or int(choice) not in range(0, len(m_shop.get_bases()) + 1):
                    color_print("Invalid input. Please enter a valid number.", 'r')
                    choice = input("\nEnter your choice: ")
                
                if choice == '0':
                    break
                if int(choice) in range(1, len(m_shop.get_bases()) + 1) and money >= 100:
                    # add item to inventory
                    m_inventory.add_item(m_shop.get_bases()[int(choice) - 1])

                    money -= 100
                    color_print(f"You have purchased {m_shop.get_bases()[int(choice) - 1].get_name()}.", 'g')
                    color_print(f"You now have ${money} left.", 'g')

                    # remove item from shop
                    m_shop.remove_item(m_shop.get_bases()[int(choice) - 1])

                    # update save file with new shop
                    update_save_file(shop_name, money, day_num, m_shop, m_inventory)
                elif money < 100:
                    color_print("You don't have enough money to buy this item.", 'r')
                
                display_shop_element(m_shop, m_inventory, 'bases')
        elif category_choice == '2':
            # if the player has already bought all the bases, don't show the bases
            if len(m_shop.get_bobas()) == 0:
                color_print("You already have all the bobas!", 'r')
                continue

            display_shop_element(m_shop, m_inventory, 'bobas')
            choice = 1
            while choice != '0':
                choice = input("\nEnter your choice: ")

                while choice.isnumeric() == False or int(choice) not in range(0, len(m_shop.get_bobas()) + 1):
                    color_print("Invalid input. Please enter a valid number.", 'r')
                    choice = input("\nEnter your choice: ")
                
                if choice == '0':
                    break
                if int(choice) in range(1, len(m_shop.get_bobas()) + 1) and money >= 100:
                    # add item to inventory
                    m_inventory.add_item(m_shop.get_bobas()[int(choice) - 1])

                    money -= 100
                    color_print(f"You have purchased {m_shop.get_bobas()[int(choice) - 1].get_name()}.", 'g')
                    color_print(f"You now have ${money} left.", 'g')

                    # remove item from shop
                    m_shop.remove_item(m_shop.get_bobas()[int(choice) - 1])

                    # update save file with new shop
                    update_save_file(shop_name, money, day_num, m_shop, m_inventory)
                elif money < 100:
                    color_print("You don't have enough money to buy this item.", 'r')
                
                display_shop_element(m_shop, m_inventory, 'bobas')
        elif category_choice == '3':
            # if the player has already bought all the bases, don't show the bases
            if len(m_shop.get_bases()) == 0:
                color_print("You already have all the toppings!", 'r')
                continue

            display_shop_element(m_shop, m_inventory, 'toppings')
            choice = 1
            while choice != '0':
                choice = input("\nEnter your choice: ")

                while choice.isnumeric() == False or int(choice) not in range(0, len(m_shop.get_toppings()) + 1):
                    color_print("Invalid input. Please enter a valid number.", 'r')
                    choice = input("\nEnter your choice: ")
                
                if choice == '0':
                    break
                if int(choice) in range(1, len(m_shop.get_toppings()) + 1) and money >= 100:
                    # add item to inventory
                    m_inventory.add_item(m_shop.get_toppings()[int(choice) - 1])

                    money -= 100
                    color_print(f"You have purchased {m_shop.get_toppings()[int(choice) - 1].get_name()}.", 'g')
                    color_print(f"You now have ${money} left.", 'g')

                    # remove item from shop
                    m_shop.remove_item(m_shop.get_toppings()[int(choice) - 1])

                    # update save file with new shop
                    update_save_file(shop_name, money, day_num, m_shop, m_inventory)
                elif money < 100:
                    color_print("You don't have enough money to buy this item.", 'r')
                
                display_shop_element(m_shop, m_inventory, 'toppings')
    update_save_file(shop_name, money, day_num, m_shop, m_inventory)

def run_day(shop_name):
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # load save data
    save_file = load_save_file(shop_name)
    day_num = save_file["day_number"]
    money = save_file["money"]
    m_shop = shop_from_save_file(shop_name)
    m_inventory = inventory_from_save_file(shop_name)

    # summarize start of day
    color_print(f'~*~Day {day_num} at {shop_name}~*~', 'g')
    color_print(f'You have ${money}.\n', 'g')

    # generate 3 customers each with a random order
    profit = 0
    for _ in range(3):
        temp_profit = 0
        num_correct = 0
        m_customer = customer.Customer()
        order = m_customer.generate_order(m_inventory)
        print(f'{m_customer.name} ordered a {order.get_base()} with {order.get_boba()}. Top it with {order.get_toppings()}.')

        while True:
            color_print("Do you have the order memorized? Press enter to continue.", 'r')
            inp = input()
            if(not inp):
                break
        
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Ready to make the drink? Choose the correct base. ")
        for i in range(m_inventory.get_length("base")):
            print(f'{i+1}. {m_inventory.get_bases()[i].get_name()}')
        base_choice = -1
        while base_choice not in range(1, m_inventory.get_length("base") + 1):
            base_choice = int(input())
        base_choice = m_inventory.get_bases()[base_choice - 1]
        correct_base = order.get_base()
        if base_choice.get_name() == correct_base:
            temp_profit += 20
            num_correct += 1
        
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Choose the correct boba. ")
        for i in range(m_inventory.get_length("boba")): 
            print(f'{i+1}. {m_inventory.get_bobas()[i].get_name()}')
        boba_choice = -1
        while int(boba_choice) not in range(m_inventory.get_length("boba") + 1):
            boba_choice = int(input())
        boba_choice = m_inventory.get_bobas()[boba_choice - 1]
        correct_boba = order.get_boba()
        if boba_choice.get_name() == correct_boba:
            temp_profit += 20
            num_correct += 1
        
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # check if there are any toppings
        if len(m_inventory.get_toppings()) == 0 or order.get_toppings() == "no toppings":
            # clear screen
            os.system('cls' if os.name == 'nt' else 'clear')

            color_print(f'You got {num_correct} out of 2 correct. You earned ${num_correct * 20}.\n', 'g')
        else:
            print("Choose the correct toppings. ")
            for i in range(m_inventory.get_length("topping")):
                print(f'{i+1}. {m_inventory.get_toppings()[i].get_name()}')
            topping_choice = -1
            while int(topping_choice) not in range(m_inventory.get_length("topping") + 1):
                topping_choice = int(input())
            topping_choice = m_inventory.get_toppings()[topping_choice - 1]
            correct_topping = order.get_toppings()
            if topping_choice.get_name() == correct_topping:
                temp_profit += 20
                num_correct += 1

            color_print(f'You got {num_correct} out of 3 correct. You earned ${temp_profit}.\n', 'g')
        profit += temp_profit
        money += profit
    day_num += 1
    update_save_file(shop_name, money, day_num, m_shop, m_inventory)
    save_file = load_save_file(shop_name)
    
    # summarize end of day
    print("\n-------------------------------------------------------------")
    print("What a day...")
    print(f'You earned ${profit} today.')
    print(f'You have ${money} in total.')
    shop_choice = input("Would you like to buy new ingredients? (y/n) ")
    while shop_choice != 'y' and shop_choice != 'n':
        shop_choice = input("Would you like to buy new ingredients? (y/n) ")
    if shop_choice == 'y':
        update_save_file(shop_name, money, day_num, m_shop, m_inventory)
        buy_new_ingredients(shop_name, day_num, m_shop, m_inventory)

def main():
    print("***THIS IS NEW***")
    intro()
    color_print("Welcome to your new life as a boba shop owner!", 'g')
    shop_name = False
    while shop_name == False:
        print("What would you like to name your shop?")
        shop_name = sanitize_input_string()
    
    # check if save file exists
    if not os.path.exists(f'{shop_name}.json'):
        initialize_save_file(shop_name)

    # plays game
    run_day(shop_name)
    cont = 'y'
    while cont != 'n':
        cont = input("Would you like to play through the next day? (y/n) ")
        if cont == 'n':
            # clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            cat()
            print("Thanks for playing! Hope you had fun :)")
            break
        elif cont == 'y':
            run_day(shop_name)
        else:
            color_print("Invalid input. Please enter 'y' or 'n'.", 'r')
            continue

if __name__ == '__main__':
    main()