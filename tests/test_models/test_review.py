#!/usr/bin/python3
"""Unit tests for Review"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(Review.text, "")
