import unittest

from fizzbuzzwoofbang import FizzBuzzWoofBangFactory

class TestFizzBuzz(unittest.TestCase):

    def test_1_should_be_1(self):
        expected = '1'
        actual = FizzBuzzWoofBangFactory().create().say(1)
        self.assertEqual(expected, actual)

    def test_3_should_be_Fizz(self):
        expected = 'Fizz'
        actual = FizzBuzzWoofBangFactory().create().say(3)
        self.assertEqual(expected, actual)

    def test_5_should_be_Buzz(self):
        expected = 'Buzz'
        actual = FizzBuzzWoofBangFactory().create().say(5)
        self.assertEqual(expected, actual)

    def test_7_should_be_Woof(self):
        expected = 'Woof'
        actual = FizzBuzzWoofBangFactory().create().say(7)
        self.assertEqual(expected, actual)

    def test_11_should_be_Bang(self):
        expected = 'Bang'
        actual = FizzBuzzWoofBangFactory().create().say(11)
        self.assertEqual(expected, actual)

    def test_15_should_be_FizzBuzz(self):
        expected = 'FizzBuzz'
        actual = FizzBuzzWoofBangFactory().create().say(15)
        self.assertEqual(expected, actual)

    def test_21_should_be_FizzWoof(self):
        expected = 'FizzWoof'
        actual = FizzBuzzWoofBangFactory().create().say(21)
        self.assertEqual(expected, actual)

    def test_33_should_be_FizzBang(self):
        expected = 'FizzBang'
        actual = FizzBuzzWoofBangFactory().create().say(33)
        self.assertEqual(expected, actual)

    def test_35_should_be_BuzzWoof(self):
        expected = 'BuzzWoof'
        actual = FizzBuzzWoofBangFactory().create().say(35)
        self.assertEqual(expected, actual)

    def test_55_should_be_BuzzBang(self):
        expected = 'BuzzBang'
        actual = FizzBuzzWoofBangFactory().create().say(55)
        self.assertEqual(expected, actual)

    def test_77_should_be_WoofBang(self):
        expected = 'WoofBang'
        actual = FizzBuzzWoofBangFactory().create().say(77)
        self.assertEqual(expected, actual)

    def test_105_should_be_FizzBuzzWoof(self):
        expected = 'FizzBuzzWoof'
        actual = FizzBuzzWoofBangFactory().create().say(105)
        self.assertEqual(expected, actual)

    def test_165_should_be_FizzBuzzBang(self):
        expected = 'FizzBuzzBang'
        actual = FizzBuzzWoofBangFactory().create().say(165)
        self.assertEqual(expected, actual)

    def test_231_should_be_FizzWoofBang(self):
        expected = 'FizzWoofBang'
        actual = FizzBuzzWoofBangFactory().create().say(231)
        self.assertEqual(expected, actual)

    def test_385_should_be_BuzzWoofBang(self):
        expected = 'BuzzWoofBang'
        actual = FizzBuzzWoofBangFactory().create().say(385)
        self.assertEqual(expected, actual)

    def test_1155_should_be_FizzBuzzWoofBang(self):
        expected = 'FizzBuzzWoofBang'
        actual = FizzBuzzWoofBangFactory().create().say(1155)
        self.assertEqual(expected, actual)

