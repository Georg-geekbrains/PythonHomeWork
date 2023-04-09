

def add_contact():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    phone_number = input("Enter phone number: ")
    with open('phone_book.txt', 'a') as infile:
        infile.write(f"{last_name}, {first_name}, {middle_name}, {phone_number}\n")

def show():
    with open('phone_book.txt', 'r') as infile:
        for line in infile:
            print(line.strip())

def search():
    search_item = input("Enter search item: ")
    with open('phone_book.txt', 'r') as infile:
        for line in infile:
            if search_item in line:
                print(line.strip())

def edit():
    old_name = input("Enter name to edit: ")
    new_name = input("Enter new name: ")
    with open('phone_book.txt', 'r') as infile:
        lines = infile.readlines()
    with open('phone_book.txt', 'w') as infile:
        for line in lines:
            if old_name in line:
                infile.write(line.replace(old_name, new_name))
            else:
                infile.write(line)

def delete():
    name = input("Enter name to delete: ")
    with open('phone_book.txt', 'r') as infile:
        lines = infile.readlines()
    with open('phone_book.txt', 'w') as infile:
        for line in lines:
            if name not in line:
                infile.write(line)

def menu():
    while True:
        choice = input("Menu:\n1. Add_contact\n2. Show contacts\n3. Search contacts\n4. Edit contact\n5. Delete contact\n6. Quit\nEnter choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            show()
        elif choice == '3':
            search()
        elif choice == '4':
            edit()
        elif choice == '5':
            delete()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

menu()
