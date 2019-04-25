import unittest
from lshPy import compute

class lshTestCase(unittest.TestCase):
    """Unit testing begins"""
    def test_given_samples(self):
        self.assertAlmostEqual(compute("testisyote"),"TeStIsYoTe")
        self.assertAlmostEqual(compute("num 5 on pariton"),"NuM o On PaRiToN")
        self.assertAlmostEqual(compute("hel 123 $# abc"),"HeL oEo $# AbC")
        
if __name__ == '__main__':
    unittest.main()