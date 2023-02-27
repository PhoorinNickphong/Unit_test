from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
   def test_give_1_2_3_is_prime(self):
     prime_list = [1, 2, 3]
     is_prime = is_prime_list(prime_list)
     self.assertTrue(is_prime)
   def test_give_2_3_5_is_prime(self):
     prime_list = [2, 3, 5]
     is_prime = is_prime_list(prime_list)
     self.assertTrue(is_prime)
   def test_give_2_2_2_is_prime(self):
     prime_list = [2, 2, 2]
     is_prime = is_prime_list(prime_list)
     self.assertTrue(is_prime)
   def test_give_2_4_6_is_prime(self):
     prime_list = [5,7,8]
     is_prime = is_prime_list(prime_list)
     self.assertFalse(is_prime)
   def test_give_907_23_83_is_prime(self):
      prime_list = [4, 5, 6]
      is_prime = is_prime_list(prime_list)
      self.assertFalse(is_prime)