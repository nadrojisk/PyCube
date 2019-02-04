'''
Created on Oct 25, 2018

@author: snow
'''
import unittest
from RCube.rotate2DList import rotateClockwise, convertListTo2DList, convert2DListToList, \
    rotateCounterclockwise


class Test(unittest.TestCase):

    def testCounterClockwise(self):
        originalList = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expectedRotatedFace = [[2, 5, 8], [1, 4, 7], [0, 3, 6]]

        actualRotation = rotateCounterclockwise(originalList)

        self.assertEqual(expectedRotatedFace, actualRotation)

    def testClockwise(self):
        originalList = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expectedRotation = [[6, 3, 0], [7, 4, 1], [8, 5, 2]]

        actualRotation = rotateClockwise(originalList)

        self.assertEqual(expectedRotation, actualRotation)
        pass

    def test1DTo2DConversion(self):
        originalList = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        expectedResult = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        actualResult = convertListTo2DList(3, originalList)

        self.assertEqual(expectedResult, actualResult)

    def test1DTo2DConversionSmallerSlice(self):
        originalList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expectedResult = [[0, 1, 2, 3], [4, 5, 6, 7], [8]]
        actualResult = convertListTo2DList(2, originalList)

        self.assertEqual(expectedResult, actualResult)

    def test2Dto1DConversion(self):
        originalList = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        convertedList = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        actualList = convert2DListToList(originalList)

        self.assertEqual(convertedList, actualList)
