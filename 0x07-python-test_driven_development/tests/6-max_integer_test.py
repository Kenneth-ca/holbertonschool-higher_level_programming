#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_work(self):
        a_list = [1, 2, 3]
        self.assertEqual(3, max_integer(a_list))

    def test_empty(self):
        self.assertEqual(None, max_integer([]))

if __name__ == '__main__':
        unittest.main()
