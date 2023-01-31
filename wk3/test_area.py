from unittest import TestCase
# Import name of file to test
import area

class TestShapeAreas(TestCase):

    def test_triangle_area(self):

        # A triangle with height 4 base 5 should have area = 10
            # (Expected value, actual_value(parameter, parameter))
        self.assertEqual(10, area.triangle_area(4, 5))

    # Testing for floating point data
        # .assertAlmostEqual means data clost to what is expected
    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25,4.91))

    # Error testing for negative numbers
    def test_triangle_negative_height_base_raises_value_exception(self):
        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)
    
    # Error testing for 0
    def test_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 4))
        self.assertEqual(0, area.triangle_area(4, 0))
        self.assertEqual(0, area.triangle_area(0, 0))