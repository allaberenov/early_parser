from early_algo import *
from unittest import TestCase


class GrammarTests(TestCase):
    def test_non_terminal(self):
        self.assertTrue(is_non_terminal('A'))
        self.assertFalse(is_non_terminal('2'))
        self.assertFalse(is_non_terminal('v'))
        self.assertTrue(is_non_terminal('F'))

    def test_start(self):
        g = Grammar('I')
        self.assertEqual(g.get_start(), 'I')
        k = Grammar()
        self.assertEqual(k.get_start(), 'S')


class AlgoTests(TestCase):

    def get_data(self, number):
        filename = 'test/test_' + str(number) + '.txt'
        file = open(filename, 'r')
        grammar = Grammar()
        for line in file:
            grammar.add_rule(line)
        return grammar

    def test_0(self):
        grammar = self.get_data(0)
        self.assertFalse(Algo(grammar).has_word("abb"))
        self.assertFalse(Algo(grammar).has_word(" "))

    def test_1(self):
        grammar = self.get_data(1)
        self.assertTrue(Algo(grammar).has_word("abb"))
        self.assertFalse(Algo(grammar).has_word("babba"))
        self.assertTrue(Algo(grammar).has_word("ababba"))
        self.assertFalse(Algo(grammar).has_word(""))
        self.assertTrue(Algo(grammar).has_word("aaabbabbabba"))

    def test_2(self):
        grammar = self.get_data(2)
        self.assertTrue(Algo(grammar).has_word("abb"))
        self.assertFalse(Algo(grammar).has_word("babba"))
        self.assertFalse(Algo(grammar).has_word("ababba"))
        self.assertTrue(Algo(grammar).has_word(''))
        self.assertFalse(Algo(grammar).has_word("aaabbabbabba"))

    def test_3(self):
        grammar = self.get_data(3)
        self.assertFalse(Algo(grammar).has_word("eee"))
        self.assertTrue(Algo(grammar).has_word("e"))
        self.assertTrue(Algo(grammar).has_word(''))

    def test_4(self):
        grammar = self.get_data(4)
        self.assertTrue(Algo(grammar).has_word("adc"))
        self.assertTrue(Algo(grammar).has_word("adc"))
        self.assertTrue(Algo(grammar).has_word("abadadc"))
        self.assertTrue(Algo(grammar).has_word("dddddabadadc"))
        self.assertFalse(Algo(grammar).has_word("cdddddabadac"))
        self.assertFalse(Algo(grammar).has_word(""))

    def test_5(self):
        grammar = self.get_data(5)
        self.assertTrue(Algo(grammar).has_word("ab"))
        self.assertTrue(Algo(grammar).has_word("abaabb"))
        self.assertTrue(Algo(grammar).has_word(""))
        self.assertFalse(Algo(grammar).has_word("a"))

    def test_6(self):
        grammar = self.get_data(6)
        self.assertTrue(Algo(grammar).has_word('()()()()()()'))
        self.assertTrue(Algo(grammar).has_word('()((())())()'))
        self.assertFalse(Algo(grammar).has_word('())'))
        self.assertTrue(Algo(grammar).has_word('(((((())))))'))
        self.assertFalse(Algo(grammar).has_word('(((()'))
        self.assertTrue(Algo(grammar).has_word(''))

    def test_7(self):
        grammar = self.get_data(7)
        self.assertTrue(Algo(grammar).has_word('12+15=27'))
        self.assertTrue(Algo(grammar).has_word('15+12=27'))
        self.assertFalse(Algo(grammar).has_word('1215=27'))
        self.assertFalse(Algo(grammar).has_word('1+215='))
        self.assertTrue(Algo(grammar).has_word(''))

    def test_8(self):
        grammar = self.get_data(8)
        self.assertTrue(Algo(grammar).has_word('ayan_went_to_moscow_yesterday'))
        self.assertFalse(Algo(grammar).has_word('ayan_to_moscow_went'))
        self.assertTrue(Algo(grammar).has_word('yesterday_ayan_went_to_moscow'))
        self.assertFalse(Algo(grammar).has_word('yesterday_ayan_went_moscow'))
        self.assertTrue(Algo(grammar).has_word('yesterday_ayan_went_to_moscow.'))
        self.assertTrue(Algo(grammar).has_word('ayan_went_to_moscow.'))

    def test_from_lecture(self):
        grammar = self.get_data(9)
        self.assertFalse(Algo(grammar).has_word('abb'))
        self.assertTrue(Algo(grammar).has_word('aaabbbaaaabbbbaaaaabbbbbaabb'))
        self.assertFalse(Algo(grammar).has_word('baaabbbaaaabbbbaaaaabbbbbaabb'))
