import sys
sys.stdout = open('file_count.txt', 'w')
reader = open('e2.srt', 'r')

def clear_line(lines):
    wrong = "/!@#$1234567890-?\",.>\t\n:;[]"
    for char in wrong:
        lines = lines.replace(char,'')
    return lines
def word_to_second_list(lines):
    second_list = lines.split()
    return (second_list)

def list_to_main_list(main_list,second_list):
    for el in second_list:
        main_list.append(el.lower())
    return (main_list)

try:
    #print(reader.read()) # прочитать весь файл
    main_list = []
    for i in reader:
        line = i
        lin = clear_line(line)
        if len(lin) > 2:
            lin = lin
            second_list = word_to_second_list(lin)
            main_list = list_to_main_list(main_list,second_list)
        else:
            continue
finally:
    reader.close()
# for i in main_list:
#     print(i)
main_set = set(main_list)
# c = 0
# for i in main_set:
#     print(i)
#     c = c + 1
# print(c)
#
main_dict = {}
def count_wort_in_sub(main_set,main_list, main_dict):
    for element_set in main_set:
        count = 0
        for element_list in main_list:
            if element_set == element_list:
                count = count + 1
            else:
                continue
        #print(element_set, count)
        main_dict[element_set] = str(count)
    return main_dict
main_dict = count_wort_in_sub(main_set,main_list, main_dict)
# print(main_dict)
for i in main_dict:
    print(i,main_dict[i])
sys.stdout.close()
