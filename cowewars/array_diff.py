# a =
# b =
#
# for el in a:
#     #print(el)
#     for j in b:
#         #print(j)
#         if j == el:
#             a.remove(el)
#             b.remove(j)
# print(a)
#


# if x[0] in y:
#     print('yes')
# else:
#     print('sss')
#
# for el in b:
#     for i in a:
#         if el == i:
#             a.remove(el)
#         else:
#             continue
# print(a)
#
#
#
#
# print(a)
a = [1,2,2]
b = [2]
# def array_diff(a, b):
#     for el in a:
#         for jel in b:
#             if el == jel:
#                 a.remove(el)
#     for el in a:
#         for jel in b:
#             if el == jel:
#                 a.remove(el)
#     return a
# print(array_diff(a,b))


for i in range(len(b)):
    for j in a:
        if b[i] == a[j]:
            del a[j]
print(a)

