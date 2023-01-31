"""
Test for quote.py
"""
import unittest
# TestCase is a file
from unittest import TestCase

# Import code to use
import quote

class QuoteTest(TestCase):

    def test_quote_for_small_lawn_same_day(self):
        # variable
        actual_quote = quote.lawn_quote('small', True)
        expected_quote = 15
        # Check if value of return is the same as expected_quote 
        self.assertEqual(expected_quote, actual_quote )
    
    # More tests using self.assertEqual() method
    def test_quote_for_large_lawn_not_same_day(self):
        self.assertEqual(20, quote.lawn_quote('large', False))
        
    # Test for invalid data
    def test_quote_for_unrecognized_size(self):
        # variable
        actual_quote = quote.lawn_quote('alligator', False)
        self.assertIsNone(actual_quote)

# Run test
if __name__ == '__main__':
    unittest.main()

""" 
Running test from terminal
                        'name of test file'
    python -m unittest test_quote.py
"""
