from program.FunnyString  import funnyString

import unittest

class TestFunnyString(unittest.TestCase):
    def test_acxz_in_FunnyString(self):
        x = 'acxz'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
    def test_bcxz_in_FunnyString(self):
        x = 'bcxz'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')
    def test_zxca_in_FunnyString(self):
        x = 'zxca'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
    def test_lmnop_in_FunnyString(self):
        x = 'lmnop'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
    def test_loop_in_FunnyString(self):
        x = 'loop'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')

#nose2 --with-coverage