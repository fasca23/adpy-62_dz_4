from flatIterator import FlatIterator
from flatgenerator import flat_generator
from tests import *
from recursion import smooth
from data import *


test_1(FlatIterator)

test_2(flat_generator)

test_3(smooth)

# for i in FlatIterator(list_of_lists_1):
#     print(i)
    
# for i in flat_generator(list_of_lists_1):
#     print(i)

for i in smooth(list_of_lists_2):
    print(i)
