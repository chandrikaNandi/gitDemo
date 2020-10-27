from PythonBasics.democlass import Calculator  # importing parent class in child class


class TryInheritance(Calculator):  # calling parent class in child class

    num2 = 200  # child class variable

    def __init__(self):
        Calculator.__init__(self, 5, 10)  # if parent constructor is default then we don't have to call and initiate it.
#                                 but if constructor use any code in parent class the it should be call in child class.

    def childmethod(self):
        return TryInheritance.num2 + TryInheritance.num + TryInheritance.sumofnum(self)
        # for TryInheritance.sumofnum(self), can't use TryInheritance.sumofnum() or we can write self.sumofnum()


obj = TryInheritance()

print(obj.childmethod())

