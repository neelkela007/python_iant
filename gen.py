def demo():
    # for i in demo:
    #     return i 
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    yield 11
    yield 12
    yield 13
    yield 14
    yield 15
    yield 16
    yield 17
    yield 18
    yield 19 
    yield 20
    yield 21
    yield 22
    yield 23
    yield 24
    yield 25
    yield 26
    yield 27
    yield 28
    yield 29
    yield 30
    
obj = demo()

for i in obj:
    print(i)

# lst = [1,2,3,4,5]
# a = filter(lambda z: z%2 != 0, lst)
# for i in a:
#     print(i)

# import sys

# sys.setrecursionlimit(3000)

# def x(n):
#     if n == 1:
#         return 1
#     else:
#         return n * (x(n-1))

# # 3 * x(3-1) --> 2 * x(2-1) --> 1
# # 1 --> 2 * 1 = 2 --> 3 * 2 = 6

# p = x(5)
# print(p)

# 3 --> 3,2,1

# def p(n):
#     if n == 1:
#         return 1
#     else:
#         print(p(n-1)) # p(n-1)

# p(5)
#  print(l)
