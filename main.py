import requests

api_token = ""  # this is a global variable that stores the API token
group_number = -1
groups_data = []
data = []

#TODO: Encrypt Token
""" This involves getting api token from user, encrypt it, and save in a file.
Should check if file contains encrypted key and prompt user if not.
"""

#Prompts user to input developer API key
def get_api_token():
    global api_token
    global data
    api_token = str(raw_input("Enter your GroupMe developer API token:"))
    print("")
    response = requests.get('https://api.groupme.com/v3/groups?token=' + api_token)
    data = response.json()
    if data['response'] is None:
        print "Invalid API Key!"
        get_api_token()

#Prints all of a user's groupme groups
def print_groups():

    if len(data['response']) == 0:
        print("You are not part of any groups.")
        return
    print("Here are your ten most recent groups:")
    for i in range(len(data['response'])):
        group = data['response'][i]['name']
        print(str(i)+". "+"\'"+group+"\'")
    global groups_data
    groups_data = data
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
    options2=[
        'Self likes of all time',
        'Total likes received all time (with self likes subtracted)',
        'Total words sent all time',
        'Number of pictures sent all time',
        'Number of videos sent all time',
        'Most liked message - Text all time',
        'Most liked message - Picture all time',
        'Most liked message - Gif all time',
        'Back'
    ]
    print("More options")
    print("Which statistic would you like to receive?")
    for i in range(len(options2)):
        print(str(i+1)+". "+"\'"+options2[i]+"\'")

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
        #Most liked message - Gif all time
        donothing=0
    elif choice==9:
        #Back to previous options
        get_person()

#TODO: Menu
""" Menu invloves displaying all of the different pages of options for user input.
The exact content of the pages is explained in the high level design document.
"""
def menu():

    if chose_group():
        get_groups()
    else :
        get_person()

""" get_group_number retrieves the group number. It uses recursion to prompt user
to input until a valid input is given.
"""
def print_person_or_group():
    print("Which type of statistic would you like to retrieve?")
    print("1 - Group Specific Statistics")
    print("2 - Person Specific Statistics")

#function that displays groups and retrieves group data
def get_groups():
    print_groups()
    get_group_number()
    group_id = get_group_id(groups_data, group_number)

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
def get_group_number():
    try:
        global group_number
        group_number = int(raw_input("Enter the number of the group you would like to analyze:"))
        if not ( 0<= group_number <= 9 ) :
            print("Not a valid integer")
            get_group_number()
    except ValueError:
        print("\nNot an integer")
        get_group_number()

def get_group_id(groups_data, group_number):

    group_id = groups_data['response'][group_number]['id']
    return group_id

#Statistics Functions

#TODO: Get people in a group

#TODO: Get data for single person

#TODO: Calculate statistics given data

#Main function. First thing that is called.
if __name__ == '__main__':
    print('If you have not done so already, go to the following website to receive your API token: ' +
          'https://dev.groupme.com/. When signing up, it does not matter what you put for the callback URL')
    get_api_token()
    menu()
