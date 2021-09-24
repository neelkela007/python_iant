# class Person:
#     def __init__(self,name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")


# John = Person("John Smith")
# print(John.name)
# John.talk()

# Bob = Person("Bob Smith")
# Bob.talk()


i = 0
while i<=5:
    # print(i)
    i += 1
    if i == 3:
        continue
    else:
        print(i)
    # i = i + 1

else:
    print("Loop end")