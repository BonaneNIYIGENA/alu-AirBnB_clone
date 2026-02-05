#!/usr/bin/python3
"""Unit tests for FileStorage"""
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_all(self):
        from models import storage
        self.assertIsInstance(storage.all(), dict)
