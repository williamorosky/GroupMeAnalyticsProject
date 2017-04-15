group_number = -1
group_id = []
groups_data = []
data = []

def get_group_number():
    try:
        print_groups()
        global group_number
        num = int(raw_input("Enter the number of the group you would like to analyze: "))
        if num==10:
            print("")
            menu()
        else:
            group_number = num
        if not ( 0<= group_number <= 9 ) :
            print("Not a valid integer")
            get_group_number()
    except ValueError:
        print("\nNot an integer")
        get_group_number()

def get_group_id(groups_data, group_number):

    group_id = groups_data['response'][group_number]['id']
    return group_id


def get_group_option():
    try:
        print_group_options()
        choice = int(raw_input("Enter the number: "))
        print("")
        if 1<= choice <= 9 :
            return choice
        else:
            print("Not a valid integer\n")
            return get_group_option()
    except ValueError:
        print("\nNot an integer\n")
        return get_group_option()

def get_group_option_more():
    try:
        print_group_options_more()
        choice = int(raw_input("Enter the number: "))
        print("")
        if 1<= choice <= 16 :
            return choice
        else:
            print("Not a valid integer\n")
            return get_group_option_more()
    except ValueError:
        print("\nNot an integer\n")
        return get_group_option_more()

def get_person_option():
    try:
        print_person_options()
        choice = int(raw_input("Enter the number: "))
        print("")
        if 1<= choice <= 9 :
            return choice
        else:
            print("Not a valid integer\n")
            return get_person_option()
    except ValueError:
        print("\nNot an integer\n")
        return get_person_option()

def get_person_option_more():
    try:
        print_person_options_more()
        choice = int(raw_input("Enter the number: "))
        print("")
        if 1<= choice <= 9 :
            return choice
        else:
            print("Not a valid integer\n")
            return get_person_option_more()
    except ValueError:
        print("\nNot an integer\n")
        return get_person_option_more()

def print_person_options():
    options1=[
    'Number of messages sent all time',
    'Total likes given all time',
    'Total likes received all time',
    'Average likes received per message all time',
    'Most popular word of all time',
    'Most liked message',
    'More options',
    'Group Specific Statistics',
    'Back' ]
    print("Which statistic would you like to retreive?")
    for i in range(len(options1)):
        print(str(i+1)+". "+"\'"+options1[i]+"\'")

def print_person_options_more():
    options1=[
        'Self likes of all time',
        'Total likes received all time (with self likes subtracted)',
        'Total words sent all time',
        'Number of pictures sent all time',
        'Number of videos sent all time',
        'Most liked message - Text all time',
        'Most liked message - Picture all time',
        'Most liked message - Video all time',
        'Back'
    ]
    print("More options")
    print("Which statistic would you like to receive?")
    for i in range(len(options1)):
        print(str(i+1)+". "+"\'"+options1[i]+"\'")

def print_group_options():
    options1=[
    'Your number of messages sent',
    'Your total likes given',
    'Your total likes received',
    'Your average likes received per message',
    'Your most popular word',
    'Your most liked message',
    'More options',
    'Person Specific Statistics',
    'Back'
    ]
    print_group_name()
    print("Which statistic would you like to retreive?")
    for i in range(len(options1)):
        print(str(i+1)+". "+"\'"+options1[i]+"\'")

def print_group_options_more():
    options1=[
    'Self-likes',
    'Total likes received (with self likes subtracted)',
    'Total words sent',
    'Number of pictures sent',
    'Number of videos sent',
    'Most liked message - Text',
    'Most liked message - Picture',
    'Most liked message - Video',
    'Number of likes received from each member of group',
    'Percent of each member\'s total likes that went to a particular member',
    'Number of times you liked the same post as another member',
    'Most "popular" person',
    'Least "popular" person',
    'What time of day is the groupme most active',
    'Group\'s most popular word',
    'Back'
    ]
    print("More options for " + data['response'][group_number]['name'])
    print("Which statistic would you like to retreive?")
    for i in range(len(options1)):
        print(str(i+1)+". "+"\'"+options1[i]+"\'")
""" get_group_number retrieves the group number. It uses recursion to prompt user
to input until a valid input is given.
"""
def print_person_or_group():
    print("Which type of statistic would you like to retrieve?")
    print("1 - Group Specific Statistics")
    print("2 - Person Specific Statistics")

#function that displays groups and retrieves group data
#Prints all of a user's groupme groups
def print_groups():

    if len(data['response']) == 0:
        print("You are not part of any groups.")
        return
    print("Here are your ten most recent groups:")
    for i in range(len(data['response'])):
        group = data['response'][i]['name']
        print(str(i)+". "+"\'"+group+"\'")
    print("10. Back")
    global groups_data
    groups_data = data

def get_person():

    choice = get_person_option()
    if choice==1:
        #Number of messages sent all time
        donothing=0
    elif choice==2:
        #Total likes given all time
        donothing=0
    elif choice==3:
        #Total likes received all time
        donothing=0
    elif choice==4:
        #Average likes received per message all time
        donothing=0
    elif choice==5:
        #Most popular word of all time
        donothing=0
    elif choice==6:
        #Most liked message
        donothing=0
    elif choice==7:
        #More options
        get_person_more()
    elif choice==8:
        #Group Specific Statistics
        get_groups()
    elif choice==9:
        #Back to menu
        menu()

def get_groups():
    choice = get_group_option()
    if choice==1:
        #Your number of messages sent
        donothing=0
    elif choice==2:
        #Your total likes given
        donothing=0
    elif choice==3:
        #Your total likes received
        donothing=0
    elif choice==4:
        #Your average likes received per message
        donothing=0
    elif choice==5:
        #Your most popular word
        donothing=0
    elif choice==6:
        #MYour most liked message
        donothing=0
    elif choice==7:
        #More options
        get_groups_more()
    elif choice==8:
        #Person Specific Statistics
        get_person()
    elif choice==9:
        #Back to menu
        group()

def group():
    choose_which_group()
    get_groups()

def choose_which_group():
    get_group_number()
    group_id = get_group_id(groups_data, group_number)

def get_person_more():

    choice = get_person_option_more()
    if choice==1:
        #Self likes of all time
        donothing=0
    elif choice==2:
        #Total likes received all time (with self likes subtracted)
        donothing=0
    elif choice==3:
        #Total words sent all time
        donothing=0
    elif choice==4:
        #Number of pictures sent all time
        donothing=0
    elif choice==5:
        #Number of videos sent all time
        donothing=0
    elif choice==6:
        #Most liked message - Text all time
        donothing=0
    elif choice==7:
        #Most liked message - Pic all time
        donothing=0
    elif choice==8:
        #Most liked message - Video all time
        donothing=0
    elif choice==9:
        #Back to previous options
        get_person()

def print_group_name():
    print("\n"+data['response'][group_number]['name'])

def get_groups_more():
    choice = get_group_option_more()
    if choice==1:
        #Self-likes
        donothing=0
    elif choice==2:
        #Total likes received (with self likes subtracted)
        donothing=0
    elif choice==3:
        #Total words sent
        donothing=0
    elif choice==4:
        #Number of pictures sent
        donothing=0
    elif choice==5:
        #Number of videos sent
        donothing=0
    elif choice==6:
        #Most liked message - Text
        donothing=0
    elif choice==7:
        #Most liked message - Pic
        get_groups_more()
    elif choice==8:
        #Most liked message - Video
        get_person()
    elif choice==9:
        #Number of likes received from each member of group
        donothing=0
    elif choice==10:
        #Percent of each member\'s total likes that went to a particular member
        donothing=0
    elif choice==11:
        #Number of times you liked the same post as another member
        donothing=0
    elif choice==12:
        #Most "popular" person
        donothing=0
    elif choice==13:
        #Least "popular" person
        donothing=0
    elif choice==14:
        #What time of day is the groupme most active
        donothing=0
    elif choice==15:
        #Group\'s most popular word
        donothing=0
    elif choice==16:
        #Back
        get_groups()

#function that prompts user to choose between person and group statistics
#true means they chose group, false means they chose person
def chose_group():
    try:
        print_person_or_group()
        choice = int(raw_input("Enter the number of the type of statistic: "))
        if choice==1:
            print("")
            return True
        elif choice==2:
            print("")
            return False
        else:
            print("Not a valid integer\n")
            return chose_group()
    except ValueError:
        print("\nNot an integer\n")
        return chose_group()
