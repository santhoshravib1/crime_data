import unittest 
from validate_functions import checkVictSex, checkVictAge
from stats_function import findMean, findMedian

class testFunctions(unittest.TestCase):
    def testVictSex(self):
        self.assertIsInstance(checkVictSex(), bool)

    def testVictAge(self):
        self.assertIsInstance(checkVictAge(), bool)

    def testMean(self):
        self.assertTrue(1 <= findMean() <= 100)
    
    def testMedian(self):
        self.assertTrue(1 <= findMedian() <= 100)

if __name__ == '__main__':
    unittest.main()
