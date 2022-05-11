# Опеартор +
# s = 'foo'
# t = 'bar'
# u = 'baz'
# print(s+t+u)

# Оператор in
# s = 'foo'
# print('That\'s food for thought.')
# print(s in 'That\'s food for thought.')

# Оператор not
# z = 'a'
# print(z not in 'xyz')

# Метод len(s)
# s = 'I am a string'
# print(len(s))

# Метод str - Возвращает строковое представление объекта.
# s = 555.5
# print(type(str(s)))

# Индексация строк
# s = 'foobar'
# print(s[0])
# print(s[1])
# print(s[3])
# print(len(s))
# print(s[len(s)-1])

# f-строки
# n = 20
# m =25
# prod = n * m
# print(f'The product of {n} and {m} is {prod}')

# Преоброзование
# s.capitalize - Делает целевую строку заглавной.
# s= 'foO BaR BAZ quX'
# print(s.capitalize())

# s.lower - Преобразует буквы алфавита в нижний регистр.
# s = 'FOO Bar 123 baz qUX'
# print(s.lower())

# s.swapcase() - Меняет регистр букв.
# s = 'FOO Bar 123 baz qUX'
# print(s.swapcase())

# s.title() - Преобразует целевую строку в «заглавный регистр».
# s = 'the sun also rises'
# print(s.title())

# s.upper() - s.upper()
# s = 'FOO Bar 123 baz qUX'
# print(s.upper())

# s.count(<sub>[, <start>[, <end>]]) - Подсчитывает количество вхождений подстроки в целевой строке.
# s = 'foo goo moo'
# print(s.count('oo'))
# print(s.count('oo', 0, 8))

# s.endswith(<suffix>[, <start>[, <end>]]) - Определяет, заканчивается ли целевая строка заданной подстрокой.
# s= 'foobar'
# print(s.endswith('bar'))
# print(s.endswith('baz'))

# s.find(<sub>[, <start>[, <end>]]) - Ищет в целевой строке заданную подстроку.
# s = 'foo bar foo baz foo qux'
# print(s.find('foo'))
# print(s.find('sadyr'))

# s.rfind(<sub>[, <start>[, <end>]]) - Ищет в целевой строке заданную подстроку, начиная с конца.
# s = 'foo bar foo baz foo qux'
# print(s.rfind('foo'))
# print(s.rfind('sadyr'))

# # s.startswith(<prefix>[, <start>[, <end>]]) - Определяет, начинается ли целевая строка с заданной подстроки.
# s = 'foobar'
# print(s.startswith('foo'))

# Классификация персонажей - Определяет, состоит ли целевая строка из буквенно-цифровых символов.
# s.isalnum()
# s = 'abc123'
# print(s.isalnum())

# s.isalpha() - Определяет, состоит ли целевая строка из буквенных символов.
# s = 'ABCabc'
# print(s.isalpha())

# s.isdigit() Определяет, состоит ли целевая строка из цифровых символов.
# s= '123a'
# print(s.isdigit())

# s.islower() - Определяет, являются ли буквенные символы целевой строки строчными.

# s = 'abc'
# print(s.islower())

# s.isspace() - Определяет, состоит ли целевая строка из пробельных символов.
# Наиболее часто встречающиеся пробельные символы — пробел ' ', табуляция '\t'и перевод строки '\n':
# s = ' \t \n'
# print(s.isspace())

# s s.istitle() - Определяет, является ли целевая строка заглавной.
# s= 'This Is A Title'
# print(s.istitle())

# s.isupper() - Определяет, являются ли буквенные символы целевой строки прописными.
# s = 'ABC'
# print(s.isupper())


# a = "a!b@c#d$"
# b = "!@#$"
# for char in b:
#     print(char)
#     a = a.replace(char, "")
#
# print(a)


# def clear_line(line):
#     wrong = "!@#$1234567890--> \t\n:;[]"
#
#     for char in wrong:
#         line = line.replace(char,'')
#     return line
# line = '00:00:47,881 --> 00:00:49,757'
# print(clear_line(line))


lines = 'sadyr amidala kf kkk kk k'
lines2 = 'sadyr amidala kf kkk kk k'
main_list = []

def word_to_second_list(lines):
    second_list = lines.split()
    return (second_list)

def list_to_main_list(main_list,second_list):
    for el in second_list:
        main_list.append(el.lower())
    return (main_list)

second_list = word_to_second_list(lines)

main_list= (list_to_main_list(main_list,second_list))
print(main_list)
main_set = set(main_list)
print(main_set)
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
print(count_wort_in_sub(main_set,main_list, main_dict))






