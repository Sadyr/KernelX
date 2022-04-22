def user_registration():
    print('Please provide me: ')
    username = str(input('Your username: '))
    password = str(input('Your password: '))
    repeat_password = str(input('Repeat password: '))
    if password != repeat_password:
        while password != repeat_password:
            print('Passwords not equivalent. Please repeate correctly password')
            repeat_password = str(input('repeat password'))
    u_p = username + ' ' + password + '\n'
    db_users = open('user.txt', 'a')
    db_users.write(u_p)
    db_users.close()
    print(f'Conglomerations {username}. Registrations success')


user_registration()





