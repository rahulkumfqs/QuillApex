# test_quillapex.py
"""
Tests for QuillApex module.
"""

import unittest
from quillapex import QuillApex

class TestQuillApex(unittest.TestCase):
    """Test cases for QuillApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuillApex()
        self.assertIsInstance(instance, QuillApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuillApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
