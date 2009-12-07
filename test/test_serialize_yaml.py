# coding: utf-8

"""
Test serializing XML
"""

import re

from tiddlyweb.model.bag import Bag
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.model.tiddler import Tiddler
from tiddlyweb.serializer import Serializer

def setup_module(module):
    module.serializer = Serializer('tiddlywebplugins.xml')

def test_list_single_recipe_as_xml():
    recipes = [Recipe('recipe' + str(name)) for name in xrange(1)]
    string = serializer.list_recipes(recipes)
    assert string == '<?xml version="1.0"?><marshal><list id="i2"><unicode>recipe0</unicode></list></marshal>'

def test_list_recipes_as_xml():
    recipes = [Recipe('recipe' + str(name)) for name in xrange(2)]
    string = serializer.list_recipes(recipes)
    assert string == '<?xml version="1.0"?><marshal><list id="i2"><unicode>recipe0</unicode><unicode>recipe1</unicode></list></marshal>'
