from early_algo import Algo
from grammar import Grammar

f = open('test', 'r')
grammar = Grammar()
for line in f:
    grammar.add_rule(line)
word = input()

print(Algo(grammar).has_word(word))