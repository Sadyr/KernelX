PASSWORD_FRAME = "user_data.txt"

def get_existing_users():
    with open('r', PASSWORD_FRAME) as fp:
        for line in fp.readlines():
            # This expects each line of a file to be (name, pass) separated by white space
            username, password = line.split()
            yield username, password

def is_authorized(username, password):
    return any(user == (username, password) for user in get_existing_users())

def user_exists(username):
    return any((usr_name == username) for usr_name, _ in get_existing_users())
# above is equilent of :
#
# for usr_name, _ in get existing_users():
#   if usr_name == username:
#   return True
# return False

def ask_user_credentials():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password"))
    return name, password
def checkdetails():
    name, password = ask_user_credentials()
    if is_authorized(name,password):
        return "Welcome Back,  "+ name
    if user_exists(name):
        return "Password enterd is wrong"
    return "Name not found. Please Sign UP."

def getdetails():
    name, password = ask_user_credentials()
    if not user_exists(name):
        return "Name unavailable. Pleas Try again"
