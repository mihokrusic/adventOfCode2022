#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day05
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input05")
        result = day05.solve(input, True)
        self.assertEqual(result, 'CMZ')

    def test_in(self):
        input = inputs.read("input05_actual")
        result = day05.solve(input, True)
        self.assertEqual(result, 'VPCDMSLWJ')

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input05")
        result = day05.solve(input, False)
        self.assertEqual(result, 'MCD')

    def test_in(self):
        input = inputs.read("input05_actual")
        result = day05.solve(input, False)
        self.assertEqual(result, 'TPWCGNCCG')

if __name__ == '__main__':
    unittest.main(verbosity=2)
