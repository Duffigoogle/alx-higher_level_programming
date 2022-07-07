#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list_is_empty(self):
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_negative_number_in_the_list(self):
        self.assertEqual(max_integer([-1, 2, 3]), 3)

    def test_only_negative_numbers_in_the_list(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_raises(self):
        self.assertRaises(TypeError, max_integer, 10)
        self.assertRaises(TypeError, max_integer, 10.0)


"""python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1"""
