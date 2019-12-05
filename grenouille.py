# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:10:21 2019

@author: delan
"""

from pyDatalog import pyDatalog
pyDatalog.clear()

pyDatalog.create_terms('croakes, Pet, frog, chrisp, cannary, sing, yellow, green, eat_flies, p, marg')

frog(Pet) <= croakes(Pet) & eat_flies(Pet)
cannary(Pet) <= chrisp(Pet) & sing(Pet)
green(Pet) <= frog(Pet)
yellow(Pet) <= cannary(Pet)
+croakes(marg)
+eat_flies(marg)
+frog(marg)


pyDatalog.assert_fact('croakes, marg')
pyDatalog.assert_fact('eat_flies, marg')

query = 'green(marg)'
answers = pyDatalog.ask(query).answers
print( answers )