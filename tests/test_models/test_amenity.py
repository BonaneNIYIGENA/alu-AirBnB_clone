#!/usr/bin/python3
"""Unit tests for Amenity"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(Amenity.name, "")
