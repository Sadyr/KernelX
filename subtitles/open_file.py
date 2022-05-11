import sys
sys.stdout = open('file.txt', 'w')
reader = open('seb.srt', 'r')

def clear_line(lines):
    wrong = "!@#$1234567890-,.>\t\n:;[]"
    for char in wrong:
        lines = lines.replace(char,'')
    return lines

try:
    #print(reader.read()) # прочитать весь файл
    for i in reader:
        line = i
        lin = clear_line(line)
        if len(lin) > 2:
            print(lin)
        else:
            continue
finally:
    reader.close()
print(len('  '))
sys.stdout.close()

