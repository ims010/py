
# have a HELP command
# have a SHOW command
# clean code up in general

# make a list to hold onto our items
# shopping_list = []


# def show_help():
#     # print out instructions on how to use the app
#     print("Pass for now")
#     print("""
# Enter 'DONE' to stop adding items.
# Enter 'HELP' to get more help.
# Enter 'SHOW' to see your current list.
# """)


# def add_to_list(new_item):
#     shopping_list.append(new_item)
#     print("Added {}. List now has {} items".format(new_item, len(shopping_list)))


# def show_list():
#     for item in shopping_list:
#         print(item)


# show_help()

# while True:
#     # ask for new items
#     new_item = input("> ")
#     # be able to quit the app
#     if new_item == "DONE":
#         print("Here's your list: ")
#         break
#     elif new_item == "HELP":
#         show_help()
#         continue
#     elif new_item == 'SHOW':
#         show_list()
#         continue
#     add_to_list(new_item)

# show_list()


# ----------------------- EXTENDED----------------------------
# Adding an item to a speific index.


# import os
# shopping_list = []


# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def show_help():
#     clear_screen()
#     # print out instructions on how to use the app
#     print("Pass for now")
#     print("""
# Enter 'DONE' to stop adding items.
# Enter 'HELP' to get more help.
# Enter 'SHOW' to see your current list.
# """)


# def add_to_list(new_item):
#     show_list()
#     if len(shopping_list):
#         position = input(" Where should I add {}?\n"
#                          "Press ENTER to add to the end of list \n"
#                          ">".format(new_item))
#     else:
#         position = 0

#     try:
#         position = abs(int(position))
#     except ValueError:
#         position = None
#     if position is not None:
#         shopping_list.insert(position - 1, new_item)
#     else:
#         shopping_list.append(new_item)

#     # shopping_list.append(new_item)
#     # print("Added {}. List now has {} items".format(new_item, len(shopping_list)))
#     show_list()


# def show_list():
#     clear_screen()
#     print('Here\'s your list: ')
#     index = 1
#     for item in shopping_list:
#         print('{}. {}'.format(index, item))
#         index += 1

#     print('-' * 10)


# show_help()

# while True:
#     # ask for new items
#     new_item = input("> ")
#     # be able to quit the app
#     if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
#         print("Here's your list: ")
#         break
#     elif new_item.upper() == "HELP":
#         show_help()
#         continue
#     elif new_item.upper() == 'SHOW':
#         show_list()
#         continue
#     else:
#         add_to_list(new_item)

# show_list()


# ----------------------- EXTENDED----------------------------
# Removing an item from a speific index.


# import os
# shopping_list = []


# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def show_help():
#     clear_screen()
#     # print out instructions on how to use the app
#     print("Welcome to Your Shopping List")
#     print("""
# Enter 'DONE' to stop adding items.
# Enter 'HELP' to get more help.
# Enter 'SHOW' to see your current list.
# Enter 'REMOVE' to delete an item from the list.
# """)


# def add_to_list(new_item):
#     show_list()
#     if len(shopping_list):
#         position = input(" Where should I add {}?\n"
#                          "Press ENTER to add to the end of list \n"
#                          ">".format(new_item))
#     else:
#         position = 0

#     try:
#         position = abs(int(position))
#     except ValueError:
#         position = None
#     if position is not None:
#         shopping_list.insert(position - 1, new_item)
#     else:
#         shopping_list.append(new_item)

#     # shopping_list.append(new_item)
#     # print("Added {}. List now has {} items".format(new_item, len(shopping_list)))
#     show_list()


# def show_list():
#     clear_screen()
#     print('Here\'s your list: ')
#     index = 1
#     for item in shopping_list:
#         print('{}. {}'.format(index, item))
#         index += 1

#     print('-' * 10)


# def remove_from_list():
#     show_list()
#     what_to_remove = input("What would you like to remove? \n> ")
#     try:
#         shopping_list.remove(what_to_remove)
#     except ValueError:
#         pass
#     show_list()


# show_help()

# while True:
#     # ask for new items
#     new_item = input("> ")
#     # be able to quit the app
#     if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
#         print("Here's your list: ")
#         break
#     elif new_item.upper() == "HELP":
#         show_help()
#         continue
#     elif new_item.upper() == 'SHOW':
#         show_list()
#         continue
#     elif new_item.upper() == 'REMOVE':
#         remove_from_list()
#     else:
#         add_to_list(new_item)

# show_list()


# ----------------------- EXTENDED----------------------------
# Removing an item using pop() 
# pop() returns to display the item which was removed. None of other methods, del and remove will return the removed items. Also good to know which item is being removed from list


# import os
# shopping_list = []


# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def show_help():
#     clear_screen()
#     # print out instructions on how to use the app
#     print("Welcome to Your Shopping List")
#     print("""
# Enter 'DONE' to stop adding items.
# Enter 'HELP' to get more help.
# Enter 'SHOW' to see your current list.
# Enter 'REMOVE' to delete an item from the list.
# """)


# def add_to_list(new_item):
#     show_list()
#     if len(shopping_list):
#         position = input(" Where should I add {}?\n"
#                          "Press ENTER to add to the end of list \n"
#                          ">".format(new_item))
#     else:
#         position = 0

#     try:
#         position = abs(int(position))
#     except ValueError:
#         position = None
#     if position is not None:
#         shopping_list.insert(position - 1, new_item)
#     else:
#         shopping_list.append(new_item)

#     # shopping_list.append(new_item)
#     # print("Added {}. List now has {} items".format(new_item, len(shopping_list)))
#     show_list()


# def show_list():
#     clear_screen()
#     print('Here\'s your list: ')
#     index = 1
#     for item in shopping_list:
#         print('{}. {}'.format(index, item))
#         index += 1

#     print('-' * 10)


# def remove_from_list():
#     show_list()
#     what_to_remove = input("What would you like to remove the recently added item? Y/n \n> ").lower()
#     removed = shopping_list.pop()
#     print('{}, was removed from your list'. format(removed))
#     # try:
#     #     removed = shopping_list.pop()
#     #     print('{}, was removed from your list'. format(removed))
#     # except ValueError:
#     #     pass
#     # show_list()

#     # IndexError will pop up if the list is empty you are trying to pop item, we can use try and except block to catch the IndexErrror and display no items in the shopping list.

# show_help()

# while True:
#     # ask for new items
#     new_item = input("> ")
#     # be able to quit the app
#     if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
#         print("Here's your list: ")
#         break
#     elif new_item.upper() == "HELP":
#         show_help()
#         continue
#     elif new_item.upper() == 'SHOW':
#         show_list()
#         continue
#     elif new_item.upper() == 'REMOVE':
#         remove_from_list()
#     else:
#         add_to_list(new_item)

# show_list()


# ----------------------- EXTENDED----------------------------
# Using enumerate()

import os
shopping_list = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    clear_screen()
    # print out instructions on how to use the app
    print("Welcome to Your Shopping List")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to get more help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from the list.
""")


def add_to_list(new_item):
    show_list()
    if len(shopping_list):
        position = input(" Where should I add {}?\n"
                         "Press ENTER to add to the end of list \n"
                         ">".format(new_item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, new_item)
    else:
        shopping_list.append(new_item)

    # shopping_list.append(new_item)
    # print("Added {}. List now has {} items".format(new_item, len(shopping_list)))
    show_list()


def show_list():
    clear_screen()
    print('Here\'s your list: ')
    for index, item in enumerate(shopping_list, start=1):
        print('{}. {}'.format(index, item))

    print('-' * 10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove the recently added item? Y/n \n> ").lower()
    removed = shopping_list.pop()
    print('{}, was removed from your list'. format(removed))
    # try:
    #     removed = shopping_list.pop()
    #     print('{}, was removed from your list'. format(removed))
    # except ValueError:
    #     pass
    # show_list()

    # IndexError will pop up if the list is empty you are trying to pop item, we can use try and except block to catch the IndexErrror and display no items in the shopping list.


show_help()

while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        print("Here's your list: ")
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()
