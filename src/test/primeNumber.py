#!/usr/bin/env python

class NegativeNumberException(Exception):
    def __init__(self, arg):
        self.msg = arg


class PrimeNumber:
    def isPrimeNumber(self, number):
        result = True
        if number < 0:
            raise NegativeNumberException('Error: Numero negativo')
        elif number < 2:
            result = False
        else:
            for i in xrange(number - 1, 1, -1):
                if ((number % i) == 0):
                    result = False
        return result
