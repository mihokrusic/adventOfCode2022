#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day01
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input01")
        result = day01.part1(input)
        self.assertEqual(result, 24000)

    def test_in(self):
        input = inputs.read("input01_actual")
        result = day01.part1(input)
        self.assertEqual(result, 66616)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input01")
        result = day01.part2(input)
        self.assertEqual(result, 45000)

    def test_in(self):
        input = inputs.read("input01_actual")
        result = day01.part2(input)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
