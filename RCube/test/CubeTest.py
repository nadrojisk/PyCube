'''
Created on Oct 25, 2018

@author: snow
'''

import collections
import unittest

from RCube.Cube import Cube

CLOCKWISE = 'clockwise'
COUNTER_CLOCKWISE = 'counter-clockwise'


class Test(unittest.TestCase):

    def testShouldRotatePartOfFaceBeingRotatedClockwise(self):
        cube = Cube()
        face = ['0', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
        newFace = cube._rotateCallingFace(face, CLOCKWISE)

        self.assertEquals(newFace[2], face[0])

    def testShouldRotateFaceBeingRotatedClockwise(self):
        cube = Cube()
        face = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        expectedRotatedFace = ['6', '3', '0', '7', '4', '1', '8', '5', '2']
        actualRotatedFace = cube._rotateCallingFace(face, CLOCKWISE)

        self.assertEquals(actualRotatedFace, expectedRotatedFace)

    def testShouldRotateFaceBeingRotatedCounterClockwise(self):
        cube = Cube()
        face = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        expectedRotatedFace = ['2', '5', '8', '1', '4', '7', '0', '3', '6']
        actualRotatedFace = cube._rotateCallingFace(face, COUNTER_CLOCKWISE)

        self.assertEquals(actualRotatedFace, expectedRotatedFace)

    def testShouldRotateFrontClockwise(self):
        cube = Cube()
        faceBeingRotated = 'f'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['red', 'yellow', 'yellow', 'red', 'yellow', 'yellow', 'red', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'orange', 'white', 'white', 'orange', 'white', 'white', 'orange']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'white', 'white', 'white']),
            ('u', ['yellow', 'yellow', 'yellow', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateFrontCounterClockwise(self):
        cube = Cube()
        faceBeingRotated = 'F'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['orange', 'yellow', 'yellow', 'orange', 'yellow', 'yellow', 'orange', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'red', 'white', 'white', 'red', 'white', 'white', 'red']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'yellow', 'yellow', 'yellow']),
            ('u', ['white', 'white', 'white', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateLeftClockwise(self):
        cube = Cube()
        faceBeingRotated = 'l'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['red', 'green', 'green', 'red', 'green', 'green', 'red', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'orange', 'blue', 'blue', 'orange', 'blue', 'blue', 'orange']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['blue', 'red', 'red', 'blue', 'red', 'red', 'blue', 'red', 'red']),
            ('u', ['green', 'orange', 'orange', 'green', 'orange', 'orange', 'green', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateLeftCounterClockwise(self):
        cube = Cube()
        faceBeingRotated = 'L'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['orange', 'green', 'green', 'orange', 'green', 'green', 'orange', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'red', 'blue', 'blue', 'red', 'blue', 'blue', 'red']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['green', 'red', 'red', 'green', 'red', 'red', 'green', 'red', 'red']),
            ('u', ['blue', 'orange', 'orange', 'blue', 'orange', 'orange', 'blue', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateRightClockwise(self):
        cube = Cube()
        faceBeingRotated = 'r'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'orange', 'green', 'green', 'orange', 'green', 'green', 'orange']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['red', 'blue', 'blue', 'red', 'blue', 'blue', 'red', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'green', 'red', 'red', 'green', 'red', 'red', 'green']),
            ('u', ['orange', 'orange', 'blue', 'orange', 'orange', 'blue', 'orange', 'orange', 'blue'])))

        cube.rotateCube(faceBeingRotated)
        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateRightCounterClockwise(self):
        cube = Cube()
        faceBeingRotated = 'R'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'red', 'green', 'green', 'red', 'green', 'green', 'red']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['orange', 'blue', 'blue', 'orange', 'blue', 'blue', 'orange', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'blue', 'red', 'red', 'blue', 'red', 'red', 'blue']),
            ('u', ['orange', 'orange', 'green', 'orange', 'orange', 'green', 'orange', 'orange', 'green'])))

        cube.rotateCube(faceBeingRotated)
        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateTopClockwise(self):
        cube = Cube()
        faceBeingRotated = 't'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['blue', 'blue', 'blue', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['green', 'green', 'green', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)
        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateTopCounterClockwise(self):
        cube = Cube()
        faceBeingRotated = 'T'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['white', 'white', 'white', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['green', 'green', 'green', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['yellow', 'yellow', 'yellow', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['blue', 'blue', 'blue', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)
        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateUnderClockwise(self):
        cube = Cube()
        faceBeingRotated = 'u'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'white', 'white', 'white']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'yellow', 'yellow', 'yellow']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateUnderCounterClockwise(self):
        cube = Cube()
        faceBeingRotated = 'U'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'blue', 'blue', 'blue']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'white', 'white', 'white']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'green', 'green', 'green']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateBackClockwise(self):
        cube = Cube()
        faceBeingRotated = 'b'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'orange', 'yellow', 'yellow', 'orange', 'yellow', 'yellow', 'orange']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['red', 'white', 'white', 'red', 'white', 'white', 'red', 'white', 'white']),
            ('t', ['yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'white', 'white', 'white'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateBackCounterClockwise(self):
        cube = Cube()
        faceBeingRotated = 'B'
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'red', 'yellow', 'yellow', 'red', 'yellow', 'yellow', 'red']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['orange', 'white', 'white', 'orange', 'white', 'white', 'orange', 'white', 'white']),
            ('t', ['white', 'white', 'white', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'yellow', 'yellow', 'yellow'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldRotateFront(self):
        cube = Cube()
        faceBeingRotated = 'f'
        cubeCollection = collections.OrderedDict((
            ('f', ['red', 'yellow', 'blue', 'blue', 'green', 'orange', 'blue', 'red', 'green']),
            ('r', ['yellow', 'orange', 'white', 'green', 'yellow', 'yellow', 'yellow', 'red', 'yellow']),
            ('b', ['red', 'white', 'orange', 'blue', 'blue', 'green', 'green', 'white', 'red']),
            ('l', ['green', 'green', 'green', 'red', 'white', 'orange', 'blue', 'white', 'orange']),
            ('t', ['white', 'green', 'blue', 'yellow', 'red', 'white', 'white', 'orange', 'orange']),
            ('u', ['white', 'yellow', 'orange', 'red', 'orange', 'blue', 'yellow', 'blue', 'red'])))
        cube.sides = cubeCollection

        expectedRotatedCube = collections.OrderedDict((
            ('f', ['blue', 'blue', 'red', 'red', 'green', 'yellow', 'green', 'orange', 'blue']),
            ('r', ['white', 'orange', 'white', 'orange', 'yellow', 'yellow', 'orange', 'red', 'yellow']),
            ('b', ['red', 'white', 'orange', 'blue', 'blue', 'green', 'green', 'white', 'red']),
            ('l', ['green', 'green', 'white', 'red', 'white', 'yellow', 'blue', 'white', 'orange']),
            ('t', ['white', 'green', 'blue', 'yellow', 'red', 'white', 'orange', 'orange', 'green']),
            ('u', ['yellow', 'green', 'yellow', 'red', 'orange', 'blue', 'yellow', 'blue', 'red'])))

        cube.rotateCube(faceBeingRotated)

        self.assertEquals(expectedRotatedCube, cube.sides)

    def testShouldTestPicking1Rotations(self):
        cube = Cube()
        numberOfRotations = '1'
        cube.scramble(numberOfRotations)

        self.assertEquals(len(cube.rotations), int(numberOfRotations))

    def testShouldTestScrambleNotBeing100(self):
        cube = Cube()
        numberOfRotations = '1'
        cube.scramble(numberOfRotations)

        self.assertNotEquals(cube.status, 'scrambled 100')

    def testShouldTestScrambleNotBeing100Two(self):
        cube = Cube()
        numberOfRotations = '8'
        cube.scramble(numberOfRotations)

        self.assertNotEquals(cube.status, 'scrambled 100')

    def testShouldTestRandomnessFidelity(self):
        cube = Cube()
        faces = collections.OrderedDict((
            ('f', ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']),
            ('r', ['y', 'r', 'r', 'y', 'r', 'r', 'y', 'r', 'r']),
            ('b', ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']),
            ('l', ['o', 'o', 'w', 'o', 'o', 'w', 'o', 'o', 'w']),
            ('t', ['w', 'w', 'w', 'w', 'w', 'w', 'r', 'r', 'r']),
            ('u', ['o', 'o', 'o', 'y', 'y', 'y', 'y', 'y', 'y'])))
        cube.sides = faces
        cube._randomness()
        self.assertEquals(cube.randomness, 67)

    def testShouldTestTransitionFidelity(self):
        cube = Cube()
        numberOfRotations = '1'
        cube.scramble(numberOfRotations, 'transition')

        self.assertEquals(cube.status, 'scrambled 67')

    def testShouldFailSinceIllegalCubeColorNotInSet(self):
        cube = Cube()
        cubeCollection = collections.OrderedDict((
            ('f', ['r', 'red', 'blue', 'blue', 'green', 'orange', 'blue', 'red', 'green']),
            ('r', ['yellow', 'orange', 'white', 'green', 'red', 'yellow', 'yellow', 'red', 'yellow']),
            ('b', ['red', 'white', 'orange', 'blue', 'blue', 'green', 'green', 'white', 'red']),
            ('l', ['green', 'green', 'green', 'red', 'orange', 'orange', 'blue', 'white', 'orange']),
            ('t', ['white', 'green', 'blue', 'yellow', 'white', 'white', 'white', 'orange', 'orange']),
            ('u', ['white', 'yellow', 'orange', 'red', 'yellow', 'blue', 'yellow', 'blue', 'red'])))
        cube.sides = cubeCollection
        faceBeingRotated = 'f'
        cube.checkCube(cube.getCubeString())
        if cube.status != 'error':
            cube.rotateCube(faceBeingRotated)

        self.assertEquals('color not in set', cube.error)

    def testShouldFailSinceIllegalCubeIncorrectSize(self):
        cube = Cube()
        cubeCollection = collections.OrderedDict((
            ('f', ['red', 'blue', 'blue', 'green', 'orange', 'blue', 'red', 'green']),
            ('r', ['yellow', 'orange', 'white', 'green', 'red', 'yellow', 'yellow', 'red', 'yellow']),
            ('b', ['red', 'white', 'orange', 'blue', 'blue', 'green', 'green', 'white', 'red']),
            ('l', ['green', 'green', 'green', 'red', 'orange', 'orange', 'blue', 'white', 'orange']),
            ('t', ['white', 'green', 'blue', 'yellow', 'white', 'white', 'white', 'orange', 'orange']),
            ('u', ['white', 'yellow', 'orange', 'red', 'yellow', 'blue', 'yellow', 'blue', 'red'])))
        cube.sides = cubeCollection
        faceBeingRotated = 'f'

        cube.checkCube(cube.getCubeString())
        if cube.status != 'error':
            cube.rotateCube(faceBeingRotated)

        self.assertEquals('cube is not sized properly', cube.error)

    def testShouldFailSinceFaceNotGiven(self):
        cube = Cube()
        cubeCollection = collections.OrderedDict((
            ('f', ['red', 'blue', 'blue', 'green', 'orange', 'blue', 'red', 'green']),
            ('r', ['yellow', 'orange', 'white', 'green', 'red', 'yellow', 'yellow', 'red', 'yellow']),
            ('b', ['red', 'white', 'orange', 'blue', 'blue', 'green', 'green', 'white', 'red']),
            ('l', ['green', 'green', 'green', 'red', 'orange', 'orange', 'blue', 'white', 'orange']),
            ('t', ['white', 'green', 'blue', 'yellow', 'white', 'white', 'white', 'orange', 'orange']),
            ('u', ['white', 'yellow', 'orange', 'red', 'yellow', 'blue', 'yellow', 'blue', 'red'])))
        cube.sides = cubeCollection
        faceBeingRotated = ''
        cube.rotateCube(faceBeingRotated)

        self.assertEquals('face is missing', cube.error)

    def testShouldFailSinceIncorrectFace(self):
        cube = Cube()
        cubeCollection = collections.OrderedDict((
            ('f', ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']),
            ('r', ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']),
            ('b', ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']),
            ('l', ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']),
            ('t', ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']),
            ('u', ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'])))
        cube.sides = cubeCollection
        faceBeingRotated = 'blah'
        cube.rotateCube(faceBeingRotated)

        self.assertEquals('face is unknown', cube.error)

    def testShouldFailSinceNIsIllegal(self):
        cube = Cube()
        numberOfRotations = -1
        cube.scramble(numberOfRotations)

        self.assertEquals('n must be an integer between 0 to 99', cube.error)

    def testShouldFailSinceNIsIllegal2(self):
        cube = Cube()
        numberOfRotations = 100
        cube.scramble(numberOfRotations)

        self.assertEquals('n must be an integer between 0 to 99', cube.error)

    def testShouldFailSinceNIsIllegal3(self):
        cube = Cube()
        numberOfRotations = 'a'
        cube.scramble(numberOfRotations)

        self.assertEquals('n must be an integer between 0 to 99', cube.error)

    def testShouldFailSinceMethodIsIllegal(self):
        cube = Cube()
        numberOfRotations = '1'
        cube.scramble(numberOfRotations, 'test')

        self.assertEquals('unknown function for scramble', cube.error)
