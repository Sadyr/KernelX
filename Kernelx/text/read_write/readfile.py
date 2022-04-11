# reader = open('dog.txt', 'r')
# try:
#     for i in reader.read():
#         print(i)
# finally:
#     reader.close()

with open('test.txt', 'w', encoding ='utf-8') as f:
    f.write('my firts file\n')
    f.write('This file\n')
    f.write('contains three lines\n')
f = open('test.txt', 'r', encoding='utf-8')
# print(f.read())

for line in f:
    print(line, end='')

