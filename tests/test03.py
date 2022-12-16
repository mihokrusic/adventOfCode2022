#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day03
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input03")
        result = day03.part1(input)
        self.assertEqual(result, 157)

    def test_in(self):
        input = inputs.read("input03_actual")
        result = day03.part1(input)
        self.assertEqual(result, 7674)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input03")
        result = day03.part2(input)
        self.assertEqual(result, 70)

    def test_in(self):
        input = inputs.read("input03_actual")
        result = day03.part2(input)
        self.assertEqual(result, 2805)

if __name__ == '__main__':
    unittest.main(verbosity=2)
