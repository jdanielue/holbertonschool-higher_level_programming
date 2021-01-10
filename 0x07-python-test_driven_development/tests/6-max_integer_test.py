#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
      self.assertAlmostEqual(max_integer(list()), None)

    def test_normal_case(self):
      self.assertAlmostEqual(max_integer([2, 5, 3, 8, 6]), 8)

if __name__ == '__main__':
    unittest.main()
  