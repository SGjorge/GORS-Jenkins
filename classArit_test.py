import unittest
import classArit

class MyTest(unittest.TestCase):
	def testSum(self):
		self.assertEqual(classArit.sum(2,3),5)

	def testRest(self):
		self.assertEqual(classArit.rest(3,2),1)

	def testMult(self):
		self.assertEqual(classArit.mult(3,2),6)

	def testDiv(self):
		self.assertEqual(classArit.div(4,2),2)

	def testMySqrt(self):
		self.assertEqual(classArit.mySqrt(4),2)

if __name__=='__main__':
	unittest.main()