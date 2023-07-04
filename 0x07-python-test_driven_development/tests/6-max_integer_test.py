#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test with an unsorted list of positive integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-5, 0, 10, -3]), 10)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
