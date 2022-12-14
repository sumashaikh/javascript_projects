class ClassOne:
    def func1(self):
        print("we are in base class")

class ClassTwo(ClassOne):
    def func2(self):
        print("we are in child class")

obj = ClassTwo()
obj.func1()
obj.func2()        
