from program.CatandMouse import CatAndMouse

import unittest

class TestCatAndMouse(unittest.TestCase):
    def test_give_1_2_3_to_cat_and_mouse(self):
        x,y,z = 1,2,3
        expected_output = "Cat B"
        result = CatAndMouse(x,y,z)
        self.assertEqual(expected_output, result)

    def test_give_1_3_2_to_cat_and_mouse(self):
        x,y,z = 1,3,2
        expected_output = "Mouse C"
        result = CatAndMouse(x,y,z)
        self.assertEqual(expected_output, result)
      
    def test_give_100_97_99_to_cat_and_mouse(self):
        x,y,z = 100,97,99
        expected_output = "Cat A"
        result = CatAndMouse(x,y,z)
        self.assertEqual(result, expected_output)
    
    def test_give_99_100_101_to_cat_and_mouse(self):
        x,y,z = 99,100,101
        expected_output = None
        result = CatAndMouse(x,y,z)
        self.assertEqual(result, expected_output)