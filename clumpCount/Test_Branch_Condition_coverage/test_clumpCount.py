# Lab#7 - Whitebox testing
# SC353201 Software Quality Assurance
# Semester 1/2567
# Instructor: Chitsutha Soomlek

# Student : Phannakon Phungamngoen
# ID : 653380022-2
# Section : 1

import unittest
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from source.CountClump import CountClump

class Test_Branch_Condition_coverage(unittest.TestCase):
    
    def setUp(self):
        self.clump = CountClump()
        test_name = self.shortDescription()
        
        self.result = []
        
        print("Test : "+test_name)
    
    def tearDown(self) -> None:
        print("Result",self.result)
        self.result.clear()
        
        
    def test_None(self):
        """ None """
        self.result.append(self.clump.count_clumps(None))
        self.assertEqual(0, self.result[0])
        
    def test_empty(self):
        """ Empty """
        self.result.append(self.clump.count_clumps([]))
        self.assertEqual(0, self.result[0])
    
    def test_no_clump(self):
        """ No clump """
        self.result.append(self.clump.count_clumps([1,2,3]))
        self.assertEqual(0, self.result[0])
    
    def test_one_clump(self):
        """ One clump """
        self.result.append(self.clump.count_clumps([1,1,1]))
        self.assertEqual(1, self.result[0])
    
    
    
if __name__ == '__main__':
    suite = unittest.makeSuite(Test_Branch_Condition_coverage)
    suite.addTest(Test_Branch_Condition_coverage('test_None'))
    suite.addTest(Test_Branch_Condition_coverage('test_empty'))
    suite.addTest(Test_Branch_Condition_coverage('test_no_clump'))
    suite.addTest(Test_Branch_Condition_coverage('test_one_clump'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    