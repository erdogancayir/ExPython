class Classy:
    varia = 1
    c = 10
    def __init__(self):
        self.a = 5
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)