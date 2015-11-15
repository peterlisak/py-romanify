import unittest
import romanify


class TestSimple(unittest.TestCase):

    def test_basic_roman_numerals(self):
        # basic numerals
        self.assertEqual(romanify.roman2arabic('I'), 1)
        self.assertEqual(romanify.roman2arabic('V'), 5)
        self.assertEqual(romanify.roman2arabic('X'), 10)
        self.assertEqual(romanify.roman2arabic('L'), 50)
        self.assertEqual(romanify.roman2arabic('C'), 100)
        self.assertEqual(romanify.roman2arabic('D'), 500)
        self.assertEqual(romanify.roman2arabic('M'), 1000)

    def test_basic_arabic_numerals(self):
        # basic numerals
        self.assertEqual(romanify.arabic2roman(1), 'I')
        self.assertEqual(romanify.arabic2roman(5), 'V')
        self.assertEqual(romanify.arabic2roman(10), 'X')
        self.assertEqual(romanify.arabic2roman(50), 'L')
        self.assertEqual(romanify.arabic2roman(100), 'C')
        self.assertEqual(romanify.arabic2roman(500), 'D')
        self.assertEqual(romanify.arabic2roman(1000), 'M')

    def test_repeating_roman_numerals(self):
        # repeatinf roman numerals
        self.assertEqual(romanify.roman2arabic('II'), 2)
        self.assertEqual(romanify.roman2arabic('III'), 3)
        self.assertEqual(romanify.roman2arabic('XX'), 20)
        self.assertEqual(romanify.roman2arabic('XXX'), 30)
        self.assertEqual(romanify.roman2arabic('CC'), 200)
        self.assertEqual(romanify.roman2arabic('CCC'), 300)
        self.assertEqual(romanify.roman2arabic('MMMMM'), 5000)

    def test_repeating_arabic_numerals(self):
        # repeatinf roman numerals
        self.assertEqual(romanify.arabic2roman(2), 'II')
        self.assertEqual(romanify.arabic2roman(3), 'III')
        self.assertEqual(romanify.arabic2roman(20), 'XX')
        self.assertEqual(romanify.arabic2roman(30), 'XXX')
        self.assertEqual(romanify.arabic2roman(200), 'CC')
        self.assertEqual(romanify.arabic2roman(300), 'CCC')
        self.assertEqual(romanify.arabic2roman(5000), 'MMMMM')

    def test_substract_roman_syntax(self):
        # substract roman syntax
        self.assertEqual(romanify.roman2arabic('IV'), 4)
        self.assertEqual(romanify.roman2arabic('IX'), 9)
        self.assertEqual(romanify.roman2arabic('XL'), 40)
        self.assertEqual(romanify.roman2arabic('XC'), 90)
        self.assertEqual(romanify.roman2arabic('CD'), 400)
        self.assertEqual(romanify.roman2arabic('CM'), 900)

    def test_substract_arabic_syntax(self):
        # substract roman syntax
        self.assertEqual(romanify.arabic2roman(4), 'IV')
        self.assertEqual(romanify.arabic2roman(9), 'IX')
        self.assertEqual(romanify.arabic2roman(40), 'XL')
        self.assertEqual(romanify.arabic2roman(90), 'XC')
        self.assertEqual(romanify.arabic2roman(400), 'CD')
        self.assertEqual(romanify.arabic2roman(900), 'CM')

    def test_combination_roman_numerals(self):
        # combination of roman numerals
        self.assertEqual(romanify.roman2arabic('CDXLIV'), 444)
        self.assertEqual(romanify.roman2arabic('DLV'), 555)
        self.assertEqual(romanify.roman2arabic('MCXI'), 1111)
        self.assertEqual(romanify.roman2arabic('MDCLXVI'), 1666)
        self.assertEqual(romanify.roman2arabic('MMMMMMDCCCXXXIII'), 6833)

    def test_combination_arabic_numerals(self):
        # combination of roman numerals
        self.assertEqual(romanify.arabic2roman(444), 'CDXLIV')
        self.assertEqual(romanify.arabic2roman(555), 'DLV')
        self.assertEqual(romanify.arabic2roman(1111), 'MCXI')
        self.assertEqual(romanify.arabic2roman(1666), 'MDCLXVI')

    def test_reverse_combination(self):
        self.assertEqual(romanify.roman2arabic(
            romanify.arabic2roman(123456789)), 123456789)
        self.assertEqual(romanify.roman2arabic(
            romanify.arabic2roman(987654321)), 987654321)

    def test_low_roman_numerals(self):
        # low case
        self.assertEqual(romanify.roman2arabic('MDcLxVI'), 1666)
        self.assertEqual(romanify.roman2arabic('mdclxvi'), 1666)

    def test_wrong_roman_numerals(self):
        # wrong roman numerals
        self.assertRaises(ValueError, romanify.roman2arabic, 'yc')
        self.assertRaises(ValueError, romanify.roman2arabic, 'cF')
        self.assertRaises(ValueError, romanify.roman2arabic, 'Mk')
        self.assertRaises(ValueError, romanify.roman2arabic, 'OM')

    def test_substract_roman_syntax_error(self):
        # wrong substract syntax
        self.assertRaises(ValueError, romanify.roman2arabic, 'IVI')
        self.assertRaises(ValueError, romanify.roman2arabic, 'IXI')
        self.assertRaises(ValueError, romanify.roman2arabic, 'XCX')
        self.assertRaises(ValueError, romanify.roman2arabic, 'CDC')

        self.assertRaises(ValueError, romanify.roman2arabic, 'IC')
        self.assertRaises(ValueError, romanify.roman2arabic, 'VD')
        self.assertRaises(ValueError, romanify.roman2arabic, 'LM')
        self.assertRaises(ValueError, romanify.roman2arabic, 'DM')

        self.assertRaises(ValueError, romanify.roman2arabic, 'MIM')
        self.assertRaises(ValueError, romanify.roman2arabic, 'IMM')

    def test_repeating_roman_numerals_error(self):
        # too much numeral repeating
        self.assertRaises(ValueError, romanify.roman2arabic, 'IIII')
        self.assertRaises(ValueError, romanify.roman2arabic, 'VV')
        self.assertRaises(ValueError, romanify.roman2arabic, 'XXXX')
        self.assertRaises(ValueError, romanify.roman2arabic, 'LL')
        self.assertRaises(ValueError, romanify.roman2arabic, 'CCCC')
        self.assertRaises(ValueError, romanify.roman2arabic, 'DD')

    def test_interesting_roman_numerals(self):
        # number of the beast
        self.assertEqual(romanify.roman2arabic('DCLXVI'), 666)
        # least number of all roman numerals
        self.assertEqual(romanify.roman2arabic('MCDXLIV'), 1444)
        # descending roman numerals
        self.assertEqual(romanify.roman2arabic('MDCLXVI'), 1666)
        # not MIM
        self.assertEqual(romanify.roman2arabic('MCMXCIX'), 1999)
