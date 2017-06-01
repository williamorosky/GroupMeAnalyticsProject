import requests
import re
import sys
from collections import Counter

api_token = ""
group_number = -1
groups_data = []
global_group_id = 0
data = []
message_data = []
data_mapping = []

def display_menu():
    if chose_group():
        group()
    else :
        get_person()

def get_group_number():
    try:
        print_groups()
        global group_number
        num = int(raw_input("Enter the number of the group you would like to analyze: "))
        if num==10:
            print("")
            display_menu()
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

def get_members_option():
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
        pass
    elif choice==2:
        get_total_likes_given(data_mapping)
        get_groups()
    elif choice==3:
        get_total_likes_received(data_mapping)
        get_groups()
    elif choice==4:
        #Your average likes received per message
        get_likes_per_message(data_mapping)
        get_groups()
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
        get_people_in_group()
        get_person()
    elif choice==9:
        #Back to menu
        group()

def group():
    choose_which_group()
    get_groups()

def choose_which_group():
    get_group_number()
    global global_group_id
    global_group_id = get_group_id(groups_data, group_number)
    prepare_analysis_of_group(groups_data, global_group_id)

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

def get_group_members(groups_data, group_id):
    i = 0
    while True:
        if group_id == groups_data['response'][i]['group_id']:
            return groups_data['response'][i]['members']
        i += 1

def prepare_user_dictionary(members_of_group_data):
    user_dictionary = {}
    i = 0
    while True:
        try:
            user_id = members_of_group_data[i]['user_id']
            nickname = members_of_group_data[i]['nickname']
            user_dictionary[user_id] = [nickname, 0.0, 0.0, 0.0, 0.0, {}, {}, 0.0, []]
            # [0] = nickname, [1] = total messages sent in group, like count, [2] = likes per message,
            # [3] = average likes received per message, [4] = total words sent, [5] = dictionary of likes received from each member
            # [6] = dictionary of shared likes, [7] = total likes given, [8] = word dictionary

        except IndexError:  # it will reach here when it gets to the end of the members
            return user_dictionary
        i += 1
    return user_dictionary

def prepare_analysis_of_group(groups_data, group_id):
    # these three lines simply display info to the user before the analysis begins
    number_of_messages = get_number_of_messages_in_group(groups_data, group_id)

    #these two lines put all the members currently in the group into a dictionary
    members_of_group_data = get_group_members(groups_data, group_id)
    user_dictionary = prepare_user_dictionary(members_of_group_data)

    #this line calls the "analyze_group" method which goes through the entire conversation
    global data_mapping
    data_mapping = analyze_group(group_id, user_dictionary, number_of_messages)

def analyze_group(group_id, user_id_mapped_to_user_data, number_of_messages):
    response = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+api_token)
    data = response.json()
    message_with_only_alphanumeric_characters = ''
    message_id = 0
    iterations = 0.0
    while True:
        for i in range(20):  # in range of 20 because API sends 20 messages at once
            try:
                iterations += 1
                name = data['response']['messages'][i]['name']  # grabs name of sender
                message = data['response']['messages'][i]['text']  # grabs text of message
                #print(message)
                try:
                    #  strips out special characters
                    emoji_pattern = re.compile(
                        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
                        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
                        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
                        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
                        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
                        "+", flags=re.UNICODE)
                    if message is None :
                        message = ""
                    message_with_only_alphanumeric_characters = re.sub(r'\W+', ' ', str(message.lower()))
                    message_with_only_alphanumeric_characters = emoji_pattern.sub(r'', message_with_only_alphanumeric_characters)
                except ValueError:
                    pass  # this is here to catch errors when there are special characters in the message e.g. emoticons
                sender_id = data['response']['messages'][i]['sender_id']  # grabs sender id
                list_of_favs = data['response']['messages'][i]['favorited_by']  # grabs list of who favorited message
                length_of_favs = len(list_of_favs)  # grabs number of users who liked message

                #grabs the number of words in message
                number_of_words_in_message = len(re.findall(r'\w+', str(message_with_only_alphanumeric_characters)))
                word_array = re.findall(r'\w+', str(message_with_only_alphanumeric_characters))
                if sender_id not in user_id_mapped_to_user_data.keys():
                    user_id_mapped_to_user_data[sender_id] = [name, 0.0, 0.0, 0.0, 0.0, {}, {}, 0.0, []]

                #this if statement is here to fill the name in for the case where a user id liked a message but had
                #yet been added to the dictionary
                if user_id_mapped_to_user_data[sender_id][0] == '':
                    user_id_mapped_to_user_data[sender_id][0] = name

                for user_id in list_of_favs:
                    if user_id in user_id_mapped_to_user_data[sender_id][5].keys():
                        user_id_mapped_to_user_data[sender_id][5][user_id] += 1
                    else:
                        user_id_mapped_to_user_data[sender_id][5][user_id] = 1

                for user_id in list_of_favs:
                    for user_id_inner in list_of_favs:
                        if user_id not in user_id_mapped_to_user_data.keys():
                            # leave name blank because this means a user is has liked a message but has yet to be added
                            # to the dictionary. So leave the name blank until they send their first message.
                            user_id_mapped_to_user_data[user_id] = ['', 0.0, 0.0, 0.0, 0.0, {}, {}, 0.0,[]]
                        if user_id == user_id_inner:
                            user_id_mapped_to_user_data[user_id][7] += 1
                            continue  # pass because you don't want to count yourself as sharing likes with yourself
                        try:
                            user_id_mapped_to_user_data[user_id][6][user_id_inner] += 1
                        except KeyError:
                            user_id_mapped_to_user_data[user_id][6][user_id_inner] = 1

                user_id_mapped_to_user_data[sender_id][1] += 1  # add one to sent message count
                user_id_mapped_to_user_data[sender_id][2] += length_of_favs
                user_id_mapped_to_user_data[sender_id][4] += number_of_words_in_message
                user_id_mapped_to_user_data[sender_id][8].extend(word_array)

            except IndexError:
                for key in user_id_mapped_to_user_data:
                    try:
                        user_id_mapped_to_user_data[key][3] = user_id_mapped_to_user_data[key][2] / user_id_mapped_to_user_data[key][1]
                    except ZeroDivisionError:  # for the case where the user has sent 0 messages
                        user_id_mapped_to_user_data[key][3] = 0
                return user_id_mapped_to_user_data

        if i == 19:
                message_id = data['response']['messages'][i]['id']
                remaining = iterations/number_of_messages
                remaining *= 100
                remaining = round(remaining, 2)
                print(str(remaining)+' percent done')

        payload = {'before_id': message_id}
        response = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+api_token, params=payload)
        data = response.json()

def get_number_of_messages_in_group(groups_data, group_id):
    i = 0
    number_of_messages = 0
    while True:
        if group_id == groups_data['response'][i]['group_id']:
            number_of_messages = groups_data['response'][i]['messages']['count']
            print("Analyzing " + str(number_of_messages) + " messages")
            return groups_data['response'][i]['messages']['count']
        i += 1

def get_most_popular_word_in_group(user_id_mapped_to_user_data):
    word_list = []
    for key in user_id_mapped_to_user_data:
        word_list.extend(user_id_mapped_to_user_data[key][8])
    boring_words = ['the', 'a', 'I', 'i', 't', 'none', 's', 'to', 'an', 'and', 'if', 'in', 'None', 'are', 'that', 'is', 'that', 'do', 'it', 'we', 'you','of', 'me', 'on', 'this', 'they', 'my', 've', 'for', 'm', 'your', 'just', 'can', 'all', 'will', 'be', 'was', 'there', 'then', 'com', 'at', 'what', 'http', 'https', 'll', 'so', 'with', 'have']
    word_list = [x for x in word_list if x not in boring_words]
    words_to_count = Counter(word for word in word_list).most_common(5)
     
    print('TOP 5 Most Common Words')
    if(len(words_to_count)>4):
        print('1. ' + str(words_to_count[0][0]))
        print('2. ' + str(words_to_count[1][0]))
        print('3. ' + str(words_to_count[2][0]))
        print('4. ' + str(words_to_count[3][0]))
        print('5. ' + str(words_to_count[4][0]))
        print ""
        print ""

def get_likes_per_message(user_id_mapped_to_user_data):
    leaderboard = []
    for key in user_id_mapped_to_user_data:
        leaderboard.append((user_id_mapped_to_user_data[key][0],(user_id_mapped_to_user_data[key][3])))
     
    print('Likes per Message Leaderboard')
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    for i,person in enumerate(leaderboard):
        name = person[0]
        emoji_pattern = re.compile(
                        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
                        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
                        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
                        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
                        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
                        "+", flags=re.UNICODE)
        name = emoji_pattern.sub(r'', name)
        print(str(i+1) + ". " + str(name) + " - " + str(person[1]))

def get_total_likes_received(user_id_mapped_to_user_data):
    leaderboard = []
    for key in user_id_mapped_to_user_data:
        leaderboard.append((user_id_mapped_to_user_data[key][0],(user_id_mapped_to_user_data[key][2])))
     
    print('Total Likes Leaderboard')
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    for i,person in enumerate(leaderboard):
        name = person[0]
        emoji_pattern = re.compile(
                        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
                        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
                        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
                        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
                        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
                        "+", flags=re.UNICODE)
        name = emoji_pattern.sub(r'', name)
        print(str(i+1) + ". " + str(name) + " - " + str(person[1]))

def get_total_likes_given(user_id_mapped_to_user_data):
    leaderboard = []
    for key in user_id_mapped_to_user_data:
        leaderboard.append((user_id_mapped_to_user_data[key][0],(user_id_mapped_to_user_data[key][7])))
     
    print('Total Likes Given Leaderboard')
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    for i,person in enumerate(leaderboard):
        name = person[0]
        emoji_pattern = re.compile(
                        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
                        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
                        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
                        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
                        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
                        "+", flags=re.UNICODE)
        name = emoji_pattern.sub(r'', name)
        print(str(i+1) + ". " + str(name) + " - " + str(person[1]))

def get_self_likes(user_id_mapped_to_user_data):
    leaderboard = []
    for key in user_id_mapped_to_user_data:
        try:
            leaderboard.append((user_id_mapped_to_user_data[key][0],(user_id_mapped_to_user_data[key][5][key])))
        except KeyError:
            leaderboard.append((user_id_mapped_to_user_data[key][0],(0)))

     
    print('Total Self-Likes Leaderboard')
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    for i,person in enumerate(leaderboard):
        name = person[0]
        emoji_pattern = re.compile(
                        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
                        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
                        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
                        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
                        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
                        "+", flags=re.UNICODE)
        name = emoji_pattern.sub(r'', name)
        print(str(i+1) + ". " + str(name) + " - " + str(person[1]))

def get_groups_more():
    choice = get_group_option_more()
    if choice==1:
        get_self_likes(data_mapping)
        get_groups_more()
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
        pass
    elif choice==8:
        #Most liked message - Video
        pass
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
        get_groups_more()
    elif choice==15:
        #Group\'s most popular word
        get_most_popular_word_in_group(data_mapping)
        get_groups_more()
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
