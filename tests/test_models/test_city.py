#!/usr/bin/python3
"""Unit tests for City"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(City.name, "")
