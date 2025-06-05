# Shopping List Manager
'''
Utilize Python lists to create a simple shopping list manager that allows users 
to add items, view the current list, and remove items
'''

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")



def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter the item to add: ")

        if choice == '1':
            # Prompt for and add an item
            item = input('Enter an item of your choice: ')
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            if shopping_list != []:
                shopping_list.pop(-1)
            else:
                print('Shopping list is empty')
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

