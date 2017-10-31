"""
Team - Agnel Aaron and Anjanay Kirti Gour
Roll no. - 2017010 and 217021 respectively
Section - B5 and A6 respectively
"""

import unittest
from a4 import *

class testpoint(unittest.TestCase):
    def test_columnsawp(self):
        self.assertEqual(columnswap([[1,0,0],[0,1,0],[0,0,1]],1,2),[[1,0,0],[0,0,1],[0,1,0]])
        self.assertEqual(columnswap([[0,0,0],[0,4,0],[0,0,0]],0,1),[[0,0,0],[4,0,0],[0,0,0]])
        self.assertEqual(columnswap([[10,20,10],[-20,-30,10],[30,50,0]],0,2),[[10,20,10],[10,-30,-20],[0,50,30]])
        self.assertEqual(columnswap([[0,1,0],[0,0,0]],0,1),[[1,0,0],[0,0,0]])
        self.assertEqual(columnswap([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]],2,3),[[1,3,9,5],[1,3,7,1],[4,3,7,9],[5,2,9,0]])
    def test_rowswap(self):
        self.assertEqual(swaprows([[1,0,0],[0,1,0],[0,0,1]],1,2),[[1,0,0],[0,0,1],[0,1,0]])
        self.assertEqual(swaprows([[0,0,0],[0,4,0],[0,0,0]],0,1),[[0,4,0],[0,0,0],[0,0,0]])
        self.assertEqual(swaprows([[10,20,10],[-20,-30,10],[30,50,0]],0,2),[[30,50,0],[-20,-30,10],[10,20,10]])
        self.assertEqual(swaprows([[0,1,0],[0,0,0]],0,1),[[0,0,0],[0,1,0]])
        self.assertEqual(swaprows([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]],2,3),[[1,3,5,9],[1,3,1,7],[5,2,0,9],[4,3,9,7]])
    def test_Row_transformation(self):
        self.assertEqual(Row_transformation([[1,0,0],[0,1,0],[0,0,1]],2.0,0,1),[[1,0,0],[2,1,0],[0,0,1]])
        self.assertEqual(Row_transformation([[0,0,0],[0,4,0],[0,0,0]],2.0,0,1),[[0,0,0],[0,4,0],[0,0,0]])
        self.assertEqual(Row_transformation([[10,20,10],[-20,-30,10],[30,50,0]],2.0,0,2),[[10,20,10],[-20,-30,10],[50,90,20]])
        self.assertEqual(Row_transformation([[0,1,0],[0,0,0]],2.0,0,1),[[0,1,0],[0,2,0]])
        self.assertEqual(Row_transformation([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]],2.0,2,3),[[1,3,5,9],[1,3,1,7],[4,3,9,7],[13,8,18,23]])
    def test_matrixrank(self):
        self.assertEqual(matrixrank([[1,0,0],[0,1,0],[0,0,1]]),3)
        self.assertEqual(matrixrank([[0,0,0],[0,4,0],[0,0,0]]),1)
        self.assertEqual(matrixrank([[10,20,10],[-20,-30,10],[30,50,0]]),2)
        self.assertEqual(matrixrank([[0,1,0],[0,0,0]]),1)
        self.assertEqual(matrixrank([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]),4)
if __name__=="__main__":
    unittest.main()
