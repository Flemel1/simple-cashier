menus = []


def insert_menu():
    user_input = input("Insert Your Menu: ")
    menus.append(user_input.title())

def print_menu():
    if (len(menus) == 0):
        print("Menu is empty, insert at least 1 menu")
    else:
        for index, food in enumerate(menus):
            print(f'{index + 1}. {food}')

def remove_menu():
    for index, food in enumerate(menus):
        print(f'{index + 1}. {food}')
    
    user_input = int(input(f'Choose your food to remove 1 - {len(menus)}: '))

    while user_input > len(menus):
        print("Your Chouse Is Wrong!!")
        user_input = int(input(f'Choose your food to remove 1 - {len(menus)}: '))

    menus.pop(user_input - 1)
    print('Your food is removed!')

def menu():
    state = 1
    while state != 0:
        print("Choose: ")
        print("0. Exit")
        print("1. Input Menu")
        print("2. Remove Menu")
        print("3. Print Menu")
        user_input = int(input("Choose Your Input 1 - 3: "))

        if user_input == 1:
            insert_menu()
        elif user_input == 2:
            remove_menu()
        elif user_input == 3:
            print_menu()
        elif user_input == 0:
            state = 0
        else :
            print("Your choose not found")

menu()

print("Good Bye See You Again!")