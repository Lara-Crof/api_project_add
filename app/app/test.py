"""sample test"""
from django.test import SimpleTestCase

from app import calc

class CalcTesr(SimpleTestCase):

    def test_add_number(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_substract_numders(self):
        """Test subtracting number"""
        rec = calc.substract(10, 15)
        self.assertEqual(rec, 5)
    
  