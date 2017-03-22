import requests

api_token = ""  # this is a global variable that stores the API token
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

    if data['response'] is None:
        print "Invalid API Key!"
    else:
        if len(data['response']) == 0:
            print("You are not part of any groups.")
            return
        for i in range(len(data['response'])):
            group = data['response'][i]['name']
            print(str(i)+". "+"\'"+group+"\'")
        group_data = data

#TODO: Menu
""" Menu invloves displaying all of the different pages of options for user input.
The exact content of the pages is explained in the high level design document.
"""

#Statistics Functions

#TODO: Get people in a group

#TODO: Get data for single person

#TODO: Calculate statistics given data

#Main function. First thing that is called.
if __name__ == '__main__':
    get_api_token()
    #print_groups()
