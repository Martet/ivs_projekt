import unittest
from math_library import *
import math



class TestADD(unittest.TestCase):
<<<<<<< HEAD
   def testADDnuber(self):
      result=ADD(1.00012, 1.00012)
=======
   def ADDnumber(self):
      result=ADD(1.00012, 1.00012 )
>>>>>>> a6458ef4011ebc4677e33ac3cb86e363ed2ac09e
      self.assertEqual(result, 1.00024)
      result=ADD(1000000000000, 1000000000000)
      self.assertEqual(result, 2000000000000)
      result=ADD(5,-7)
      self.assertEqual(result,-2)
      result=ADD(0,12)
      self.assertEqual(result, 12)
   def testADDstring(self):
      self.assertRaises(TypeError, ADD("ad",6))
      self.assertRaises(TypeError, ADD(6,"ad"))
      self.assertRaises(TypeError, ADD("ad","ad"))

class TestSUB(unittest.TestCase):        
   def testSUBnumber(self):
      result=SUB(1.00012, 1.00011 )
      self.assertEqual(result, 0.00001)
      result=SUB(1000000000000, 100000000000 )
      self.assertEqual(result, 900000000000)
      result=SUB(5,-7)
      self.assertEqual(result,12)
      result=SUB(0,12)
      self.assertEqual(result, -12)
   def testSUBstring(self):
      self.assertRaises(TypeError, SUB("ad",6))
      self.assertRaises(TypeError, SUB(6,"ad"))
      self.assertRaises(TypeError, SUB("ad","ad"))

class TestDIV(unittest.TestCase):
   def testDIVnumber(self):
      result=DIV(5000, 5)
      self.assertEqual(result, 1000)
      result=DIV(10, 3)
      self.assertEqual(result, (10.0/3.0))
      result=DIV(5, 5)
      self.assertEqual(result, 1)
      result=DIV(-325, 5)
      self.assertEqual(result, -65)
      result=DIV(-10, -2)
      self.assertEqual(result, 5)
      self.assertRaises(ZeroDivisionError, DIV(10,0))
   def testDIVstring(self):
      self.assertRaises(TypeError, DIV("ad",6))
      self.assertRaises(TypeError, DIV(6,"ad"))
      self.assertRaises(TypeError, DIV("ad","ad"))

class TestSQRT(unittest.TestCase):
   def testSQRTnumber(self):
      result=SQRT(25)
      self.assertEqual(result, 5)
      result=SQRT(0)
      self.assertEqual(result, 0)
      result=SQRT(159)
      self.assertEqual(result, math.sqrt(159))
      result=SQRT(135429.123456)
      self.assertEqual(result, math.sqrt(135429.123456))
      result=SQRT(10000000000000000)
      self.assertEqual(result, math.sqrt(10000000000000000))
      self.assertRaises(ValueError, SQRT(-5))
      self.assertRaises(ValueError, SQRT(-459))
   def testSQRTstring(self):
      self.assertRaises(TypeError, SQRT("ad"))
class TestMUL(unittest.TestCase):
   def testMULnumber(self):
      result=MUL(10, 10)
      self.assertEqual(result, 100)
      result=MUL(1.23, 1.54)
      self.assertEqual(result, 1.8942)
      result=MUL(500000, 0)
      self.assertEqual(result, 0)
      result=MUL(0.5, 0.5)
      self.assertEqual(result, 0.25)
      result=MUL(-10, 10)
      self.assertEqual(result, -100)
      result=MUL(-10, -10)
      self.assertEqual(result, 100)
   def testMULstring(self):
      self.assertRaises(TypeError, MUL("ad", 6))
      self.assertRaises(TypeError, MUL(6, "ad"))
      self.assertRaises(TypeError, MUL("ad", "ad"))

class TestPOW(unittest.TestCase):
   def testPOWnumber(self):
      result = POW(1)
      self.assertEqual(result, 1*1)
      result = POW(2)
      self.assertEqual(result, 2*2)
      result = POW(50)
      self.assertEqual(result, 50*50)
      result=POW(-20)
      self.assertEqual(result, -20*-20)

   def testPOWstring(self):
      self.assertRaises(TypeError, POW("ad"))

if __name__ == '__main__':
   unittest.main()
