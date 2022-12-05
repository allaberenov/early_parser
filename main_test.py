from grammar import *
from early_algo import *

from unittest import *


class AlgoTests(TestCase):

    def get_data(self):
        file = open('test/test_1.txt', 'r')
        grammar = Grammar()
        for line in file:
            grammar.add_rule(line)
        return grammar

    def test_simple(self):

        self.assertTrue(q.has_word("ab"))
