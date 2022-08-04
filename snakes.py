# imports reptile class which in turn inherits the animal class
from reptiles import Reptile


class Snakes(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.__scales = 10

    def tongue_smell(self):
        return "you smell nice :) "

    # protected module '_'
    def _move(self):
        return "slithers"

    # private module '__'
    def __hiss(self):
        return "hello"


p3 = Snakes()
try:
    print(p3.__hiss())
except AttributeError:
    print("this is information is protected or hidden")




# print(p3.forked_tongue)
# print(p3.tongue_smell())
# print(p3.seek_heat())
# print(p3.sleep())
#
# # You can access from anywhere it is just notation to developers to not touch it
#
#print(p3._move())
#print(p3._Snakes__hiss())
# print(p3._Snakes__scales)
# p3._Snakes__scales = 15
# print(p3._Snakes__scales)
#print(p3._Reptile__hunt())

#  what types of errors have we seen so far
#  syntax error
#  identation error, value errors, attribute errors,