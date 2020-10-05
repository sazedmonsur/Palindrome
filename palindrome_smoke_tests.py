from palindrome_check import is_plaindrome
import unittest


class PalindromeSmokeTests(unittest.TestCase):
    def test_shouldReturnTrueWhenPalindromeEvenCharacters(self):
        self.assertEqual(is_plaindrome("diid"), True)

    def test_shouldReturnTrueWhenPalindromeOddCharacters(self):
        self.assertEqual(is_plaindrome("did"), True)

    def test_shouldReturnTrueWhenPalindromeUpperOrLowerCase(self):
        self.assertEqual(is_plaindrome("Did"), True)

    def test_shouldReturnTrueWhenPalindromeMultipleWords(self):
        self.assertEqual(is_plaindrome("A nut for a jar of tuna"), True)

    def test_shouldReturnTrueWhenPalindromeMultipleWordsWithSpacesSpecialCharacters(self):
        self.assertEqual(is_plaindrome("   Murder??? for a jar of red rum!!!  "), True)

    def test_shouldReturnFalseWhenNotPalindrome(self):
        self.assertEqual(is_plaindrome("Not"), False)

    def test_shouldReturnFalseForEmptyString(self):
        self.assertEqual(is_plaindrome(""), False)

    def test_shouldReturnFalseForWhiteSpaceString(self):
        self.assertEqual(is_plaindrome(" "), False)

    def test_shouldReturnFalseForLongWhiteSpaceString(self):
        self.assertEqual(is_plaindrome("                                       "), False)

    def test_shouldReturnTrueForOneCharacter(self):
        self.assertEqual(is_plaindrome("L"), True)

    def test_shouldReturnFalseForSpecialCharactersOnly(self):
        self.assertEqual(is_plaindrome("??@#$"), False)