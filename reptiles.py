from animals import Animal


#create reptile class
class Reptile(Animal):  # write the name of the parent class in () to inherit
    # parent class - base class - super class (same thing)
    def __init__(self):
        # have to let it know to inherit everything from parent class
        super().__init__()
        self.cold_blooded = True
        self.heart_chambers = [3,4]

    # creates the functions
    def seek_heat(self):
        return "looking for the sun shine"

    def __hunt(self):
        return "working hard to catch a next meal"


# p2 = Reptile()
# print(p2.sleep())
# print(p2.hunt())
# print(p2.cold_blooded)
# print(p2.alive)
