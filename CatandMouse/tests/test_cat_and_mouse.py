from program.cat_and_mouse import cat_and_mouse

import unittest

class TestCatMouse(unittest.TestCase):
    def test_1_2_3_in_CatMouse(self): 
        result = cat_and_mouse(1,2,3)
        self.assertEqual(result, 'Cat B')
    def test_1_3_2_in_CatMouse(self): 
        result = cat_and_mouse(1,3,2)
        self.assertEqual(result, 'Mouse C')
    def test_2_1_4_in_CatMouse(self): 
        result = cat_and_mouse(2,1,4)
        self.assertEqual(result, 'Cat A')
    def test_1_2_8_in_CatMouse(self): 
        result = cat_and_mouse(1,2,8)
        self.assertEqual(result, 'Cat B')

