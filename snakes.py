# imports reptile class which in turn inherits the animal class
from reptiles import Reptile


class Snakes(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.__scales = 10

    def tongue_smell(self):
        return "you smell nice :) "

    def seek_heat(self):
        return "i am plenty warm :) "

    # protected module '_'
    def _move(self):
        return "slithers"

    # private module '__'
    def __hiss(self):
        return "hello"


# p3 = Snakes()
# print(p3.forked_tongue)
# print(p3.tongue_smell())
# print(p3.seek_heat())
# print(p3.sleep())
#
# # You can access from anywhere it is just notation to developers to not touch it
#
# print(p3._move())
# print(p3._Snakes__hiss())
# print(p3._Snakes__scales)
# p3._Snakes__scales = 11
# print(p3._Snakes__scales)
# print(p3._Reptile__hunt())
