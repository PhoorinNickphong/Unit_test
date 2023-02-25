from program.fizz_buzz import fizz_buzz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_3_in_FizzBuzz(self): # Testing the fizz_buzz function with input 3
        self.assertEqual(fizz_buzz(3), 'Fizz')

    def test_5_in_FizzBuzz(self): # Testing the fizz_buzz function with input 5
        self.assertEqual(fizz_buzz(5), 'Buzz')
    
    def test_18_in_FizzBuzz(self): #test with number that is divisible by 3
        self.assertEqual(fizz_buzz(9), 'Fizz')
    
    def test_20_in_FizzBuzz(self): #test with number that is divisible by 5
        self.assertEqual(fizz_buzz(10), 'Buzz')
