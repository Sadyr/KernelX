username = 'svet'
password = '1234l5'
user_db = 'user.txt'


def get_existing_users():
    with open(user_db,'r') as user_dba:
        for line in user_dba.readlines():
            # This expects each line of a file to be (name, pass) separated by white space
            username, password = line.split()
            yield username, password


# def is_authorized(username, password):
# return any(user == (username, password) for user in get_existing_users())

# def user_exists(username):
#     return any((usr_name == username) for usr_name, _ in get_existing_users())
# #
# for i in get_existing_users():
#     if username == i[0]:
#         print(i[1])
#         break
#     else:
#         continue
def is_authorized(username, password):
    for user in get_existing_users():
        user_name, pass_word = user
        if username == user_name and password == pass_word:
            authorizide = True
            break
        else:
            authorizide = False
            continue
    return authorizide


if is_authorized(username, password):
    print('user exists')
else:
    print('user not found')


def user_exists(username):
    for user in get_existing_users():
        user_name, _ = user
        if username == user_name:
            authorizide = True
            break
        else:
            authorizide = False
            continue
    return authorizide


print(user_exists(username))

def choice_menu():
    choice = str(input('Please choice point. If want authorized, enter "a", if want registration, enter "r". For exit enter "q"'))
    if choice.lower() == 'a':
        start_aut()
    #if choice.lower() == 'r':
        #user_registration()
    if choice.lower() == 'q':
        exit()

def ask_user_credentials():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password"))
    return name, password

def start_aut():
    username, password = ask_user_credentials()
    if user_exists():
        if is_authorized(username,password):
            print('Success aut')
        else:
            print('Incorrect password')
    else:
        print('user don"t found')
