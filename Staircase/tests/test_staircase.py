from program import staircase
import unittest


class StaircaseTest(unittest.TestCase):
    def test_given_4_with_hash_should_be_hh(self):
        n = 4
        printed_sym = "#"
        expected_result = "   #\n" + "  ##\n" + " ###\n" + "####"

        result = staircase.staircase(n)

        self.assertEqual(len(expected_result.split("\n")), n)
        self.assertIn(printed_sym, expected_result)
        self.assertEqual(result, expected_result)

