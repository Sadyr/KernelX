print('Please type you login and password...')
username = input()
password = input()
db = open('db.txt', 'r')

for uline in db.readlines():
    ulines = uline.split(':')
    print(ulines)
    if ulines[0] == username:
        print('This is username have db')
        for pline in db.readlines():
            plines = pline.split(':')
            print(plines)
            if plines[1] == password:
                print('Correctly is passowrd')
            else:
                print('errt')

# if username in db.read():
#     line = db.read()
#     print(line.split())
#     print('username have in db')
# else:
#     print('error')
