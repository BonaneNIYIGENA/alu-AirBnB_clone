#!/usr/bin/python3
"""Unit tests for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_id_is_string(self):
        """Check if id is a string"""
        model = BaseModel()
        self.assertEqual(type(model.id), str)

    def test_unique_id(self):
        """Check if ids are unique"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

if __name__ == "__main__":
    unittest.main()
    