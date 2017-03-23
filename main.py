import requests

api_token = ""  # this is a global variable that stores the API token
group_number = -1
group_data = []

#TODO: Encrypt Token
""" This involves getting api token from user, encrypt it, and save in a file.
Should check if file contains encrypted key and prompt user if not.
"""

#Prompts user to input developer API key
def get_api_token():
    global api_token

    api_token = str(raw_input("Enter your GroupMe developer API token:"))

#Prints all of a user's groupme groups
def print_groups():

    response = requests.get('https://api.groupme.com/v3/groups?token=' + api_token)
    data = response.json()
    while data['response'] is None:
        print "Invalid API Key!"
        get_api_token()
        response = requests.get('https://api.groupme.com/v3/groups?token=' + api_token)
        data = response.json()
    if len(data['response']) == 0:
        print("You are not part of any groups.")
        return
    print("Here are your ten most recent groups:")
    for i in range(len(data['response'])):
        group = data['response'][i]['name']
        print(str(i)+". "+"\'"+group+"\'")
    global groups_data
    groups_data = data

#TODO: Menu
""" Menu invloves displaying all of the different pages of options for user input.
The exact content of the pages is explained in the high level design document.
"""
def menu():
    get_group_number()
    group_id = get_group_id(groups_data, group_number)

""" get_group_number retrieves the group number. It uses recursion to prompt user
to input until a valid input is given.
"""
def get_group_number():
    try:
        global group_number
        group_number = int(raw_input("Enter the number of the group you would like to analyze:"))
        if not ( 0<= group_number <= 9 ) :
            print("Not a valid integer")
            get_group_number()
    except ValueError:
        print("Not an integer")
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
    print_groups()
    menu()
