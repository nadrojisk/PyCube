'''
    Cube.py

    Initilizes a default cube if no default sides provided 

    Created on Oct 24, 2018
    Modified for Assignment 6 10/19/18
    Modified for Assignment 7 11/10/18
    @author: Jordan Sosnowski
'''
import collections
from math import ceil
from random import randint

from RCube.Corner import Corner
from RCube.Edge import Edge
from RCube.rotate2DList import rotateClockwise, convertListTo2DList, \
    convert2DListToList, rotateCounterclockwise

ERROR = "error"


class Cube:

    def createCube(self):
        # Cube will be created based on colors passed during cube construction
        if self.status != ERROR:  # set color values, if True, no missing values
            self.status = 'created'
            self._addColorsToSides()

    def checkCube(self, cubeString):
        # Check to see if cube is correct size, then setup default colors, sides and then check if cube is legal,
        # after that check its type
        self._parseCube(cubeString)
        if len(self.cubeList) == self.elements:  # if cube is correct size - 54 elements, then setup sides
            self._setupSides()
            if self._isCubeLegal():  # if cube is legal, then get its type
                self._getCubeType()
        else:
            self.setErrorMessage('cube is not sized properly')

    def rotateCube(self, faceToBeRotated):
        ''' Rotates given face.

        First rotates faces affected by rotating face, then rotates rotating face

        If no face is given then error message is 'face is missing'
        If face is given but not logical then error message is 'face is unknown'

        '''

        if faceToBeRotated is not '':
            if self.status != ERROR:
                self.status = 'rotated'
                oppositeFaces = {'f': 'b', 'l': 'r', 't': 'u',
                                 'b': 'f', 'r': 'l', 'u': 't'}

                rotation = self._getRotationDirection(faceToBeRotated)
                faceToBeRotated = faceToBeRotated.lower()  # converts face to lower
                if faceToBeRotated in self.sides.keys():  # if face is a valid face, if not then face is unknown
                    faceNotBeingAffected = oppositeFaces[
                        faceToBeRotated]  # face not being affected is face opposite to face being rotated

                    # sets the side that are being affected by the rotating side
                    rotatedSides = self._rotateOtherFaces(faceToBeRotated, rotation)

                    rotatedSides[faceNotBeingAffected] = self.sides[
                        faceNotBeingAffected]  # sets side that is not rotated to itself
                    # sets the side that is being rotated
                    rotatedSides[faceToBeRotated] = self._rotateCallingFace(self.sides[faceToBeRotated], rotation)

                    for side in self.sides:  # puts rotatedSides in correct order 'f, t, b, l, t, u'
                        self.sides[side] = rotatedSides[side]
                else:
                    self.setErrorMessage('face is unknown')
        else:
            self.setErrorMessage('face is missing')

    def scramble(self, n='0', method='random'):
        ''' Scrambles cube

            Inputs:
                method: determines type of scramble
                    random: picks a random rotation, and then calculates
                        randomness after that rotation
                    transition: calculates randomness of every possible rotation
                        and picks the smallest randomness and performs that rotation
                n: determines the repetition of rotations
                    Must be from 1 to 99

        '''

        rotates = ['f', 'l', 'r', 'b', 'u', 't', 'F', 'L', 'R', 'B', 'U', 'T']
        if method != 'transition' and method != 'random':
            self.setErrorMessage('unknown function for scramble')

        else:
            if self._isInt(n):
                numberOfRotations = int(n)
                if 0 <= numberOfRotations <= 99:
                    self._addColorsToSides()
                    for _ in range(numberOfRotations):
                        if method == 'transition':
                            side = self._transition()  # picks smallest randomness rotation
                        else:
                            side = rotates[randint(0, 11)]  # pick random rotation
                        self.rotations.extend(side)  # add rotation to rotation list
                        self.rotateCube(side)  # rotate cube

                    self._randomness()  # calculate randomness

                    self.status = 'scrambled %d' % self.randomness

                else:
                    self.setErrorMessage('n must be an integer between 0 to 99')
            else:
                self.setErrorMessage('n must be an integer between 0 to 99')

    def getCubeList(self):
        # gets contents of cube as a list
        cube = []
        for side in self.sides.values():
            for value in side:
                cube.append(value)
        return cube

    def getCubeString(self):
        # gets contents of cube as a string
        cube = ""
        for side in self.sides.values():
            for value in side:
                cube += value + ','
        return cube

    def __init__(self, colors=None):
        # Constructor
        if colors is None:
            colors = collections.OrderedDict(
                (('f', 'green'), ('r', 'yellow'), ('b', 'blue'), ('l', 'white'), ('t', 'red'), ('u', 'orange')))
        self._setupVariables()  # sets up default variables
        self.colors = colors
        self._areColorsUnique()  # check for duplicate colors

    def _setupVariables(self):  # had to do this because the class would not recreate itself upon calling dispatch again
        # setup default values
        self.numOfSides = 6
        self.elements = 54
        self.dots = self.elements / self.numOfSides
        self.numOfCorners = 8
        self.middleElement = 4
        self.rotations = []
        self.randomness = 100

        # setup default empty sides
        self.sideNames = ('f', 'r', 'b', 'l', 't', 'u')
        self.sides = collections.OrderedDict(((self.sideNames[0], []), (self.sideNames[1], []), (self.sideNames[2], []),
                                              (self.sideNames[3], []), (self.sideNames[4], []),
                                              (self.sideNames[5], [])))

        # setup default strings
        self.status = ""  # should be created, error, full, spots, or crosses
        self.op = ""
        self.cubeList = None
        self.error = ""

    def _areColorsUnique(self):
        # Loop through sides to see if there are duplicate values
        uniqueColorsLength = self._createUniqueColorCollection()
        if uniqueColorsLength != len(self.colors.values()):  # if true there is a duplicate, return False
            self.setErrorMessage('duplicate side')
            return False
        return True  # else, list is unique and return True

    def _createUniqueColorCollection(self):
        # creates unique collection of colors
        uniqueColors = []
        for side in self.colors.values():
            if side not in uniqueColors:
                uniqueColors.append(side)
        return len(uniqueColors)

    def _addColorsToSides(self):
        # add colors to the correct sides
        for key in self.sides:  # loops through sides, will apply the color of the side to each block on the side
            value = self.colors[key]
            for _ in range(9):  # loops through blocks to apply color to
                self.sides[key].append(value)

    def _cleanupList(self):
        # makes sure the list does not contain any empty elements
        for value in self.cubeList:
            if value == '':
                self.cubeList.remove(value)

    def _parseCube(self, cubeString):
        # parse cubes and splits at the ','
        self.cubeList = cubeString.split(',')
        self._cleanupList()

    def _setupSides(self):
        # Adds individual dots to their correct sides
        faces = []
        for side in self.colors:
            faces.append(side)
        for i in range(self.numOfSides):
            self.sides[faces[i]] = self.cubeList[self.dots * i:self.dots * (i + 1)]

    def _isCubeLegal(self):
        ''' checks to see if cube is legal

        Checks to make sure:
            colors are unique
            colors are part of the default palette
            colors are not used too many times
            edges are used correctly
            corners are used correctly
        '''

        if not self._areColorsUnique():  # check to make sure cube contains unique colors
            return False
        if not self._isColorInPalette():  # check to see if cube contains only colors in the default set
            return False
        if self._areValuesUsedTooManyTimes():  # check to see if every value is used the correct number of times
            return False

        # setup variables for corners and edges
        illegalMatches = {
            self.colors['f']: self.colors['b'],
            self.colors['l']: self.colors['r'],
            self.colors['t']: self.colors['u'],
            self.colors['b']: self.colors['f'],
            self.colors['r']: self.colors['l'],
            self.colors['u']: self.colors['t']}

        cornerCounter = self._setupColorCounter()
        edgeCounter = self._setupColorCounter()

        # check if corners are legal
        if self._cornersIllegal(illegalMatches, cornerCounter):
            return False

        # check if edges are legal
        if self._edgesIllegal(illegalMatches, edgeCounter):
            return False

        # check if corner and edges have caused an issue
        return True

    def _isColorInPalette(self):
        # check to make sure cube contains colors only in color palette
        for side in self.colors:
            for dot in self.sides[side]:
                if dot not in self.colors.values():
                    self.setErrorMessage('color not in set')
                    return False
        return True

    def _areValuesUsedTooManyTimes(self):
        # check to see if values are used appropriate amount of times
        if self._ColorCheck() or self._areMiddleCheck():
            return True
        return False

    def _setupColorCounter(self):
        # sets up collection of colors, with value to use as a counter
        collection = collections.OrderedDict(())
        for color in self.colors.values():
            collection[color] = 0
        return collection

    def _ColorCheck(self):
        # check to see if individual values are used too many times
        colorCount = self._setupColorCounter()
        for color in colorCount:
            for side in self.sides.values():
                colorCount[color] += side.count(color)
            if colorCount[color] != 9:
                self.setErrorMessage('value not used 9 times')
                return True
        return False

    def _areMiddleCheck(self):
        # Check to see if middle values are used correctly

        # First checks to see if middle values are used on the correct faces
        for side in self.colors:
            if self.sides[side][self.middleElement] != self.colors[side]:
                self.setErrorMessage('middle value not on correct side')
                return True

        # then checks to see if middle values are used too many times
        # i think this is redundant ask Neda
        '''middleCount = self._setupColorCounter()
        for color in middleCount:
            for side in self.sides.values():
                if side[self.middleElement] == color:
                    middleCount[color] += 1
            if middleCount[color] != 1:
                self.setErrorMessage('middle value not on correct side')
                return True'''
        return False

    def _cornersIllegal(self, illegalMatches, cornerCounter):
        # check to see if the corner pairs are illegal

        corners = [Corner('f', 'l', 't'),
                   Corner('f', 'r', 't'),
                   Corner('f', 'l', 'u'),
                   Corner('f', 'r', 'u'),
                   Corner('b', 'l', 't'),
                   Corner('b', 'r', 't'),
                   Corner('b', 'l', 'u'),
                   Corner('b', 'r', 'u')]
        cornersUsed = []
        for corner in corners:  # loop through edges, get their values in the cube and then check to see if its logical
            firstSide = self.sides[corner.firstSide]
            secondSide = self.sides[corner.secondSide]
            thirdSide = self.sides[corner.thirdSide]
            corner.firstValue = firstSide[corner.firstIndex]
            corner.secondValue = secondSide[corner.secondIndex]
            corner.thirdValue = thirdSide[corner.thirdIndex]
            cornerSides = [corner.firstValue, corner.secondValue, corner.thirdValue]
            cornerCounter[corner.firstValue] += 1
            cornerCounter[corner.secondValue] += 1
            cornerCounter[corner.thirdValue] += 1
            if cornerSides not in cornersUsed:
                cornersUsed.append(cornerSides)
            else:
                self.setErrorMessage('every corner must be added once')
                return True
            for side in cornerSides:
                if illegalMatches[side] in cornerSides:
                    self.setErrorMessage('every corner must be added once')
                    return True
        for value in cornerCounter:
            if cornerCounter[value] != 4:
                self.setErrorMessage('every corner must be added once')
        return False

    def _edgesIllegal(self, illegalMatches, edgeCounter):
        # check to see if edges are illegal
        edges = [
            Edge('f', 't'), Edge('f', 'l'),
            Edge('f', 'r'), Edge('f', 'u'),
            Edge('b', 't'), Edge('b', 'l'),
            Edge('b', 'r'), Edge('b', 'u'),
            Edge('l', 't'), Edge('l', 'u'),
            Edge('r', 't'), Edge('r', 'u')]
        edgesUsed = []
        for edge in edges:
            firstSide = self.sides[edge.firstSide]
            secondSide = self.sides[edge.secondSide]
            edge.firstValue = firstSide[edge.firstIndex]
            edge.secondValue = secondSide[edge.secondIndex]
            edgeSides = [edge.firstValue, edge.secondValue]
            edgeCounter[edge.firstValue] += 1
            edgeCounter[edge.secondValue] += 1
            if edgeSides not in edgesUsed:
                edgesUsed.append(edgeSides)
            else:
                self.setErrorMessage('every edge must be added once')
                return True
            for side in edgeSides:
                if illegalMatches[side] in edgeSides:
                    self.setErrorMessage('every edge must be added once')
                    return True
        for value in edgeCounter:
            if edgeCounter[value] != 4:
                self.setErrorMessage('every edge must be added once')
                return True
        return False

    def _getCubeType(self):
        # get cube's type -> full, spots, crosses, unknown
        if self._isFull():
            self.status = 'full'
        elif self._isSpots():
            self.status = 'spots'
        elif self._isCrosses():
            self.status = 'crosses'
        else:
            self.status = 'unknown'

    def _isFull(self):
        # if a cube is full every side is only one value
        for side in self.sides.values():
            colorsUsed = []
            for dot in side:
                if dot not in colorsUsed:
                    colorsUsed.append(dot)
            if len(colorsUsed) > 1:
                return False
        return True

    def _isCrosses(self):
        ''' if a cube is crosses, then each side consists of two colors such
            that the corner elements are one color and the remaining elements are another color
        '''

        for side in self.sides.values():
            cornerColors = []
            otherColors = []
            i = 0
            for dot in side:
                if (i % 2 == 0) and (i != self.middleElement):
                    if dot not in cornerColors:
                        cornerColors.append(dot)
                elif dot not in otherColors:
                    otherColors.append(dot)
                i += 1
            if len(cornerColors) > 1 or len(otherColors) > 1:
                return False
        return True

    def _isSpots(self):
        ''' if a cube is a spot, then each side consists of exactly two colors such
            that the middle element is one color and the remaining elements are another color
        '''

        for side in self.sides.values():
            index = 0
            colorsUsed = []
            for dot in side:
                if index == self.middleElement:  # middle of side
                    if dot in colorsUsed:
                        return False
                elif dot not in colorsUsed:
                    colorsUsed.append(dot)
                index += 1
            if len(colorsUsed) > 1:
                return False
        return True

    def _getRotationDirection(self, faceToBeRotated):
        ''' Gets direction of rotation.

        if value is lower case -> clockwise
        if value is upper case -> counter-clockwise

        '''

        rotation = 'none'
        if faceToBeRotated.isupper():  # counter clockwise
            rotation = 'counter-clockwise'
        elif faceToBeRotated.islower():  # clockwise
            rotation = 'clockwise'
        return rotation

    def _rotateCallingFace(self, face, rotation):
        ''' Rotates face

        Does this by converting the contents of a face to a 2D list and then
        performs a clockwise or counter clockwise rotation on that and then
        converts the 2D list back to a 1D list

        '''

        convertedFace = convertListTo2DList(3, face)
        rotatedFace2D = ''
        if rotation == 'clockwise':
            rotatedFace2D = rotateClockwise(convertedFace)
        elif rotation == 'counter-clockwise':
            rotatedFace2D = rotateCounterclockwise(convertedFace)
        rotatedFace = convert2DListToList(rotatedFace2D)
        return rotatedFace

    def _rotateOtherFaces(self, faceToBeRotated, rotation):
        ''' Rotates faces other than the face being rotated

        For example, if you rotate the front clockwise
        Then the under side will be rotated into the left side
        The left side will be rotated into the top side
        The top side will be rotated into the right side
        The right side will be rotated into the under side

        '''

        holderSides = collections.OrderedDict(())
        faceMatchups = collections.OrderedDict((
            ('f', ['l', 't', 'r', 'u']),
            ('l', ['b', 't', 'f', 'u']),
            ('b', ['r', 't', 'l', 'u']),
            ('r', ['f', 't', 'b', 'u']),
            ('t', ['l', 'b', 'r', 'f']),
            ('u', ['l', 'f', 'r', 'b'])))
        facesToRotate = faceMatchups[faceToBeRotated]
        for index in range(4):
            holderSideValue = facesToRotate[index]  # gets the side that will be rotated into
            if rotation == 'clockwise':

                # gets the side that will be moving into the holding side
                if index == 0:  # if at the beginning of the list the prior face will be at the end of the list
                    movingSideValue = facesToRotate[len(facesToRotate) - 1]  # sets moving side to the name of the face
                else:
                    movingSideValue = facesToRotate[index - 1]  # sets moving side to the name of the face

                # Gets appropriate rotating function
                if faceToBeRotated == 'f':
                    holderSides[holderSideValue] = self._rotateFrontClockwise(index, holderSideValue, movingSideValue)
                elif faceToBeRotated == 'l':
                    holderSides[holderSideValue] = self._rotateLeftClockwise(index, holderSideValue, movingSideValue)
                elif faceToBeRotated == 'r':
                    holderSides[holderSideValue] = self._rotateRightClockwise(index, holderSideValue, movingSideValue)
                elif faceToBeRotated == 't':
                    holderSides[holderSideValue] = self._rotateTop(holderSideValue, movingSideValue)
                elif faceToBeRotated == 'u':
                    holderSides[holderSideValue] = self._rotateUnder(holderSideValue, movingSideValue)
                elif faceToBeRotated == 'b':
                    holderSides[holderSideValue] = self._rotateBackClockwise(index, holderSideValue, movingSideValue)

            elif rotation == 'counter-clockwise':

                # gets the side that will be moving into the holding side
                if index == len(facesToRotate) - 1:
                    movingSideValue = facesToRotate[0]
                else:
                    movingSideValue = facesToRotate[index + 1]

                # Gets appropriate rotating function
                if faceToBeRotated == 'f':
                    holderSides[holderSideValue] = self._rotateFrontCounterClockwise(index, holderSideValue,
                                                                                     movingSideValue)
                elif faceToBeRotated == 'l':
                    holderSides[holderSideValue] = self._rotateLeftCounterClockwise(index, holderSideValue,
                                                                                    movingSideValue)
                elif faceToBeRotated == 'r':
                    holderSides[holderSideValue] = self._rotateRightCounterClockwise(index, holderSideValue,
                                                                                     movingSideValue)
                elif faceToBeRotated == 't':
                    holderSides[holderSideValue] = self._rotateTop(holderSideValue, movingSideValue)
                elif faceToBeRotated == 'u':
                    holderSides[holderSideValue] = self._rotateUnder(holderSideValue, movingSideValue)
                elif faceToBeRotated == 'b':
                    holderSides[holderSideValue] = self._rotateBackCounterClockwise(index, holderSideValue,
                                                                                    movingSideValue)

        return holderSides

    def _rotateFrontClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Front Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:
            holderSide[2] = movingSide[0]
            holderSide[5] = movingSide[1]
            holderSide[8] = movingSide[2]
        elif index == 1:
            holderSide[8] = movingSide[2]
            holderSide[7] = movingSide[5]
            holderSide[6] = movingSide[8]
        elif index == 2:
            holderSide[0] = movingSide[6]
            holderSide[3] = movingSide[7]
            holderSide[6] = movingSide[8]
        elif index == 3:
            holderSide[2] = movingSide[0]
            holderSide[1] = movingSide[3]
            holderSide[0] = movingSide[6]
        return holderSide

    def _rotateLeftClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Left Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:  # holder = back, moving = under
            holderSide[2] = movingSide[6]
            holderSide[5] = movingSide[3]
            holderSide[8] = movingSide[0]
        elif index == 1:  # holder = top, moving = back
            holderSide[6] = movingSide[2]
            holderSide[3] = movingSide[5]
            holderSide[0] = movingSide[8]
        elif index == 2:  # holder = front, moving = top
            holderSide[6] = movingSide[6]
            holderSide[3] = movingSide[3]
            holderSide[0] = movingSide[0]
        elif index == 3:  # holder = under, moving = front
            holderSide[6] = movingSide[6]
            holderSide[3] = movingSide[3]
            holderSide[0] = movingSide[0]
        return holderSide

    def _rotateRightClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Right Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:  # holder = front, moving = under
            holderSide[2] = movingSide[2]
            holderSide[5] = movingSide[5]
            holderSide[8] = movingSide[8]
        elif index == 1:  # holder = top, moving = front
            holderSide[2] = movingSide[2]
            holderSide[5] = movingSide[5]
            holderSide[8] = movingSide[8]
        elif index == 2:  # holder = back, moving = top
            holderSide[0] = movingSide[8]
            holderSide[3] = movingSide[5]
            holderSide[6] = movingSide[2]
        elif index == 3:  # holder = under, moving = back
            holderSide[2] = movingSide[6]
            holderSide[5] = movingSide[3]
            holderSide[8] = movingSide[0]
        return holderSide

    def _rotateTop(self, holderSideValue, movingSideValue):
        # Rotates faces affected by a top rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]

        holderSide[0] = movingSide[0]
        holderSide[1] = movingSide[1]
        holderSide[2] = movingSide[2]

        return holderSide

    def _rotateUnder(self, holderSideValue, movingSideValue):
        # Rotates faces affected by a under rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]

        holderSide[6] = movingSide[6]
        holderSide[7] = movingSide[7]
        holderSide[8] = movingSide[8]

        return holderSide

    def _rotateBackClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Back Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]

        if index == 0:  # holding = right, moving = under
            holderSide[8] = movingSide[6]
            holderSide[5] = movingSide[7]
            holderSide[2] = movingSide[8]
        elif index == 1:  # holding = top, moving = right
            holderSide[0] = movingSide[2]
            holderSide[1] = movingSide[5]
            holderSide[2] = movingSide[8]
        elif index == 2:  # holding = left, moving = top
            holderSide[6] = movingSide[0]
            holderSide[3] = movingSide[1]
            holderSide[0] = movingSide[2]
        elif index == 3:  # holding = under, moving = left
            holderSide[6] = movingSide[0]
            holderSide[7] = movingSide[3]
            holderSide[8] = movingSide[6]

        return holderSide

    def _rotateFrontCounterClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Front Counter Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:  # holder = left, moving = top
            holderSide[2] = movingSide[8]
            holderSide[5] = movingSide[7]
            holderSide[8] = movingSide[6]
        elif index == 1:  # holder = top, moving = right
            holderSide[8] = movingSide[6]
            holderSide[7] = movingSide[3]
            holderSide[6] = movingSide[0]
        elif index == 2:  # holder = right, moving = under
            holderSide[6] = movingSide[0]
            holderSide[3] = movingSide[1]
            holderSide[0] = movingSide[2]
        elif index == 3:  # holder = under, moving = left
            holderSide[2] = movingSide[8]
            holderSide[1] = movingSide[5]
            holderSide[0] = movingSide[2]
        return holderSide

    def _rotateLeftCounterClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Left Counter Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:  # holder = back, moving = top
            holderSide[2] = movingSide[6]
            holderSide[5] = movingSide[3]
            holderSide[8] = movingSide[0]
        elif index == 1:  # holder = top, moving = front
            holderSide[0] = movingSide[0]
            holderSide[3] = movingSide[3]
            holderSide[6] = movingSide[6]
        elif index == 2:  # holder = front, moving = under
            holderSide[0] = movingSide[0]
            holderSide[3] = movingSide[3]
            holderSide[6] = movingSide[6]
        elif index == 3:  # holder = under, moving = back
            holderSide[0] = movingSide[8]
            holderSide[3] = movingSide[5]
            holderSide[6] = movingSide[2]
        return holderSide

    def _rotateRightCounterClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Right Counter Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:  # holder = front, moving = top
            holderSide[2] = movingSide[2]
            holderSide[5] = movingSide[5]
            holderSide[8] = movingSide[8]
        elif index == 1:  # holder = top, moving = back
            holderSide[2] = movingSide[6]
            holderSide[5] = movingSide[3]
            holderSide[8] = movingSide[0]
        elif index == 2:  # holder = back, moving = under
            holderSide[0] = movingSide[8]
            holderSide[3] = movingSide[5]
            holderSide[6] = movingSide[2]
        elif index == 3:  # holder = under, moving = front
            holderSide[2] = movingSide[2]
            holderSide[5] = movingSide[5]
            holderSide[8] = movingSide[8]
        return holderSide

    def _rotateBackCounterClockwise(self, index, holderSideValue, movingSideValue):
        # Rotates faces affected by a Back Counter Clockwise rotation
        holderSide = self.sides[holderSideValue][:]
        movingSide = self.sides[movingSideValue][:]
        if index == 0:  # holder = right, moving = top
            holderSide[2] = movingSide[0]
            holderSide[5] = movingSide[1]
            holderSide[8] = movingSide[2]
        elif index == 1:  # holder = top, moving = left
            holderSide[2] = movingSide[0]
            holderSide[1] = movingSide[3]
            holderSide[0] = movingSide[6]
        elif index == 2:  # holder = left, moving = under
            holderSide[0] = movingSide[6]
            holderSide[3] = movingSide[7]
            holderSide[6] = movingSide[8]
        elif index == 3:  # holder = under, moving = right
            holderSide[6] = movingSide[8]
            holderSide[7] = movingSide[5]
            holderSide[8] = movingSide[2]
        return holderSide

    def _transition(self):
        ''' Performs scramble method transition

            Will create a copy of the original sides collection
            to reset the cube after each rotation.

            Will create a dictionary to hold the randomness count
            of each rotation

            Then will loop through each rotation and perform it on a default cube

            Then figures out the minimum randomness and chooses the rotation
        '''
        randomnessCount = collections.OrderedDict()
        auxSides = self.sides.copy()

        # calculates randomness for each rotation
        for side in self.sides:
            for x in range(2):
                if x == 1:
                    side = side.upper()
                self.rotateCube(side)
                self._randomness()
                randomnessCount[side] = self.randomness

                self.randomness = 100
                self.sides = auxSides.copy()

        # picks smallest randomness and returns that rotation
        minValue = 100
        minKey = []
        for key in randomnessCount:
            value = randomnessCount[key]
            if value == minValue:
                minKey.append(key)
            if value < minValue:
                minKey = [key]
                minValue = value

        # if multiple rotations have the same randomness pick from them randomly
        if len(minKey) > 1:
            randomNum = randint(0, len(minKey) - 1)
            minRotation = minKey[randomNum]
        else:
            minRotation = minKey[0]
        return minRotation

    def _isInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def _randomness(self):
        self.randomness = int(ceil(self._randomnessSummation() * (1 / 6.0 ** 3) * 100))

    def _randomnessSummation(self):
        sumValue = 0
        for dots in self.sides.values():
            x = 1
            for dot in dots:
                currentList = dots[x:]
                sumValue += currentList.count(dot)
                x += 1
        return sumValue

    def setErrorMessage(self, errorMessage):
        # If cube is in an error state, set status to error and set error to its corresponding error message
        self.status = ERROR
        self.error = errorMessage
