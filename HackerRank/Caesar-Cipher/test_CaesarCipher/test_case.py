from program.caesarCipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_abcdefghijklmnopqrstuvwxyz_in_caesarcipher(self):
        x = 'abcdefghijklmnopqrstuvwxyz'
        result = caesarCipher(x,3)
        self.assertEqual(result,'defghijklmnopqrstuvwxyzabc')
    def test_abcdefghijklmnopqrstuvwxyz_in2_caesarcipher(self):
        x = 'abcdefghijklmnopqrstuvwxyz'
        result = caesarCipher(x,2)
        self.assertEqual(result,'cdefghijklmnopqrstuvwxyzab')
    def test_middle_Outz_in_caesarcipher(self):
        x = 'middle_Outz'
        result = caesarCipher(x,11)
        self.assertEqual(result,'xtoowp_Zfek')
    def test_XO2XO0_in_caesarcipher(self):
        x = 'XO2XO0'
        result = caesarCipher(x,0)
        self.assertEqual(result,'XO2XO0')
    def test_Never_fall_in_love_in_caesarcipher(self):
        x = 'Never-fall-in-love'
        result = caesarCipher(x,5)
        self.assertEqual(result,'Sjajw-kfqq-ns-qtaj')
