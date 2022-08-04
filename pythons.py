from snakes import Snakes


# creates a class for pythons
class Pythons(Snakes):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        # redefine the forked tongue attribute for the python
        self.forked_tongue = False

    def climb(self):
        return "climb"

    def shed_skin(self):
        return "shed_skin"

    #  redefine the hunt for python
    def hunt(self):
        return "digest large prey"


# creates object
p4 = Pythons()

# shows test cases
print(p4.forked_tongue)
print(p4.hunt())
print(p4.climb())
