from spy_details import spy_name,spy_age,spy_rating,spy_salutation
from stegnography.stegnography import Stegnography
from datetime import datetime

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

friends = []

print("Hello! Let\'s get started")

question = "Do you want to continue as " + spy_salutation['salutation'] + " " + spy_name['name'] + " (Y/N)? "
existing = input(question)


def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None
        print( 'Your current status message is %s \n' % (current_status_message)))
    else:
        print ('You don\'t have any status message currently \n')

    default = input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1


for message in STATUS_MESSAGES:
    print( '%d. %s' % (item_position, message))
    item_position = item_position + 1

message_selection = input("\nChoose from the above messages ")

if len(STATUS_MESSAGES) >= message_selection:
    updated_status_message = STATUS_MESSAGES[message_selection - 1]

else:
    print
'The option you chose is not valid! Press either y or n.'

if updated_status_message:
    print
    'Your updated status message is: %s' % (updated_status_message)
else:
    print
    'You did not update your status message'

return updated_status_message


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")

new_friend['rating'] = input("Spy rating?")

 if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print( 'Friend Added!')
    else:
        print ('Sorry! Invalid entry. We can\'t add spy with the details you provided')
return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print( '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'], friend['age'], friend['rating']))
        item_number = item_number + 1

    friend_choice = input("Choose from your friends")

    friend_choice_position = friend_choice - 1

    return friend_choice_position

def send_message():

    friend_choice = select_a_friend()

    original_image = input("What is the name of the image?")
    output_path = "output.jpg"
    text = input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }


friends[friend_choice]['chats'].append(new_chat)

print("Your secret message image is ready!")


def read_message():
    sender = select_a_friend()

    output_path = input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)

    print( "Your secret message has been saved!")


def start_chat(spy):
    current_status_message = None

    spy['name'] = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 50:

        print("Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str( spy['rating']) + " Proud to have you onboard")

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)

            # Set status
            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print('You have %d friends' % (number_of_friends))
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            else:
                show_menu = False
    else:
        print('Sorry you are not of the correct age to be a spy')


if existing == "Y":
    start_chat(spy)
else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = input("Should I call you Mr. or Ms.?: ")

        spy['age'] = input("What is your age?")

        spy['rating'] = input("What is your spy rating?")

        spy['is_online'] = True

        start_chat(spy)
    else:
        print('Please add a valid spy name')
