#   Imports

from datetime import datetime
from default_user import Spy
from steganography.steganography import Steganography
from default_user import friend1, friend2


#    Initializations

friends = [friend1, friend2]  # Friend List, Initialized empty because no friends right now.
all_status = ['Available', 'On a mission', 'In meeting'] # 3 Default Statuses Provided.

#   CLASSES


class message:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.sent_by_me = sent_by_me
        self.time = datetime.now()
        self.length = 0

class BGcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#   FUNCTIONS


def validate_int(value):
    while not str.isdigit(value):
        value = raw_input("Please enter a number.")
    return int(value)


def validate_name(name):
    while len(name) == 0:
        name = raw_input("Cannot leave this field empty.\nEnter name again: ")
    while not str.isalpha(name):
        name = raw_input("Input only letters.\nEnter name again: ")
    while str.isspace(name):
        name = raw_input("Don't use space.\nEnter name again: ")


def validate_age(age):
    age = validate_int(age)
    while age > 50 or age <= 12:
        print "Incorrect Age."
        age = int(raw_input("In correct age value.\nEnter age again: "))
    return age


def validate_rating(rate):
    try:
        rate = float(rate)
        while rate >= 5.0:
            rate = float(raw_input("Incorrect rating value. \nEnter Rating again: "))
    except:
        rate = raw_input("enter again: ")
        validate_rating(rate)
    return rate


def add_status():
    choice = raw_input("Press 1 for new status and 2 for choosing from older ones.")
    choice = validate_int(choice)
    if choice == 1:
        spy_user.current_status = raw_input("Enter New Status: ")
        all_status.append(spy_user.current_status)
    elif choice == 2:
        count = 1
        for temp in all_status:
            print (str(count) + ". " + temp)
            count = count + 1
        choose_status = int(raw_input("Enter the no of status which you want to choose."))
        while choose_status > len(all_status):
            print len(all_status)
            choose_status = int(raw_input("Invalid value. Enter again: "))
        spy_user.current_status = all_status[choose_status - 1]
    else:
        print "Invalid Input."
        add_status()
    print "Status updated.\n Current Status - %s" % (spy_user.current_status)



def add_friends():
    friend_1 = Spy('', 0, 0.0)
    friend_1.name = raw_input("Friend's Name: ")
    validate_name(friend_1.name)
    friend_1.age = raw_input("Friend's Age: ")
    friend_1.age = validate_age(friend_1.age)
    friend_1.rating = raw_input("Friend's Rating: ")
    friend_1.rating = validate_rating(friend_1.rating)
    friends.append(friend_1)
    print "Friend added."


def select_friend():
    print"Select a friend to chat with."
    count = 1
    for temp in friends:
        print "%d. %s of age %d is online." % (count, temp.name, temp.age)
        count = count+1
    choose_friend = raw_input("Enter the no of friend you want to select.")
    validate_int(choose_friend)
    return choose_friend-1


def send_message():
    recipient = select_friend()
    new_msg = raw_input("Type your message.")
    filename = "DIP.jpg"
    out_img = raw_input("Name of image with encoded text: ")
    Steganography.encode(filename, out_img, new_msg)
    new_chat = message(new_msg, True)
    friends[recipient].chats.append(new_chat)
    print "Message sent."


def read_message():
    filename = raw_input("File you want to decode: ")
    try:
        new_msg = Steganography.decode(filename)
        print "Message is: %s" % new_msg
        if new_msg.find("SOS") > 0 or new_msg.find("Help me") > 0:
            print (BGcolors.WARNING + "Special Attention Required for this message." + BGcolors.ENDC)
        print "Append this message in chat?(Y/N)"
        choice = raw_input("")
        if choice.upper() == "Y":
            sender = select_friend()
            new_chat = message(new_msg, False)
            new_chat.length = len(new_msg)
            print new_chat.length
            if new_chat.length > 100:
                friends.remove(sender)
            else:
                friends[sender].chats.append(new_chat)
        else:
            print "Message not appended."
    except:
        print "No Message in image."


def read_chat_history():
    whose_history = select_friend()
    for temp in friends[whose_history].chats:
        if temp.sent_by_me:
            print ("[" + BGcolors.OKBLUE + str(temp.time) + BGcolors.ENDC + "]" + BGcolors.HEADER + " You Said: " + BGcolors.ENDC + temp.message)
        else:
            print ("[" + BGcolors.OKBLUE + str(temp.time) + BGcolors.ENDC + "]" + BGcolors.HEADER + friends[whose_history].name + " said: "+  BGcolors.ENDC + temp.message)


#   Execution will start from here.

spy_user = Spy('', 0, 0.0)
print("\n\tSpyChat\n")
print("Continue Anonymously/Default user or Create New user?")
user = raw_input("Press 1 for default user or 2 for new user.")
user = validate_int(user)
while user > 2 or user < 0:
    user = int(raw_input("Incorrect Input. Enter Again: "))
if user == 1:
    from default_user import spy_user
    print("Default User's Characteristics ")
    print("Name: %s\nAge: %d\nRating: %.1f" % (spy_user.name, spy_user.age, spy_user.rating))
else:
    # Creating New User.
    spy_user.name = raw_input("Name: ")
    validate_name(spy_user.name)
    spy_user.age = raw_input("Age: ")
    spy_user.age = validate_age(spy_user.age)
    spy_user.rating = raw_input("Ratings: ")
    spy_user.rating = validate_rating(spy_user.rating)
    if spy_user.rating > 4.5:
        print("That's Amazing, you're top class.")
    elif spy_user.rating > 3.5 and spy_user.rating <= 4.5:
        print("I can see you're good in what you do.")
    elif spy_user.rating > 2.5 and spy_user.rating <= 3.5:
        print("Man, you are doing great, keep at it.")
    else:
        print("Ah, you're a beginner.\nEvery Professional was once a beginner.")
while True:
    print("\n1. Add status update.\n2. Add a friend.\n3. Send a secret message.\n4. Read a secret message.\n5. Read Chat History.\n6. Exit")
    what_to_do = int(raw_input("Choose what you want to do. "))
    while type(what_to_do) != int or 0 < what_to_do > 6:
        what_to_do = int(raw_input("Incorrect Input. "))
    if what_to_do == 1:
        add_status()
    elif what_to_do == 2:
        add_friends()
    elif what_to_do == 3:
        send_message()
    elif what_to_do == 4:
        read_message()
    elif what_to_do == 5:
        read_chat_history()
    else:
        print("See you again.")
        break
