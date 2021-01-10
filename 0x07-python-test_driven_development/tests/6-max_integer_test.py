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

    def test_normal_case_end(self):
      self.assertAlmostEqual(max_integer([2, 5, 3, 8, 10]), 10)
    
    def test_normal_case_beg(self):
      self.assertAlmostEqual(max_integer([10, 5, 3, 8, 6]), 10)
    
    def test_normal_case_neg(self):
      self.assertAlmostEqual(max_integer([10, 5, 3, -8, 6]), 10)

    def test_normal_case_all_neg(self):
      self.assertAlmostEqual(max_integer([-10, -5, -3, -8, -6]), -3)
    
    def test_normal_case_all_neg(self):
      self.assertAlmostEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
  