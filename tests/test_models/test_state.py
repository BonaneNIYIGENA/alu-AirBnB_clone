#!/usr/bin/python3
"""Unit tests for State"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(State.name, "")
