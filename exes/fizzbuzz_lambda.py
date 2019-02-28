# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:02:29 2019

@author: f556085
"""

from functools import reduce

buzz_fizz = lambda x: "Fizz" * ( x % 3 == 0) + "Buzz" *( x % 2 == 0) or str(x)
string_newline_from_list = lambda x,y: x + "\n" + y
resultado = reduce(string_newline_from_list, map(buzz_fizz, range(101)))
print(resultado)