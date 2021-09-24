# from functools import reduce

# lst = [1, 2, 3, 4, 5]

# a = filter(lambda x: x%2==0, lst)

# for i in a:
#     print(i)

# b = reduce(lambda p, x: p*x, [1,2,3, 4])

# # for i in b:
# #     print(i)
# print(b)

def a():
    yield 10
    yield 20
    yield 30
    yield 40


x = a()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

for i in x:
    print(i)