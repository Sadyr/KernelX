username = 'svet'
password = '12345'
user_db = open('user.txt', 'r')

def get_existing_users():
        for line in user_db.readlines():
            # This expects each line of a file to be (name, pass) separated by white space
            username, password = line.split()
            yield username, password

def is_authorized(username, password):
    return any(user == (username, password) for user in get_existing_users())

print(is_authorized(username,password))
