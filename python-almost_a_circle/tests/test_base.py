#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_id_assignment(self):
        """Test if ids are assigned correctly."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string_None(self):
        """Test if to_json_string method handles None input."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test if to_json_string method handles empty input."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_None(self):
        """Test if from_json_string method handles None input."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test if from_json_string method handles empty input."""
        self.assertEqual(Base.from_json_string(""), [])

if __name__ == "__main__":
    unittest.main()
