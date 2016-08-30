#!/usr/bin/env python

import unittest
from primeNumber import PrimeNumber
from primeNumber import NegativeNumberException


class TestprimeNumber(unittest.TestCase):

    def setUp(self):
        self.testPrimeNumber = PrimeNumber()

    def testFirstPrimeNumber(self):
        self.assertEquals(True, self.testPrimeNumber.isPrimeNumber(2))

    def testSecondPrimeNumber(self):
        self.assertEquals(True, self.testPrimeNumber.isPrimeNumber(3))

    def testThirdPrimeNumber(self):
        self.assertEquals(True, self.testPrimeNumber.isPrimeNumber(5))

    def testFourthPrimeNumber(self):
        self.assertEquals(True, self.testPrimeNumber.isPrimeNumber(7))

    def testFifthPrimeNumber(self):
        self.assertEquals(True, self.testPrimeNumber.isPrimeNumber(11))

    def testTwentySixthPrimeNumber(self):
        self.assertEquals(True, self.testPrimeNumber.isPrimeNumber(101))

    def testNumberZeroNotPrime(self):
        self.assertEquals(False, self.testPrimeNumber.isPrimeNumber(0))

    def testNumberOneNotPrime(self):
        self.assertEquals(False, self.testPrimeNumber.isPrimeNumber(1))

    def testNumberFourNotPrime(self):
        self.assertEquals(False, self.testPrimeNumber.isPrimeNumber(4))

    def testNegativeNumberExceptionThrow(self):
        self.assertRaises(NegativeNumberException, self.testPrimeNumber.isPrimeNumber,-1)

    def tearDown(self):
        del self.testPrimeNumber

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestprimeNumber)
    unittest.TextTestRunner(verbosity=2).run(suite)