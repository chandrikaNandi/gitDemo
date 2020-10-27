class Calculator:
    num = 50  # it is class variable can be used globally in a class

    # create a constructor
    # it will call automatically when a object of the class is created, object don't have to call constructor
    def __init__(self, a, b):  # self is only a obj reference. it is default for every method in class
        self.firstnum = a  # this is instance variable. for every input value instance variable is changed
        self.lastnum = b  # this is also instance variable
        print("i am a default constructor, i will come when a object of the class is created")

    def indata(self):
        print("i am executing a class")

    def sumofnum(self):
        return self.firstnum + self.lastnum + Calculator.num   # self.num can also be written as it is an object reference

# 'new' keyword is not required when we create an object
obj = Calculator(2, 4)  # syntax of creating a new object of class
obj.indata()
print(obj.sumofnum())

obj1 = Calculator(5, 7)  # we can create as many as object for same class
#  obj1.indata()
print(obj1.firstnum)
print(obj1.lastnum)
print(obj1.num)