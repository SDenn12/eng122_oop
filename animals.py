class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = None

    def sleep(self):
        return "zzz"

    def eat(self):
        return "yum"


p1 = Animal()
print(p1.sleep())
