print('Please type you login and password...')
username = input()
password = input()
db = open('db.txt', 'r')
logic = 0

for i in db.readlines():
    ulines = i.split(':')
    if ulines[0] == username:
        logic = logic + 1
        db2 = open('db.txt', 'r')
        for j in db2.readlines():
            jlines = j.split(':')
            if jlines[1] == password + '\n':
                logic = logic + 1
                break
        if logic == 2:
            print('Welcome ...')
            break
        else:
            continue
    else:
        continue
if logic != 2:
    print('Incorrect username or password')





# if username in db.read():
#     line = db.read()
#     print(line.split())
#     print('username have in db')
# else:
#     print('error')
