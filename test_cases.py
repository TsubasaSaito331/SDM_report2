#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc(0,7))

        def test_sample2 (self):
                self.assertEqual (0.000015, calc(0.0000001,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc(-0.1,1))

        def test_sample4 (self):
                self.assertEqual (-1, calc(1,1))

        def test_sample5 (self):
                self.assertEqual (-1, calc(1,1000))

        def test_sample6 (self):
                self.assertEqual (-1, calc(1,1000.1))

        def test_sample7 (self):
                self.assertEqual (999.9, calc(1,999.9))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1,1))

        def test_sample9 (self):
                self.assertEqual (-1, calc(1,'2'))

