#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day06
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day06.solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
        self.assertEqual(result, 7)
    def test_02(self):
        result = day06.solve('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)
        self.assertEqual(result, 5)
    def test_03(self):
        result = day06.solve('nppdvjthqldpwncqszvftbrmjlhg', 4)
        self.assertEqual(result, 6)
    def test_04(self):
        result = day06.solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)
        self.assertEqual(result, 10)
    def test_05(self):
        result = day06.solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4)
        self.assertEqual(result, 11)
    def test_in(self):
        input = inputs.read("input06_actual")
        result = day06.solve(input[0], 4)
        self.assertEqual(result, 1723)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day06.solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
        self.assertEqual(result, 19)
    def test_02(self):
        result = day06.solve('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
        self.assertEqual(result, 23)
    def test_03(self):
        result = day06.solve('nppdvjthqldpwncqszvftbrmjlhg', 14)
        self.assertEqual(result, 23)
    def test_04(self):
        result = day06.solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
        self.assertEqual(result, 29)
    def test_05(self):
        result = day06.solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)
        self.assertEqual(result, 26)
    def test_in(self):
        input = inputs.read("input06_actual")
        result = day06.solve(input[0], 14)
        self.assertEqual(result, 3708)

if __name__ == '__main__':
    unittest.main(verbosity=2)
