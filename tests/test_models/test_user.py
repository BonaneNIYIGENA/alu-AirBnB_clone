#!/usr/bin/python3
"""Unit tests for User"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(User.email, "")
