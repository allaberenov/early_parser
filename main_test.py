from grammar import Grammar
from early_algo import Algo
import pytest


def get_data():
    file = open('test/test1.txt', 'r')
    grammar = Grammar()
    for line in file:
        grammar.add_rule(line)
    return grammar


def test_1():
    assert Algo(get_data()).has_word('ababa') == False


def test_2():
    assert Algo(get_data()).has_word('abb') == False
