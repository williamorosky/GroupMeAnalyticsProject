import requests
import Menu as menu
from EncryptionHandler import EncryptionHandler

api_token = ""  # this is a global variable that stores the API token

#Prompts user to input developer API key if one not already saved
def get_api_token():
    global api_token
    global data
    encryption_handler = EncryptionHandler()
    api_token = str(encryption_handler.token)
    print("")
    response = requests.get('https://api.groupme.com/v3/groups?token=' + api_token)
    menu.data = response.json()
    if menu.data['response'] is None:
        print "Invalid API Key!"
        get_api_token()


#Main function. First thing that is called.
if __name__ == '__main__':
    print('If you have not done so already, go to the following website to receive your API token: ' +
          'https://dev.groupme.com/. When signing up, it does not matter what you put for the callback URL')
    get_api_token()
    menu.api_token = api_token
    menu.display_menu()
