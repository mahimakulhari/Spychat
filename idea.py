from spy_details import spy,friends,chatmessage,spy
from stegano import lsb
import csv
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_name():

    global spy_name, spy_name_length, spy_salutation, spy_salutation_length, spy_full_name
    spy_name = input(bcolors.WARNING + "Welcome to spy chat, you must tell me your spy name first: " + bcolors.ENDC)
    spy_name_length = len(spy_name)

    spy_salutation = input("Should I call you Mister or Miss?: ")
    spy_salutation_length = len(spy_salutation)

    spy_full_name = spy_salutation + " " + spy_name.capitalize() + " "
    while spy_name_length == 0 and spy_salutation_length == 0:
        print("Incorrect Values enter name and salutation again", end='\n')
        get_name()
    else:
        print(bcolors.WARNING+"Alright " + spy_full_name.capitalize() + " I'd like to know a little bit more about..."+bcolors.ENDC, end='\n')


def get_age(c_name,c_rating):

    global spy_age
    try:
        check_rating = float(input("Please enter your " + c_name + " rating between 0 to 5 : "))
        spy_rating = check_rating
    except Exception:
        print(bcolors.FAIL + "Rating not valid" + bcolors.ENDC, end='\nPlease try Again\n')
        get_rating(check_rating, c_name)
    return spy_rating


def show_error():
    global error
    error = True
    print(bcolors.WARNING + "Sorry You are not of the proper age to enter the spy community!" + bcolors.ENDC)


def check_age(c_age, check_rating, c_name):

    if 12 < c_age < 50:
        print("Valid " + c_name + ", Welcome!")
        check_rating = get_rating(check_rating, c_name)
        print(check_rating)
        if check_rating > 4.5:
            print('Great ace! ' + c_name)
        elif 3.5 < check_rating <= 4.5:
            print('You are one of the good ' + c_name)
        elif 2.5 <= check_rating <= 3.5:
            print('You can always do better ' + c_name)
        else:
            print('We can always use somebody to help you ' + c_name + ' in the office.')

    else:
        print(bcolors.WARNING + "Sorry You are not of the proper age to enter the " + c_name + " Community!\nEnter age bw "
                                                                                            "12 to 50" + bcolors.ENDC)
        get_age(c_name, check_rating)


def add_status():
    spy.current_status_message = input("Enter status: ")
    print("status updated")
    start_chat(spy_name, spy_age, spy_rating)


def view_status():
    print("Your status is " + str(spy.current_status_message))
    start_chat(spy_name, spy_age, spy_rating)


def add_friend():
    new_friend = spy(" ", " ", 0, 0.0)
    new_friend.name = input("Please add your friend's name: ")
    new_friend.salutation = input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(input("Age?"))
    check_age(c_age=new_friend.age, c_name="friend", check_rating=new_friend.rating)
    friends.append(new_friend)
    print('Friend Added!')

    print('You have %d friends' % len(friends))

    start_chat(spy_name, spy_age, spy_rating)


def read_message():
    output_path = input("What is the name of the file? \n (Press enter to read default secret file)")

    if len(output_path) == 0:
        secrettext = lsb.reveal("./secret.png")
    else:
        try:
            secrettext = lsb.reveal(output_path)
        except Exception:
            print(bcolors.WARNING + 'error exiting your entered output path invalid' + bcolors.ENDC)
            exit()
        print(bcolors.BOLD + "Your secret message is :" + str(secrettext) + bcolors.ENDC)
        if secrettext == 'SOS' or secrettext == 'SAVE ME':
            print(bcolors.WARNING + 'HELP is on the way sending backup' + bcolors.ENDC)
        start_chat(spy_name, spy_age, spy_rating)

    def select_a_friend():
        item_number = 0
        for friend in friends:
            print("%d. %s" % (item_number + 1, friend.name))
            item_number = item_number + 1

        ch = input("select friend index")

        friend_choice_position = int(ch) - 1

        return friend_choice_position

    def send_msg():
        ch = select_a_friend()
        text = input("What do you want to say? ")

        secret = lsb.hide("./input.png", text)
        output = input('Name of output file: \n (Press enter for default name)')
        if len(output) == 0:
            secret.save("./secret.png")
            print(bcolors.BOLD + "Your secret message image is ready! with file name 'secret.png' " + bcolors.ENDC)
        else:
            try:
                secret.save(output)
                print(bcolors.BOLD + "Your secret message image is ready! with file name " + output + bcolors.ENDC)
            except Exception:
                print(bcolors.WARNING + 'Please Enter valid extension' + bcolors.ENDC)
        new_chat = chatmessage(text, True)
    friends[ch].chats.append(new_chat)

    start_chat(spy_name, spy_age, spy_rating)


def exits():
    print(bcolors.BOLD+'Exiting, Hey don\'t forget to clear your secret image file and data'+bcolors.ENDC)
    exit(1)


def store_friends_data():
    try:
        with open('data.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in friends.items():
                writer.writerow([key, value])
    except Exception:
        print(bcolors.OKGREEN + 'error no chat data found \nYou need to chat send message first' + bcolors.ENDC)

    start_chat(spy_name, spy_age, spy_rating)


def view_friends_data():
    try:
        with open('data.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file)
            friends_data = dict(reader)
            print('Friends data ' + str(friends_data))
    except Exception:
        print(bcolors.WARNING+'Error no data in csv found'+bcolors.ENDC)

    start_chat(spy_name, spy_age, spy_rating)


def start_chat(name, age, rating):
    menu_choices = bcolors.FAIL + " What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message " \
                                     "\n 4. Read a secret message \n 5. View Status \n 6. Store Friends_Data \n 7. View Friends Data \n " \
                                     "8. Exit \n" + bcolors.ENDC

    ch = input(menu_choices)

    options = {
        1: add_status,
        2: add_friend,
        3: send_message,
        4: read_message,
        5: view_status,
        6: store_friends_data,
        7: view_friends_data,
        8: exits
    }
    options[int(ch)]()


if __name__ == '__main__':
    spy_name = spy.name
    spy_salutation = spy.salutation
    spy_age = spy.age
    spy_rating = spy.rating
    spy_is_online = spy.is_online
    print(bcolors.WARNING + 'Welcome to spy chat' + bcolors.ENDC)
    question = "Do you want to continue as " + spy_salutation + " " + spy_name +" (Y/N)? "
    existing = input(question)
    print(existing)
    if existing == "Y" or existing == "y":
        start_chat(spy_name, spy_age, spy_rating)
    else:
        spy_name = ''
        spy_salutation = ''
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False

        get_name()
        get_age("spy", c_rating=spy_rating)

        start_chat(spy_name, spy_age, spy_rating)