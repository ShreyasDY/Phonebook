phonebook = {}

# Insert name and phone number
def insert_number(name, number):
    phonebook[name] = number
    print("Name and phone number added successfully.")

# Search phone number based on name
def search_number(name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Name not found."

# Update phone number based on name
def update_number(name, new_number):
    if name in phonebook:
        phonebook[name] = new_number
        print("Phone number updated successfully.")
    else:
        print("Name not found.")

# Delete name and phone number based on name
def delete_number(name):
    if name in phonebook:
        del phonebook[name]
        print("Name and phone number deleted successfully.")
    else:
        print("Name not found.")

# Test the functions
insert_number("Rajkumar", "123456789")
print(search_number("Rajkumar"))
update_number("Rajkumar", "0123456789")
print(search_number("Rajkumar"))
delete_number("Rajkumar")
print(search_number("Rajkumar"))
