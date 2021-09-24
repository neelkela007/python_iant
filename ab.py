from abc import ABC, abstractclassmethod

class a(ABC):
    @abstractclassmethod # decorator
    def n(self):
        pass

    @abstractclassmethod
    def shakur(self):
        pass

class b(a):
    def n(self):
        print("i am from n")

    def shakur(self):
        pass

obj = b()
obj.n()
obj.shakur()