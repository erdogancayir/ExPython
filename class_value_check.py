class ex:
    def __init__(self, val):
        if (val % 2 == 0):
            self.b = 10
        else:
            self.a = 20
    
ex_object = ex(1)
print(ex_object.a)

#class icinde bu deger varmi diye kontrol eder varsa if e girer.
if (hasattr(ex_object, 'b')):
    print(ex_object.b)
 

#----------------------------------

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
