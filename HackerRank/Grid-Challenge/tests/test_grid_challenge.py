from program.grid_challenge import gridChallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_exampleList_1_to_grid(self):
        lst = ['eabcd','fghij','olkmn','trpqs','xywuv']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_2_to_grid(self):
        lst = ['mpxz','abcd','wlmf']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output , f'Shoud be {expected_output}')

    def test_give_exampleList_3_to_grid(self):
        lst = ['zzzzzwz','zzzzzzw','wzzzzzz','zzwzzzz','zzyzzzz','zzzzyzz','zzzzzyz']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_4_to_grid(self):
        lst = ['rpb','hot','qra']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

