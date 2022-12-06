from grammar import *
from early_algo import *
from unittest import TestCase


class GrammarTests(TestCase):

    def test_parse_rules(self):
        q = parse_rules("F->1|tht |tRt")
        self.assertEqual(len(q), 3)
        self.assertEqual(q, ['F->', 'F->tht', 'F->tRt'])
        self.assertEqual(['F->'], parse_rules("F->1"))

    def test_non_terminal(self):
        self.assertTrue(is_non_terminal('A'))
        self.assertFalse(is_non_terminal('2'))
        self.assertFalse(is_non_terminal('v'))
        self.assertTrue(is_non_terminal('F'))

    def test_single_rule(self):
        self.assertFalse(is_valid_single_rule("dfsd"))
        self.assertFalse(is_valid_single_rule("Adfsg"))
        self.assertFalse(is_valid_single_rule("a->Adfsg"))
        self.assertTrue(is_valid_single_rule("D->"))
        self.assertTrue(is_valid_single_rule("R->Adfsg"))
        self.assertTrue(is_valid_single_rule("A->1"))
        self.assertFalse(is_valid_single_rule("A->1sdf"))
        self.assertFalse(is_valid_single_rule("A-dsfs"))
        self.assertFalse(is_valid_single_rule("A->34fdgf"))
        self.assertFalse(is_valid_single_rule("A->1|dsf"))
        self.assertTrue(is_valid_single_rule("A->sdfsaaFDs"))

    def test_multi_rules(self):
        self.assertTrue(is_valid_rule("A->||"))
        self.assertTrue(is_valid_rule("A->1|edfslr|1"))
        self.assertFalse(is_valid_rule("a->dsfs"))
        self.assertTrue(is_valid_rule("A->sdS|fl|1"))
        self.assertFalse(is_valid_rule("A->43|t"))
        self.assertFalse(is_valid_rule("A->sdfsdDaS|pf2"))
        self.assertTrue(is_valid_rule("F->1|feFkjdg|ds"))

    def test_start(self):
        g = Grammar('I')
        self.assertEqual(g.get_start(), 'I')
        k = Grammar()
        self.assertEqual(k.get_start(), 'S')

    def test_add_rules(self):
        g = Grammar()
        self.assertFalse(g.add_rule("asdf"))
        self.assertEqual(len(g), 0)
        self.assertTrue(g.add_rule("T->1"))
        self.assertEqual(len(g), 1)
        self.assertTrue(g.add_rule("T->1|asd|afdasR"))
        self.assertEqual(len(g), 4)

    def test_similar_rules(self):
        g = Grammar()
        g.add_rule("T->f|asd|fsdg")
        self.assertEqual(len(g), 3)
        g.add_rule("T->f")
        self.assertEqual(len(g), 4)
        g.del_similar_rules()
        self.assertEqual(len(g), 3)
        for i in range(100):
            g.add_rule("T->gfd")
        g.del_similar_rules()
        self.assertEqual(len(g), 4)

    def test_erase(self):
        g = Grammar()
        g.add_rule("T->f|asd|fsdg")
        t = g.__iter__()
        self.assertEqual(t.__next__(), 'T->f')
        g.erase_rule(t)
        self.assertEqual(len(g), 2)
        t = g.__iter__()
        self.assertEqual(g.erase_rule(t), t)

    def test_size(self):
        g = Grammar()
        g.add_rule("T->k")
        self.assertEqual(g.__len__('T'), 1)
        self.assertEqual(g.__len__(), 1)
        self.assertEqual(g.__len__('a'), 0)


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
        self.assertTrue(Algo(grammar).has_word("abadac"))
        self.assertTrue(Algo(grammar).has_word("dddddabadac"))
        self.assertFalse(Algo(grammar).has_word("cdddddabadac"))
        self.assertFalse(Algo(grammar).has_word(""))

    def test_5(self):
        grammar = self.get_data(5)
        self.assertTrue(Algo(grammar).has_word("kerim"))
        self.assertTrue(Algo(grammar).has_word("iiiri"))
        self.assertTrue(Algo(grammar).has_word(" "))

    def test_6(self):
        grammar = self.get_data(6)
        self.assertFalse(Algo(grammar).has_word('while(a<c)'))
        self.assertFalse(Algo(grammar).has_word('while(a<c);'))
        self.assertFalse(Algo(grammar).has_word('while(a<c'))
        self.assertTrue(Algo(grammar).has_word('(a<c);'))
        self.assertTrue(Algo(grammar).has_word('a<c;'))

    def test_7(self):
        grammar = self.get_data(7)
        self.assertTrue(Algo(grammar).has_word('12+15=27'))
        self.assertFalse(Algo(grammar).has_word('1215=27'))
        self.assertFalse(Algo(grammar).has_word('1+215='))
        self.assertTrue(Algo(grammar).has_word('++215=216'))
        self.assertTrue(Algo(grammar).has_word(''))

    def test_8(self):
        grammar = self.get_data(8)
        self.assertTrue(Algo(grammar).has_word('ayan went to moscow yesterday'))
        self.assertFalse(Algo(grammar).has_word('ayan to moscow went'))
        self.assertTrue(Algo(grammar).has_word('yesterday ayan went to moscow'))
        self.assertFalse(Algo(grammar).has_word('yesterday ayan went moscow'))
        self.assertTrue(Algo(grammar).has_word('yesterday ayan went to moscow.'))
