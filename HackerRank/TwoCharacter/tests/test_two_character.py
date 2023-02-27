from program.two_character import twoCharacter

import unittest

class TestTwoCharacter(unittest.TestCase):
    def test_give_beabeefeab_to_two_character(self):
        text = 'beabeefeab'
        expected_output = 5
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')


    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_to_two_character(self):
        text = "asdcbsdcagfsdbgdfanfghbsfdab"
        expected_output = 8
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_asvkugfiugsalddlasguifgukvsa_to_two_character(self):
        text = "asvkugfiugsalddlasguifgukvsa"
        excecpted_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, excecpted_output, f'Should be {excecpted_output}')

    def test_give_ab_to_two_character(self):
        text = 'ab'
        expected_output = 2
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_longtext_187_to_two_character(self):
        text = 'tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi'
        expected_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
