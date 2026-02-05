#!/usr/bin/python3
"""Unit tests for Place"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(Place.name, "")
