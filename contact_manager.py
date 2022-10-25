###
### Author: Kevin Cascais Nisterenko
### Course: CSc 110
### Description: My program/solution for Contact Manager PA - Week 14.
###              This program reads in a .txt file and with contacts and loads
###              them as tuples in a set that the program then performs actions
###              (show contacts, add contacts or exit the program) depending on user
###              input. To this end, 5 functions are defined. The load_contacts
###              function uses a for loop to read through the lines of the 'contacts.txt'
###              text file and store it into a set of tuples where every tuple contains
###              strings that represent a person's name, email and phone number in this
###              order. The function then returns this set. The show_contacts function
###              then takes this set and user input (command) as parameters and first
###              performs string slicing with an if-elif-elif block depending on what type
###              of contact information the user is performing the search on. Then the
###              function uses a for loop with that specified aspect (name, email or phone)
###              that iterates through all tuples and stores all matching tuples in another
###              set. Then, another for loop is used in an ordered version of the matching
###              set and it uses an if-else statement to print all contacts that have the
###              specified aspect in the output or print none if there are no matches. The
###              add_contact function also takes the contacts_set as a parameter and it
###              first gets user input for name, email and phone of the new contact and
###              creates a tuple with these strings. Then, an if-else block is used to
###              check if this tuple was already in the contacts_set, if it was, the function
###              will print a 'already exists' message. If it wasn't in the set, this tuple
###              will then be added to the set and a 'contact added' message will be printed.
###              Regardless of adding or not, the function will then return the contacts_set
###              so that it will be updated to the program as a whole. The save_contacts
###              function runs only after the user decides to exit the program and it will
###              take the final contacts_set as a parameter and it uses a for loop that
###              iterates thorugh every tuple in an ordered version of contacts_set and
###              rewrites the contents into the 'contacts.txt' file. For the program to
###              function main is defined and called and it first calls the load_contacts
###              function to load in the set, then it prints the welcome message and asks
###              the user for first input. A while loop is then used and it has an
###              an if-elif-else that will decide if it will call the show_contacts function,
###              the add_contact function or print the 'Huh?' message depending on user input.
###              If the user types 'exit' the loop is then exited and it prints the goodbye
###              message as well as calling the save_contacts function to update the file so
###              that any new information can be accessed later even after the program is exited.
###

def main():
    contacts = load_contacts()

    print('Welcome to the contacts app!')

    command = input('>\n')

    # While the user command is not exit, it will continously ask
    # the user what command to perform or print the 'Huh?' message
    # if the command is not recognized. If the user input is 'exit',
    # it will exit the loop and stop the program altogether.
    while command != 'exit':
        if command.startswith('show contacts with'):
            show_contacts(contacts, command)
        elif command == 'add contact':
            add_contact(contacts)
        else:
            print('Huh?')
        command = input('>\n')

    print('Goodbye!')

    save_contacts(contacts)

def load_contacts():
    '''
    This function first initializes an empty set and opens the contacts file.
    Then, a for loop is used that iterates through every line in the contacts
    file and creates a tuple with name, email and phone of every line. This
    tuple is then added to the contacts_set. After the loop runs the function
    returns the contacts_set in which every element is a tuple and every element
    inside the tuple is a string representing name, email and phone in this
    respective order.
    '''
    # Initializes an empty set that will have all contacts as tuples.
    contacts_set = set()

    contacts_file = open('contacts.txt', 'r')

    # Iterates through every line in the contacts file and creates a tuple
    # with the contact information of the person in the line. Then it adds
    # the tuple to the set.
    for line in contacts_file:
        line = line.strip().split(' | ')
        # line[0] is the person's name, line[1] is the person's email and
        # line[2] is the person's phone number, all are strings.
        contact = (line[0], line[1], line[2])
        contacts_set.add(contact)

    contacts_file.close()

    return contacts_set

def show_contacts(contacts_set, command):
    '''
    This function first uses an if-elif-elif block to check what type of
    information the user wants to search contacts with (name, email or phone)
    and then assigns that information (name, email or phone) to the item variable.
    Then the empty matching_set is initialized and a for loop is used to iterate
    through every tuple in contacts_set and check if the given information is there,
    if it is, the tuple will be added to the matching_set. Then, an if-else is used
    to check if matching_set is empty or not, if it is empty, it will print the 'None'
    message. However, if there are items in the matching_set, a for loop that iterates
    through every tuple in an ordered matching_set is used to print the contact information
    correctly. This function does not have any returns.
    contacts_set: set in which every element is a tuple and every element
    inside the tuple is a string representing name, email and phone in this
    respective order.
    command: string that represents user command.
    '''
    # Checks what type of contact user command has given (name, email or phone)
    # and assigns it to the item variable which is used to check for matches.
    if 'name' in command:
        item = command[24:]
    elif 'email' in command:
        item = command[25:]
    elif 'phone' in command:
        item = command[25:]

    # Initializes an empty set that will have all matching contact tuples in it.
    matching_set = set()

    # Iterates through every tuple in contacts_set and checks if the item is in
    # the tuple, if it is, it will add that tuple to the matching_set.
    for contact_tuple in contacts_set:
        if item in contact_tuple:
            matching_set.add(contact_tuple)

    # Checks if there are matches by analyzing the length of the matching_set, if
    # there are matches, a for loop that iterates through a sorted version of
    # matching_set is used with print statements to print the contact information.
    if len(matching_set) == 0:
        print(None)
    else:
        for contact_tuple in sorted(matching_set):
            print(contact_tuple[0] + '\'s ' + 'contact info:')
            print('  email:', contact_tuple[1])
            print('  phone:', contact_tuple[2])

def add_contact(contacts_set):
    '''
    This function gets user input for the new contact's name, email and phone
    number and then uses those strings to create the new_contact tuple. This
    tuple is then added to the contacts_set if it is not already in contacts_set
    using an if-else statement, if the tuple was already in contacts_set, a message
    of already existing contact will be printed. The contacts_set is then returned to
    the program with this new contact (or unchanged if no new contact added).
    contacts_set: set in which every element is a tuple and every element
    inside the tuple is a string representing name, email and phone in this
    respective order.
    '''
    # Gets user input for each of the necessary contact information.
    name = input('name:\n')
    email = input('email:\n')
    phone = input('phone:\n')

    # Creates a tuple with the given contact information.
    new_contact = (name, email, phone)

    # Adds the tuple to the contacts_set if it is not already there,
    # if it is, it will print the 'already exists' message.
    if new_contact not in contacts_set:
        contacts_set.add(new_contact)
        print('Contact added!')
    else:
        print('Contact already exists!')

    # It returns contacts_set because it has changed because of the function.
    return contacts_set

def save_contacts(contacts_set):
    '''
    This function uses a for loop that iterates through every tuple in contacts_set
    and overwrites the contacts file with the information on an ordered version of
    contacts_set in the loop. This way, the file will essentially 'save' any new
    information that may have been added to the contacts_set during the program's
    run. This function does not have any returns.
    contacts_set: set in which every element is a tuple and every element
    inside the tuple is a string representing name, email and phone in this
    respective order.
    '''
    contacts_file = open('contacts.txt', 'w')

    # Iterates through every contact information tuple in an ordered version of
    # contacts_set and writes the information to the file.
    for contact_tuple in sorted(contacts_set):
        contacts_file.write(contact_tuple[0] + ' | ' + contact_tuple[1] + ' | ' +
                            contact_tuple[2] + '\n')

    contacts_file.close()

main()