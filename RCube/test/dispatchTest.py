import unittest
import httplib
import json


class DispatchTest(unittest.TestCase):

    def setUp(self):
        self.key = "status"
        self.errorValue = "error:"
        self.operation = "op"
        self.scramble = "create"

    @classmethod
    def setUpClass(cls):
        cls.ERROR = "error:"
        cls.DEFAULT_SIZE = 3
        cls.MICROSERVICE_PATH = "/rcube?"
        cls.MICROSERVICE_URL = "127.0.0.1"
        cls.MICROSERVICE_PORT = 5000

    #         cls.MICFROSERVICE_URL="umphrda-rcube.mybluemix.net"
    #         cls.MICROSERVICE_PORT = 80

    def httpGetAndResponse(self, queryString):
        # noinspection PySingleQuotedDocstring,PySingleQuotedDocstring
        '''Make HTTP request to URL:PORT for /rcube?querystring; result is a JSON string'''
        try:
            theConnection = httplib.HTTPConnection(self.MICROSERVICE_URL, self.MICROSERVICE_PORT)
            theConnection.request("GET", self.MICROSERVICE_PATH + queryString.replace(" ", ""))
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            theStringResponse = "{'diagnostic': 'error: " + str(e) + "'}"
            return theStringResponse

    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if isinstance(unicodeDictionary[element], unicode):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result

    # Acceptance Tests
    #
    # 100 create cube - basic functionality
    # 200 check cube
    # 300 rotate cube
    # 400 scramble cube
    # Desired level of confidence: boundary value analysis
    # Analysis
    # inputs:     http:// ...myURL... /httpGetAndResponse?parm
    #            parm is a string consisting of key-value pairs
    #            At a minimum, parm must contain one key of "op"
    #
    # outputs:    A JSON string containing, at a minimum, a key of "status"
    #
    # Happy path
    #
    #    || Assignment 4 Tests ||
    #
    #     test100_010_ShouldReturnSuccessKey
    #      input:   parm having at least one element with a key of "op" and value "create"
    #      output:  JSON string containing a key of "status"
    #
    #    test100_020_ShouldReturnSuccessAndCubeKey
    #      input:   parm having at least one element with a key of "op" and value "create"
    #      output:  JSON string containing a key of "status" and key of "cube"
    #
    #    test100_030_ShouldReturnSuccessAndCubeandDefaultCubeInsidesKey
    #      input:  parm having at least one element with a key of "op" and value "create"
    #      output:  JSON string containing a key of "status" and key of "cube" and default sides
    #
    #    test100_040_ShouldReturnCustomCubeInsidesKey
    #      input:  parm having at least one element with custom valid sides
    #      output:  JSON string containing a key of "status" and key of "cube" and custom sides
    #
    #    test100_050_ShouldReturnCustomCubeInsidesKey
    #      input:   parm having at least one element with custom valid sides, except for under
    #      output:  JSON string containing a key of "status" and key of "cube" and custom sides, default for under side
    #
    #    test100_060_ShouldReturnCubeWithSameSidesVaryingCase
    #      input:   parm having at least one element with custom sides that have the same value but with varying cases
    #      output:  JSON string containing a key of "status" and key of "cube" and custom sides
    #
    #    || Assignment 5 Tests ||
    #
    #    test100_070_ShouldReturnFull
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "full"
    #
    #    test100_075_ShouldReturnFull
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "full"
    #
    #    test100_080_ShouldReturnSpots
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "spots"
    #
    #    test100_085_ShouldReturnSpots
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "spots"
    #
    #    test100_090_ShouldReturnCrossess
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "crosses"
    #
    #    test100_095_ShouldReturnCrossess
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "crosses"
    #
    #    test100_100_ShouldReturnUnknown
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "unknown"
    #
    #    test100_105_ShouldReturnUnknown
    #      input:   parm having op = check, a normal cube, and normal sides
    #      output:  JSON string containing a key of "status" with value "unknown"
    #
    #    || Assignment 6 Tests ||
    # 
    #    test100_110_ShouldReturnRotate_F_full
    #      input:   parm having op = rotate, a normal cube, and normal sides, rotates front counter clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_115_ShouldReturnRotate_f_full
    #      input:   parm having op = rotate, a normal cube, and normal sides, rotates front clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_120_ShouldReturnRotate_R_full
    #      input:   parm having op = rotate, a normal cube, and normal sides, rotates right counter clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_125_ShouldReturnRotate_r_full
    #      input:   parm having op = rotate, a normal cube, and normal sides, rotates right clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_130_ShouldReturnRotate_T_full
    #      input:   parm having op = rotate, a normal cube, and normal sides, rotates top counter clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_130_ShouldReturnRotate_t_full
    #      input:   parm having op = rotate, a normal cube, and normal sides, rotates top clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_130_ShouldReturnRotate_r_mixed
    #      input:   parm having op = rotate, a mixed cube, and normal sides, rotates right  clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    test100_140_ShouldReturnRotate
    #      input:   parm having op = rotate, a mixed cube, and normal sides, rotates front counter clockwise
    #      output:  JSON string containing a key of "status" with value "rotated" and key 'cube' with value of rotated cube
    #
    #    || Assignment 7 Tests ||
    #
    #    test100_150_ShouldReturnScrambled
    #      input:   parm having op = scramble
    #      output:  JSON string containing a key of "status" with value "Scrambled 100" and key ''rotations'' with value of empty list
    #
    #    test100_150_ShouldReturnScrambledWithRandomLength0
    #      input:   parm having op = scramble
    #      output:  JSON string containing a key of "status" with value "Scrambled 100" and key 'rotations' with value of empty list
    #
    #    test100_150_ShouldReturnScrambledWithRandomLength1
    #      input:   parm having op = scramble and n = 1
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    #    test100_150_ShouldReturnScrambledPercent
    #      input:   parm having op = scramble and n = 1
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    #    test100_150_ShouldTestRandomMethod
    #      input:   parm having op = scramble and n = 1 run 120 times
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    #    test100_150_ShouldTestTransitionMethod
    #      input:   parm having op = scramble and n = 1 run 120 times
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    #    test100_150_
    #      input:   parm having op = scramble and n = 1
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    #    test100_150_
    #      input:   parm having op = scramble and n = 1 run 120 times
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    #    test100_150_
    #      input:   parm having op = scramble and n = 1 run 120 times
    #      output:  JSON string containing a key of "status" with value not "Scrambled 100" and key 'rotations' with value of list of length 1
    #
    # Sad path
    #
    #    || Assignment 4 Tests ||
    #
    #    test100_900_ShouldReturnErrorOnEmptyParm
    #      input:   no string
    #      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
    #
    #    test100_910_ShouldReturnErrorOnMissingOp
    #      input:   valid parm string with at least one key-value pair, no key of "op"
    #      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
    #
    #    test100_920_ShouldReturnErrorOnDuplicateSide <<edited for assignment 5>>
    #      input:   two sides of the same value
    #      output:  dictionary consisting of an element with a key of "status" and value of "error: duplicate side"
    #
    #    test100_930_ShouldReturnErrorOnDuplicateSide
    #      input:   one custom sides of green, and default side of green
    #      output:  dictionary consisting of an element with a key of "status" and value of "error: duplicate side"
    #
    #    test100_940_ShouldReturnErrorColorMissing
    #      input:   parm having at least one element with blank custom sides
    #      output:  JSON string containing a key of "status" with 'error: missing color'
    #
    #    || Assignment 5 Tests ||
    #
    #    test100_950_ShouldReturnErrorOnMissingOp
    #      input:   parm having op= incorrect value
    #      output:  JSON string containing a key of "status" with 'error: missing op'
    #
    #    test100_960_ShouldReturnErrorOnMissingOp
    #      input:   parm having op= incorrect value #2
    #      output:  JSON string containing a key of "status" with 'error: missing op'
    #
    #    test100_965_ShouldReturnCubeMustBeSpecified
    #      input:   parm having just check with nothing else
    #      output:  JSON string containing a key of "status" with 'error: cube must be specified'
    #
    #    test100_970_ShouldReturnErrorOnIncorrectSize
    #      input:   parm having cube not containing 54 different elements
    #      output:  JSON string containing a key of "status" with 'error: cube is not sized properly'
    #
    #    test100_975_ShouldReturnErrorOnIncorrectSize
    #      input:   parm having cube not containing 54 different elements
    #      output:  JSON string containing a key of "status" with 'error: cube is not sized properly'
    #
    #    test100_980_ShouldReturnErrorOnErrorCubeColorNotInDefault
    #      input:   parm having cube having an element not in the default colors
    #      output:  JSON string containing a key of "status" with 'error: color not in set'
    #
    #    test100_982_ShouldReturnErrorOnerrorCubeNonUniqueColors
    #      input:   parm having cube having an color used more than once in the default color set
    #      output:  JSON string containing a key of "status" with 'error: duplicate side'
    #
    #    test100_984_ShouldReturnErrorOnErrorCubeValueNotUsed9Times
    #      input:   parm having cube having an element not used 9 times
    #      output:  JSON string containing a key of "status" with 'error: value not used 9 times'
    #
    #    test100_986_ShouldReturnErrorOnErrorCubeMiddleValueIncorrect
    #      input:   parm having cube having an center dot not the value of the face it is on
    #      output:  JSON string containing a key of "status" with 'error: middle value not on correct side'
    #
    #    test100_988_ShouldReturnErrorOnErrorCubeCornersNotCorrect
    #      input:   parm having cube having illegal corners
    #      output:  JSON string containing a key of "status" with 'error: every corner must be added once'
    #
    #    test100_990_ShouldReturnErrorOnErrorCubeEdgesNotCorrect
    #      input:   parm having cube having illegal edges
    #      output:  JSON string containing a key of "status" with 'error: every edge must be added once'
    #
    #    test100_992_ShouldReturnErrorOnErrorCubeEdgesNotCorrect
    #      input:   parm having cube having illegal corners
    #      output:  JSON string containing a key of "status" with 'error: every edge or corner must be added once'
    #
    #    || Assignment 6 ||
    #
    #    test100_995_ShouldReturnErrorOnRotateValueNotUsed9Times
    #      input:  parm having cube having an element not used 9 times
    #      output: JSON string containing a key of "status" with 'error: value not used 9 times'
    #
    #    test100_996_ShouldReturnErrorOnRotateNonUniqueColors
    #      input:  parm having cube with non unique colors
    #      output: JSON string containing a key of "status" with 'error: duplicate side'
    #
    #    test100_997_ShouldReturnErrorOnRotateIncorectSize
    #      input:  parm having cube with incorrect size
    #      output: JSON string containing a key of "status" with 'error: cube is not sized properly'
    #
    #    test100_998_ShouldReturnErrorOnRotateMissingCube
    #      input:  parm not containing cube
    #      output: JSON string containing a key of "status" with 'error: cube must be specified'
    #
    #    test100_999_ShouldReturnErrorOnRotateColorNotInSet
    #      input:  parm having cube with color not in default set
    #      output: JSON string containing a key of "status" with 'error: color not in set'
    #
    #    test100_9000_ShouldReturnErrorOnRotateMiddleValueUsedMoreThanOnce
    #      input:  parm having cube with multiple of the same middle values
    #      output: JSON string containing a key of "status" with 'error: middel value not on correct side'
    #
    #    test100_9010_ShouldReturnErrorOnRotateCubeNotSpecified
    #      input:  parm having cube with no cube
    #      output: JSON string containing a key of "status" with 'error: cube must be specified'
    #
    #    test100_9020_ShouldReturnErrorOnRotateFaceUnknown
    #      input:  parm having cube with illegal face to be rotated
    #      output: JSON string containing a key of "status" with 'error: face unknown'
    #
    #    test100_9025_ShouldReturnErrorOnRotateFaceMissing
    #      input:  parm having cube with missing face value
    #      output: JSON string containing a key of "status" with 'error: face missing'
    #
    #    test100_9030_ShouldReturnErrorOnRotateEdge
    #      input:  parm having cube with illegal edge
    #      output: JSON string containing a key of "status" with 'error: every edge must be added once'
    #
    #    test100_9040_ShouldReturnErrorOnRotateCorner
    #      input:  parm having cube with illegal corner
    #      output: JSON string containing a key of "status" with 'error: every corner must be added once'
    #
    #    || Assignment 7 ||
    #
    #    test100_9050_ShouldReturnErrorOnScrambleForNegativeN
    #      input:   parm having op = scramble and n = -1
    #      output:  JSON string containing a key of "status" with value not "error: n must be an integer between 0 to 99" 
    #    test100_9050_ShouldReturnErrorOnScrambleForNTooBig
    #      input:   parm having op = scramble and n = 100
    #      output:  JSON string containing a key of "status" with value not "error: n must be an integer between 0 to 99" 
    #    test100_9050_ShouldReturnErrorOnScrambleForNNotInt
    #      input:   parm having op = scramble and n = 'a'
    #      output:  JSON string containing a key of "status" with value not "error: n must be an integer between 0 to 99" 

    
    def test100_010_ShouldReturnSuccessKey(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)

    def test100_020_ShouldReturnSuccessAndCubeKey(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:8])
        self.assertIn('cube', resultDict)

    def test100_030_ShouldReturnSuccessAndCubeandDefaultCubeInsidesKey(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:8])
        self.assertIn('cube', resultDict)
        cubeInsides = [
            'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
            'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow',
            'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
            'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
            'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red',
            'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'
        ]
        self.assertEquals(cubeInsides, resultDict['cube'])

    def test100_040_ShouldReturnCustomCubeInsidesKey(self):
        queryString = "op=create&r=r&l=l&t=t&u=u&f=f&b=b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:8])
        self.assertIn('cube', resultDict)
        expectedDictionary = {'status': 'created',
                              'cube': ['f', 'f', 'f', 'f',
                                       'f', 'f', 'f', 'f', 'f',
                                       'r', 'r', 'r', 'r', 'r', 'r',
                                       'r', 'r', 'r', 'b', 'b', 'b',
                                       'b', 'b', 'b', 'b', 'b', 'b',
                                       'l', 'l', 'l', 'l', 'l', 'l',
                                       'l', 'l', 'l', 't', 't', 't',
                                       't', 't', 't', 't', 't', 't',
                                       'u', 'u', 'u', 'u', 'u', 'u',
                                       'u', 'u', 'u', ]
                              }
        self.assertEquals(expectedDictionary, resultDict)

    def test100_050_ShouldReturnCustomCubeInsidesKey(self):
        queryString = "op=create&r=r&l=l&t=t&under=42&f=f&b=b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:8])
        self.assertIn('cube', resultDict)
        expectedDictionary = {'status': 'created',
                              'cube': ['f', 'f', 'f', 'f',
                                       'f', 'f', 'f', 'f', 'f',
                                       'r', 'r', 'r', 'r', 'r', 'r',
                                       'r', 'r', 'r', 'b', 'b', 'b',
                                       'b', 'b', 'b', 'b', 'b', 'b',
                                       'l', 'l', 'l', 'l', 'l', 'l',
                                       'l', 'l', 'l', 't', 't', 't',
                                       't', 't', 't', 't', 't', 't',
                                       'orange', 'orange', 'orange', 'orange', 'orange', 'orange',
                                       'orange', 'orange', 'orange', ]
                              }
        self.assertEquals(expectedDictionary, resultDict)

    def test100_060_ShouldReturnCubeWithSameSidesVaryingCase(self):
        queryString = "op=create&r=red&l=Red&t=rEd&u=reD&f=RED&b=REd"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:8])
        self.assertIn('cube', resultDict)
        expectedDictionary = {'status': 'created',
                              'cube': [
                                  'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED',
                                  'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red',
                                  'REd', 'REd', 'REd', 'REd', 'REd', 'REd', 'REd', 'REd', 'REd',
                                  'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red',
                                  'rEd', 'rEd', 'rEd', 'rEd', 'rEd', 'rEd', 'rEd', 'rEd', 'rEd',
                                  'reD', 'reD', 'reD', 'reD', 'reD', 'reD', 'reD', 'reD', 'reD']
                              }
        self.assertEquals(expectedDictionary, resultDict)

    def test200_010_ShouldReturnFull(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('full', resultDict['status'])

    def test200_015_ShouldReturnFull(self):
        queryString = "op=check&f=front&r=r&b=b&l=l&t=t&u=u&cube=front,front,front,front,front,front,front,front,front,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('full', resultDict['status'])

    def test200_020_ShouldReturnSpots(self):
        queryString = "op=check&f=w&r=g&b=y&l=b&t=r&u=o&cube=y,y,y,y,w,y,y,y,y,o,o,o,o,g,o,o,o,o,w,w,w,w,y,w,w,w,w,r,r,r,r,b,r,r,r,r,b,b,b,b,r,b,b,b,b,g,g,g,g,o,g,g,g,g"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('spots', resultDict['status'])

    def test200_25_ShouldReturnSpots(self):
        queryString = "op=check&f=y&r=o&b=w&l=r&t=b&u=g&cube=r,r,r,r,y,r,r,r,r,b,b,b,b,o,b,b,b,b,o,o,o,o,w,o,o,o,o,g,g,g,g,r,g,g,g,g,w,w,w,w,b,w,w,w,w,y,y,y,y,g,y,y,y,y"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('spots', resultDict['status'])

    def test200_030_ShouldReturnCrossess(self):
        queryString = "op=check&f=w&r=g&b=y&l=b&t=r&u=o&cube=r,w,r,w,w,w,r,w,r,w,g,w,g,g,g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b,b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('crosses', resultDict['status'])

    def test200_035_ShouldReturnCrossess(self):
        queryString = "op=check&f=r&r=w&b=o&l=y&t=g&u=b&cube=w,r,w,r,r,r,w,r,w,g,w,g,w,w,w,g,w,g,y,o,y,o,o,o,y,o,y,b,y,b,y,y,y,b,y,b,r,g,r,g,g,g,r,g,r,o,b,o,b,b,b,o,b,o "
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('crosses', resultDict['status'])

    def test200_040_ShouldReturnUnknown(self):
        queryString = "op=check&f=o&r=b&b=r&l=g&t=y&u=w&cube=y,y,b,b,o,g,o,b,w,r,b,b,r,b,w,b,w,r,o,g,g,o,r,g,g,b,b,y,y,o,y,g,o,o,o,g,r,w,w,r,y,r,g,o,y,w,y,r,g,w,r,y,w,w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('unknown', resultDict['status'])

    def test200_045_ShouldReturnUnknown(self):
        queryString = "op=check&f=o&r=b&b=r&l=g&t=test&u=w&cube=test,test,b,b,o,g,o,b,w, r,b,b,r,b,w,b,w,r,o,g,g,o,r,g,g,b,b,test,test,o,test,g,o,o,o,g,r,w,w,r,test,r,g,o,test,w,test,r,g,w,r,test,w,w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('unknown', resultDict['status'])

    def test300_010_ShouldReturnRotate_F_full(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=F"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'y', 'r', 'r', 'y', 'r', 'r', 'y', 'r', 'r',
                'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'o', 'o', 'w', 'o', 'o', 'w',
                'o', 'o', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'r', 'r', 'r', 'o', 'o', 'o', 'y', 'y', 'y', 'y', 'y', 'y']
        self.assertEquals(cube, resultDict['cube'])

    def test300_015_ShouldReturnRotate_f_full(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
                'w', 'r', 'r', 'w', 'r', 'r', 'w', 'r', 'r',
                'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
                'o', 'o', 'y', 'o', 'o', 'y', 'o', 'o', 'y',
                'w', 'w', 'w', 'w', 'w', 'w', 'o', 'o', 'o',
                'r', 'r', 'r', 'y', 'y', 'y', 'y', 'y', 'y']
        self.assertEquals(cube, resultDict['cube'])

    def test300_020_ShouldReturnRotate_R_full(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=R"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['g', 'g', 'w', 'g', 'g', 'w', 'g', 'g', 'w',
                'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
                'y', 'b', 'b', 'y', 'b', 'b', 'y', 'b', 'b',
                'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
                'w', 'w', 'b', 'w', 'w', 'b', 'w', 'w', 'b',
                'y', 'y', 'g', 'y', 'y', 'g', 'y', 'y', 'g']
        self.assertEquals(cube, resultDict['cube'])

    def test300_025_ShouldReturnRotate_r_full(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['g', 'g', 'y', 'g', 'g', 'y', 'g', 'g', 'y',
                'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
                'w', 'b', 'b', 'w', 'b', 'b', 'w', 'b', 'b',
                'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
                'w', 'w', 'g', 'w', 'w', 'g', 'w', 'w', 'g',
                'y', 'y', 'b', 'y', 'y', 'b', 'y', 'y', 'b']
        self.assertEquals(cube, resultDict['cube'])

    def test300_030_ShouldReturnRotate_T_full(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=T"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['o', 'o', 'o', 'g', 'g', 'g', 'g', 'g', 'g',
                'g', 'g', 'g', 'r', 'r', 'r', 'r', 'r', 'r',
                'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b',
                'b', 'b', 'b', 'o', 'o', 'o', 'o', 'o', 'o',
                'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
                'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
        self.assertEquals(cube, resultDict['cube'])

    def test300_035_ShouldReturnRotate_t_full(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=t"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g',
                'b', 'b', 'b', 'r', 'r', 'r', 'r', 'r', 'r',
                'o', 'o', 'o', 'b', 'b', 'b', 'b', 'b', 'b',
                'g', 'g', 'g', 'o', 'o', 'o', 'o', 'o', 'o',
                'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
                'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
        self.assertEquals(cube, resultDict['cube'])

    def test300_040_ShouldReturnRotate_r_mixed(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=r,w,w,r,g,w,g,y,b,b,b,r,g,r,r,y,y,w,b,o,o,w,b,o,g,r,g,b,o,y,y,o,g,w,g,o,y,w,w,g,w,o,g,b,o,y,r,r,y,y,b,r,b,o&face=r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('rotated', resultDict['status'])
        cube = ['r', 'w', 'r', 'r', 'g', 'b', 'g', 'y', 'o',
                'y', 'g', 'b', 'y', 'r', 'b', 'w', 'r', 'r',
                'o', 'o', 'o', 'o', 'b', 'o', 'w', 'r', 'g',
                'b', 'o', 'y', 'y', 'o', 'g', 'w', 'g', 'o',
                'y', 'w', 'w', 'g', 'w', 'w', 'g', 'b', 'b',
                'y', 'r', 'g', 'y', 'y', 'w', 'r', 'b', 'b']
        self.assertEquals(cube, resultDict['cube'])

    def test300_050_ShouldReturnRotate_f_mixed(self):
        queryString = 'op=rotate&f=green&r=yellow&b=blue&l=white&t=red&u=orange&\
            cube=red,yellow,blue,blue,green,orange,blue,red,green,\
            yellow,orange,white,green,yellow,yellow,yellow,red,yellow,\
            red,white,orange,blue,blue,green,green,white,red,\
            green,green,green,red,white,orange,blue,white,orange,\
            white,green,blue,yellow,red,white,white,orange,orange,\
            white,yellow,orange,red,orange,blue,yellow,blue,red\
            &face=f'

        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        cube = ['blue', 'blue', 'red', 'red', 'green', 'yellow', 'green', 'orange', 'blue',
                'white', 'orange', 'white', 'orange', 'yellow', 'yellow', 'orange', 'red', 'yellow',
                'red', 'white', 'orange', 'blue', 'blue', 'green', 'green', 'white', 'red',
                'green', 'green', 'white', 'red', 'white', 'yellow', 'blue', 'white', 'orange',
                'white', 'green', 'blue', 'yellow', 'red', 'white', 'orange', 'orange', 'green',
                'yellow', 'green', 'yellow', 'red', 'orange', 'blue', 'yellow', 'blue', 'red']
        self.assertEquals(cube, resultDict['cube'])

    def test300_060_ShouldReturnRotate_F_full(self):
        queryString = 'op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,w,r,r,w,r,r,w,r,r,b,b,b,b,b,b,b,b,b,o,o,y,o,o,y,o,o,y,w,w,w,w,w,w,o,o,o,r,r,r,y,y,y,y,y,y&face=F'

        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        cube = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 
                'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 
                'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 
                'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 
                'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
        self.assertEquals(cube, resultDict['cube'])
    
    def test400_010_ShouldReturnScrambled(self):
        queryString = 'op=scramble'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        
        expectedDict = {'status': 'scrambled 100', 'rotations': []}
        self.assertEquals(resultDict, expectedDict)
    
    def test400_020_ShouldReturnScrambledWithRandomLength0(self):
        queryString = 'op=scramble'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        
        self.assertEquals(len(resultDict['rotations']), 0)   

    def test400_030_ShouldReturnScrambledWithRandomLength1(self):
        queryString = 'op=scramble&n=1'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        
        self.assertEquals(len(resultDict['rotations']), 1)   
    
    def test400_040_ShouldReturnScrambledPercent(self):
        queryString = 'op=scramble&n=1'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertNotEquals(resultDict['status'], 'scrambled 100')   
    
    def test400_050_ShouldTestRandomMethod(self):
        queryString = 'op=scramble&method=random&n=1'
        count = {'f':0,'l':0,'r':0,'b':0,'t':0,'u':0,
                 'F':0,'L':0,'R':0,'B':0,'T':0,'U':0}
        for _ in range(120):
            resultString = self.httpGetAndResponse(queryString)
            resultDict = self.string2dict(resultString)
            count[resultDict['rotations'][0]] += 1
        for value in count.values():
            self.assertTrue(4 <= value <= 20)   
    
    def test400_060_ShouldTestTransitionMethod(self):
        queryString = 'op=scramble&method=transition&n=1'
        count = {'f':0,'l':0,'r':0,'b':0,'t':0,'u':0,
                 'F':0,'L':0,'R':0,'B':0,'T':0,'U':0}
        for _ in range(120):
            resultString = self.httpGetAndResponse(queryString)
            resultDict = self.string2dict(resultString)
            count[resultDict['rotations'][0]] += 1
        for value in count.values():
            self.assertTrue(4 <= value <= 20)   
    
    def test400_070_TestRandomMethodCanPossiblyBe100(self):
        queryString = 'op=scramble&method=random&n=2'
        is100 = False
        for _ in range(120):
            resultString = self.httpGetAndResponse(queryString)
            resultDict = self.string2dict(resultString)
            if resultDict['status'] == 'scrambled 100':
                is100 = True  
                break
        self.assertTrue(is100)      
    
    def test_400_080_TestTransitionMethodCantPossiblyBe100(self):
        queryString = 'op=scramble&method=transition&n=2'
        is100 = False
        for _ in range(120):
            resultString = self.httpGetAndResponse(queryString)
            resultDict = self.string2dict(resultString)
            if resultDict['status'] == 'scrambled 100':
                is100 = True  
                break
        self.assertFalse(is100)  
    
    def test100_900_ShouldReturnErrorOnEmptyParm(self):
        queryString = ""
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: missing op', resultDict['status'])

    def test100_910_ShouldReturnErrorOnMissingOp(self):
        queryString = "f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: missing op', resultDict['status'])

    def test100_920_ShouldReturnErrorOnDuplicateSide(self):
        queryString = "op=create&r=r&f=r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: duplicate side', resultDict['status'])

    def test100_930_ShouldReturnErrorOnDuplicateSide(self):
        queryString = "op=create&r=green"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: duplicate side', resultDict['status'])

    def test100_940_ShouldReturnErrorColorMissing(self):
        queryString = "op=create&r=&l=&t=&u=&f=&b="
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        expectedDictionary = {'status': 'error: missing color'}
        self.assertEquals(expectedDictionary, resultDict)

    def test100_950_ShouldReturnErrorOnMissingOp(self):
        queryString = "op=build"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('error: missing op', resultDict['status'])

    def test100_960_ShouldReturnErrorOnMissingOp(self):
        queryString = "op=test"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('error: missing op', resultDict['status'])
 
    def test200_910_ShouldReturnCubeMustBeSpecified(self):
        queryString = "op=check"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: cube must be specified', resultDict['status'])

    def test200_920_ShouldReturnErrorOnIncorrectSize(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=op=check&f=2&r=o&b=g&l=r&t=b&u=y&cube=y,y,b,b,o,g,o,b,w,r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: cube is not sized properly', resultDict['status'])

    def test200_930_ShouldReturnErrorOnIncorrectSize(self):
        queryString = "op=check&f=2&r=o&b=g&l=r&t=b&u=y&cube=y,b,2,o,g,t"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: cube is not sized properly', resultDict['status'])

    def test300_940_ShouldReturnErrorOnErrorCubeColorNotInDefault(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,red,red,red,red,red,red,red,red,red,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: color not in set', resultDict['status'])

    def test300_950_ShouldReturnErrorOnerrorCubeNonUniqueColors(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=r&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,r,r,r,r,r,r,r,r,r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: duplicate side', resultDict['status'])

    def test300_960_ShouldReturnErrorOnErrorCubeValueNotUsed9Times(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,b,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: value not used 9 times', resultDict['status'])

    def test300_970_ShouldReturnErrorOnErrorCubeMiddleValueIncorrect(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,r,f,f,f,f,r,r,f,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: middle value not on correct side', resultDict['status'])

    def test300_980_ShouldReturnErrorOnErrorCubeCornersNotCorrect(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,t,f,f,r,r,r,r,r,r,r,r,r,f,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,b,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: every corner must be added once', resultDict['status'])

    def test300_985_ShouldReturnErrorOnErrorCubeEdgesNotCorrect(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,b,f,f,f,r,r,r,r,r,f,r,r,r,b,b,b,b,b,r,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: every edge must be added once', resultDict['status'])

    def test300_988_ShouldReturnErrorOnErrorCubeEdgesNotCorrect(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,b,f,f,f,r,r,r,r,r,r,r,r,r,f,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: every corner must be added once', resultDict['status'])

    def test300_990_ShouldReturnErrorOnConflictsOnEdge(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,l,r,l,r,b,b,b,b,b,b,b,b,b,l,l,l,r,l,r,l,l,l,t,t,t,u,t,t,t,t,t,u,t,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_910_ShouldReturnErrorOnRotateValueNotUsed9Times(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,w,r,r,w,r,r,w,r,r,b,b,b,b,b,b,b,b,b,o,o,y,o,o,y,o,o,y,w,w,w,w,w,w,w,w,w,g,g,o,o,y,y,y,y,y&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: value not used 9 times', resultDict['status'])

    def test400_920_ShouldReturnErrorOnRotateNonUniqueColors(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=r&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,r,r,r,r,r,r,r,r,r&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: duplicate side', resultDict['status'])

    def test400_930_ShouldReturnErrorOnRotateIncorectSize(self):
        queryString = "op=rotate&f=f&r=r&b=b&l=l&t=t&u=r&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: cube is not sized properly', resultDict['status'])

    def test400_940_ShouldReturnErrorOnRotateMissingCube(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=r&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: cube must be specified', resultDict['status'])

    def test400_950_ShouldReturnErrorOnRotateColorNotInSet(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=yellow&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: color not in set', resultDict['status'])

    def test400_960_ShouldReturnErrorOnRotateMiddleValueUsedMoreThanOnce(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,r,r,r,r,r,g,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: middle value not on correct side', resultDict['status'])

    def test400_970_ShouldReturnErrorOnRotateCubeNotSpecified(self):
        queryString = "op=rotate"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: cube must be specified', resultDict['status'])

    def test400_980_ShouldReturnErrorOnRotateFaceUnknown(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r, b,b,b,b,b,b,b,b,b, o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: face is unknown', resultDict['status'])

    def test400_990_ShouldReturnErrorOnRotateFaceMissing(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r, b,b,b,b,b,b,b,b,b, o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: face is missing', resultDict['status'])

    def test400_995_ShouldReturnErrorOnRotateEdge(self):
        queryString = "op=rotate&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,t,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,u,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,f,t,t,t,t,t,u,u,u,b,u,u,u,u,u&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: every edge must be added once', resultDict['status'])

    def test400_996_ShouldReturnErrorOnRotateCorner(self):
        queryString = "op=rotate&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,l,r,r,b,b,b,b,b,b,b,b,b,l,l,l,r,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)

        self.assertEquals('error: every corner must be added once', resultDict['status'])
    
    def test500_910_ShouldReturnErrorOnScrambleForNegativeN(self):
        queryString = 'op=scramble&n=-1'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        
        self.assertEquals('error: n must be an integer between 0 to 99', resultDict['status']) 
        
    def test500_915_ShouldReturnErrorOnScrambleForNTooBig(self):
        queryString = 'op=scramble&n=100'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        
        self.assertEquals('error: n must be an integer between 0 to 99', resultDict['status']) 
       
    def test500_920_ShouldReturnErrorOnScrambleForNNotInt(self):
        queryString = 'op=scramble&n=a'
        
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        
        self.assertEquals('error: n must be an integer between 0 to 99', resultDict['status']) 
         
    def test500_930_ShouldReturnStatusErrorOnMethodUnknown(self):
        queryString = "op=scramble&method=none"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('error:', resultDict['status'])        