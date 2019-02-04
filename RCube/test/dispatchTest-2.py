import unittest
import httplib
import json


# noinspection PyMethodMayBeStatic
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
        '''Make HTTP request to URL:PORT for /rcube?querystring; result is a JSON string'''
        try:
            theConnection = httplib.HTTPConnection(self.MICROSERVICE_URL, self.MICROSERVICE_PORT)
            theConnection.request("GET", self.MICROSERVICE_PATH + queryString)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            theStringResponse = "{'diagnostic': 'error: " + str(e) + "'}"
            return theStringResponse

    def string2dict(self, httpResponse):
        # noinspection PySingleQuotedDocstring
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
    # 100 dispatch - basic functionality
    # Desired level of confidence: boundary value analysis
    # Analysis
    # inputs:     http:// ...myURL... /httpGetAndResponse?parm
    #            parm is a string consisting of key-value pairs
    #            At a minimum, parm must contain one key of "op"
    #
    # outputs:    A JSON string containing, at a minimum, a key of "status"
    #
    # Happy path
    #      input:   parm having at least one element with a key of "op"
    #      output:  JSON string containing a key of "status"
    #
    # Sad path
    #      input:   no string
    #      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
    #
    #      input:   valid parm string with at least one key-value pair, no key of "op"
    #      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
    #
    #
    #
    # Note:  These tests require an active web service
    #
    #
    # Happy path
    def test100_010_ShouldReturnSuccessKey(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)

    # Sad path
    def test100_900_ShouldReturnErrorOnEmptyParm(self):
        queryString = ""
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test100_910_ShouldReturnErrorOnMissingOp(self):
        queryString = "f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test100_920_ShouldReturnErrorOnMissingOp(self):
        queryString = "key=value"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # ---- New sad path test for dispatch{parm} - Assignment 5 ---------
    # ------------------------------------------------------------------
    def test100_930_ShouldReturnErrorOnInvalidOp(self):
        queryString = "op=initiate"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test100_940_ShouldReturnErrorOnMissingOpCode(self):
        queryString = "op="
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # -------------------------------------------------------------------

    # Acceptance Tests
    #
    # 200 dispatch -- op=create
    # Desired level of confidence: boundary value analysis
    # Analysis
    # inputs:    http:// ...myURL... /rcube?op=create<options>
    #            where <options> can be zero or one of:
    #                    "f"    Specifies the color of the front side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "green" if missing.  Arrives unvalidated.
    #                    "r"    Specifies the color of the right side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "yellow" if missing.  Arrives unvalidated.
    #                    "b"    Specifies the color of the back side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "blue" if missing.  Arrives unvalidated.
    #                    "l"    Specifies the color of the left side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "white" if missing.  Arrives unvalidated.
    #                    "t"    Specifies the color of the top side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "red" if missing.  Arrives unvalidated.
    #                    "u"    Specifies the color of the under side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "orange" if missing.  Arrives unvalidated.
    #
    # outputs:    A JSON string containing, at a minimum, a key of "status"
    #
    # Happy path
    #      input:   zero options
    #               http:// ... myURL ... /rcube?op=create
    #      output:  default model cube, which is JSON string:
    #                {'status': 'created', 'cube': [
    #                  'green',  'green', 'green',
    #                  'green', 'green', 'green',
    #                  'green', 'green', 'green',
    #                  'yellow', 'yellow', 'yellow',
    #                  'yellow', 'yellow', 'yellow',
    #                  'yellow', 'yellow', 'yellow',
    #                  'blue', 'blue', 'blue',
    #                  'blue', 'blue', 'blue',
    #                  'blue', 'blue', 'blue',
    #                  'white', 'white', 'white',
    #                  'white', 'white', 'white',
    #                  'white', 'white', 'white',
    #                  'red', 'red', 'red',
    #                  'red', 'red', 'red',
    #                  'red', 'red', 'red',
    #                  'orange', 'orange', 'orange',
    #                  'orange', 'orange', 'orange',
    #                  'orange', 'orange', 'orange']}

    # Happy path
    def test200_010_ShouldCreateDefaultCubeStatus(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_020ShouldCreateDefaultCubeKey(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_030ShouldCreateDefaultCubeList(self):
        queryString = "op=create"
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_040_ShouldCreateMultipleFaceCubeWithOneFaceOnInputKey(self):
        queryString = "op=create&f=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_050_ShouldCreateMultipleFaceCubeWithOneFaceOnInputStatus(self):
        queryString = "op=create&f=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_060_ShouldCreateMultipleFaceCubeWithOneFaceOnInput(self):
        queryString = "op=create&f=f"
        expectedFaces = ['f', 'yellow', 'blue', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_070_ShouldCreateMultipleFaceCubeWithTwoFacesOnInputKey(self):
        queryString = "op=create&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_080_ShouldCreateMultipleFaceCubeWithTwoFacesOnInputStatus(self):
        queryString = "op=create&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_090_ShouldCreateMultipleFaceCubeWithTwoFacesOnInput(self):
        queryString = "op=create&f=f&r=2"
        expectedFaces = ['f', '2', 'blue', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_100_ShouldCreateMultipleFaceCubeWithThreeFacesOnInputKey(self):
        queryString = "op=create&b=b&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_110_ShouldCreateMultipleFaceCubeWithThreeFacesOnInputStatus(self):
        queryString = "op=create&b=b&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_120_ShouldCreateMultipleFaceCubeWithThreeFacesOnInput(self):
        queryString = "op=create&b=b&f=f&r=2"
        expectedFaces = ['f', '2', 'b', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_130_ShouldCreateMultipleFaceCubeWithFourFacesOnInputKey(self):
        queryString = "op=create&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_140_ShouldCreateMultipleFaceCubeWithFourFacesOnInputStatus(self):
        queryString = "op=create&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_150_ShouldCreateMultipleFaceCubeWithFourFacesOnInput(self):
        queryString = "op=create&b=b&f=f&l=4&r=2"
        expectedFaces = ['f', '2', 'b', '4', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_160_ShouldCreateMultipleFaceCubeWithFiveFacesOnInputKey(self):
        queryString = "op=create&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_170_ShouldCreateMultipleFaceCubeWithFiveFacesOnInputStatus(self):
        queryString = "op=create&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_180_ShouldCreateMultipleFaceCubeWithFourFacesOnInput(self):
        queryString = "op=create&t=t&b=b&f=f&l=4&r=2"
        expectedFaces = ['f', '2', 'b', '4', 't', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_190_ShouldCreateMultipleFaceCubeWithSixFacesOnInputKey(self):
        queryString = "op=create&u=1&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_200_ShouldCreateMultipleFaceCubeWithSixFacesOnInputKey(self):
        queryString = "op=create&u=1&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])

    def test200_210_ShouldCreateMultipleFaceCubeWithSixFacesOnInput(self):
        queryString = "op=create&u=1&t=t&b=b&f=f&l=45&r=200"
        expectedFaces = ['f', '200', 'b', '45', 't', '1']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_220_ShouldCreateMultipleFaceCubeWithSixFacesOnInput(self):
        queryString = "op=create&u=u&t=t&b=b&f=f&l=l&r=r"
        expectedFaces = ['f', 'r', 'b', 'l', 't', 'u']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_230_ShouldCreateMultipleFaceCubeWithInvalidFacesOnInput(self):
        queryString = "op=create&u=u&t=t&b=b&f=f&l=l&right=r"
        expectedFaces = ['f', 'yellow', 'b', 'l', 't', 'u']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_240_ShouldCreateMultipleFaceCubeWithInvalidFacesOnInput(self):
        queryString = "op=create&u=u&top=t&b=b&f=f&l=l&right=r"
        expectedFaces = ['f', 'yellow', 'b', 'l', 'red', 'u']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    def test200_250_ShouldCreateMultipleFaceCubeWithMulitpleFacesWithCaseSensitiveColors(self):
        queryString = "op=create&u=red&t=Red&b=blue&f=Blue&l=white&r=White"
        expectedFaces = ['Blue', 'White', 'blue', 'white', 'Red', 'red']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    # Sad path
    def test200_900_ShouldReturnErrorOnSameColorInInput(self):
        queryString = "op=create&f=purple&l=purple"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test200_910_ShouldReturnErrorOnSameOnOutput(self):
        queryString = "op=create&f=1&b=yellow"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # ---- New Sad path test for {'op':'create'} - Assignment 5 ------------
    # ----------------------------------------------------------------------
    def test200_920_ShouldReturnErrorOnMissingFrontFaceColor(self):
        queryString = "op=create&b=b&f=&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test200_930_ShouldReturnErrorOnMissingRightFaceColor(self):
        queryString = "op=create&b=b&f=f&l=4&r=&u=1"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test200_940_ShouldReturnErrorOnMissingBackFaceColor(self):
        queryString = "op=create&b=&l=2&r=4&u=u&t=purple"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test200_950_ShouldReturnErrorOnMissingLeftFaceColor(self):
        queryString = "op=create&b=back&l=&r=4&u=u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test200_960_ShouldReturnErrorOnMissingTopFaceColor(self):
        queryString = "op=create&l=1&r=4&u=u&t=&f=front"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test200_970_ShouldReturnErrorOnMissingUnderFaceColor(self):
        queryString = "op=create&l=1&r=4&u=&t=top&f=front"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # ---------------------------------------------------------------------

    # Acceptance Tests
    #
    # 300 dispatch -- {'op':'check'}
    # Desired level of confidence: boundary value analysis
    # Analysis
    # inputs:    http:// ...myURL... /rcube?op=check<options><cube>
    #            where <cube> is mandatory, string representing each color element of the cube
    #            where <options> can be zero or one of:
    #                    "f"    Specifies the color of the front side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "green" if missing.  Arrives unvalidated.
    #                    "r"    Specifies the color of the right side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "yellow" if missing.  Arrives unvalidated.
    #                    "b"    Specifies the color of the back side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "blue" if missing.  Arrives unvalidated.
    #                    "l"    Specifies the color of the left side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "white" if missing.  Arrives unvalidated.
    #                    "t"    Specifies the color of the top side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "red" if missing.  Arrives unvalidated.
    #                    "u"    Specifies the color of the under side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "orange" if missing.  Arrives unvalidated.
    #
    # outputs:    A JSON string containing, at a minimum, a key of "status"
    #
    # Happy path
    #      input:   zero options
    #               http:// ... myURL ... /rcube?op=check<options>
    #      output:  default model cube, which is JSON string:
    #                {'status': 'created', <options>}
    #                options:    "full", "spots", "crosses", "unknown"

    # Sad Path
    def test300_900_ShouldReturnErrorMissingCube(self):
        queryString = "op=check&f=f&r=r&b=b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_901_ShouldReturnErrorOnBadOp(self):
        queryString = "op=cjeck"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_902_ShouldReturnErrorOnEmptyCube(self):
        queryString = "op=check&cube="
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_903_ShouldReturnErrorOnInvalidCube(self):
        queryString = "op=check&f=a&r=b&b=c&l=d&t=e&u=f&cube=a,b,c,d,e,f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_904_ShouldReturnErrorInvalidCubKey(self):
        queryString = 'op=check&f=f&r=r&b=3&l=4&t=t&u=u&cbe=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u'
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_905_ShouldReturnErrorOnCubeSizeLTValidSize(self):
        queryString = "op=check&f=1&r=2&b=3&l=4&t=5&u=6&cube=1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_906_ShouldReturnErrorOnCubeSizeGTValidSize(self):
        queryString = "op=check&f=1&r=2&b=3&l=4&t=5&u=6&cube=1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_907_ShouldReturnErrorOnInvalidFaceColors(self):
        queryString = "op=check&f=1&r=2&b=3&l=4&t=5&u=6&cube=1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,7,7,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_908_ShouldReturnErrorOnInvalidFaceColors(self):
        queryString = "op=check&cube=green,green,green,green,green,green,green,green,green,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,blue,blue,blue,blue,blue,bluw,blue,blue,blue,white,white,whte,white,white,white,white,white,white,red,red,red,red,red,red,red,red,red,orange,orange,orange,orange,orange,orange,orange,orange,orange"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_909_ShouldReturnErrorOnInvalidMiddleElement(self):
        queryString = "op=check&f=1&r=2&b=3&l=4&t=5&u=6&cube=1,1,1,1,2,1,1,1,1,2,2,2,2,1,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_910_ShouldReturnErrorOnInvalidMiddleElement(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,l,b,b,b,b,l,l,l,l,b,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_911_ShouldReturnErrorOnInvalidMiddleElementWithDefaultColors(self):
        queryString = "op=check&cube=green,green,green,green,green,green,green,green,green,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,blue,blue,blue,blue,blue,blue,blue,blue,blue,white,white,white,white,white,white,white,white,white,red,red,red,red,orange,red,red,red,red,orange,orange,orange,orange,red,orange,orange,orange,orange"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_912_ShouldReturnErrorOnWhenMiddleElementOfFacesNotUnique(self):
        queryString = "op=check&u=1cube=green,green,green,green,1,green,green,green,green,yellow,yellow,yellow,yellow,blue,yellow,yellow,yellow,yellow,blue,blue,blue,blue,yellow,blue,blue,blue,blue,white,white,white,white,white,white,white,white,white,red,red,red,red,1,red,red,red,red,1,red,1,1,1,1,1,1,green"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # ----------------------------------------------------------------------
    # ----  Sad path tests for missing faces - Assignment 5 --------------
    # ----------------------------------------------------------------------
    def test300_913_ShouldReturnErrorOnEmptyFrontSideOfFaceColor(self):
        queryString = "op=check&f=&r=r&b=b&l=l&t=t&u=u&cube=green,green,green,green,green,green,green,green,green,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_914_ShouldReturnErrorOnEmptyRightSideOfFaceColor(self):
        queryString = "op=check&r=&b=b&l=l&t=t&u=u&cube=green,green,green,green,green,green,green,green,green,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_915_ShouldReturnErrorOnEmptyBackSideOfFaceColor(self):
        queryString = "op=check&f=f&r=r&b=&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,blue,blue,blue,blue,blue,blue,blue,blue,blue,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_916_ShouldReturnErrorOnEmptyLeftSideOfFaceColor(self):
        queryString = "op=check&f=f&r=r&b=b&l=&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,white,white,white,white,white,white,white,white,white,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_917_ShouldReturnErrorOnEmptyTopSideOfFaceColor(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,red,red,red,red,red,red,red,red,red,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_918_ShouldReturnErrorOnEmptyUnderSideOfFaceColor(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,orange,orange,orange,orange,orange,orange,orange,orange,orange"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # ----------------------------------------------------------------------
    # ----  Sad path tests for adjacent elements - Assignment 5 --------------
    # ----------------------------------------------------------------------
    def test300_919_ShouldReturnErrorOnConflictsOnCorner(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,b,f,f,f,r,r,r,r,r,r,r,r,r,f,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_920_ShouldReturnErrorOnConflictsOnCorner(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,l,r,r,b,b,b,b,b,b,b,b,b,l,l,l,r,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_921_ShouldReturnErrorOnConflictsOnEdge(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,t,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,u,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,f,t,t,t,t,t,u,u,u,b,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    def test300_922_ShouldReturnErrorOnConflictsOnEdge(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,l,r,l,r,b,b,b,b,b,b,b,b,b,l,l,l,r,l,r,l,l,l,t,t,t,u,t,t,t,t,t,u,t,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:', resultDict['status'][0:6])

    # ----------------------------------------------------------------------

    # Happy path
    # ----------------------------------------------------------------------
    # ----  Happy path tests for status full - Assignment 5 --------------
    # ----------------------------------------------------------------------
    def test300_010_ShouldReturnStatusFullWithNumbers(self):
        queryString = "op=check&f=1&r=2&b=3&l=4&t=5&u=6&cube=1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('full', resultDict['status'])

    def test300_015_ShouldReturnStatusFullWithLetters(self):
        queryString = "op=check&f=2&r=z&b=1&l=6&t=4&u=B&cube=2,2,2,2,2,2,2,2,2,z,z,z,z,z,z,z,z,z,1,1,1,1,1,1,1,1,1,6,6,6,6,6,6,6,6,6,4,4,4,4,4,4,4,4,4,B,B,B,B,B,B,B,B,B"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('full', resultDict['status'])

    def test300_020_ShouldReturnStatusFullWithDefaultCube(self):
        queryString = "op=check&cube=green,green,green,green,green,green,green,green,green,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,blue,blue,blue,blue,blue,blue,blue,blue,blue,white,white,white,white,white,white,white,white,white,red,red,red,red,red,red,red,red,red,orange,orange,orange,orange,orange,orange,orange,orange,orange"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('full', resultDict['status'])

    def test300_025_ShouldReturnStatusFullWithColors(self):
        queryString = "op=check&f=yellow&r=green&b=white&l=blue&t=orange&u=red&cube=yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,green,green,green,green,green,green,green,green,green,white,white,white,white,white,white,white,white,white,blue,blue,blue,blue,blue,blue,blue,blue,blue,orange,orange,orange,orange,orange,orange,orange,orange,orange,red,red,red,red,red,red,red,red,red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('full', resultDict['status'])

    # ----------------------------------------------------------------------
    # ----  Happy path tests for status crosses - Assignment 5 -------------
    # ----------------------------------------------------------------------
    def test300_030_ShouldReturnStatusCrossesWithNumbers(self):
        queryString = "op=check&f=2&r=3&b=5&l=6&t=1&u=4&cube=1,2,1,2,2,2,1,2,1,2,3,2,3,3,3,2,3,2,4,5,4,5,5,5,4,5,4,5,6,5,6,6,6,5,6,5,3,1,3,1,1,1,3,1,3,6,4,6,4,4,4,6,4,6"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('crosses', resultDict['status'])

    def test300_035_ShouldReturnStatusCrossesWithLetters(self):
        queryString = "op=check&f=w&r=g&b=y&l=b&t=r&u=o&cube=r,w,r,w,w,w,r,w,r,w,g,w,g,g,g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b,b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('crosses', resultDict['status'])

    def test300_040_ShouldReturnStatusCrossesWithColors(self):
        queryString = "op=check&f=green&r=red&b=blue&l=orange&t=white&u=yellow&cube=white,green,white,green,green,green,white,green,white,green,red,green,red,red,red,green,red,green,yellow,blue,yellow,blue,blue,blue,yellow,blue,yellow,blue,orange,blue,orange,orange,orange,blue,orange,blue,red,white,red,white,white,white,red,white,red,orange,yellow,orange,yellow,yellow,yellow,orange,yellow,orange"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('crosses', resultDict['status'])

    # ----------------------------------------------------------------------
    # ----  Happy path tests for status spots - Assignment 5 ---------------
    # ----------------------------------------------------------------------
    def test300_045_ShouldReturnStatusSpotsWithNumbers(self):
        queryString = "op=check&f=2&r=1&b=5&l=4&t=3&u=6&cube=1,1,1,1,2,1,1,1,1,3,3,3,3,1,3,3,3,3,4,4,4,4,5,4,4,4,4,6,6,6,6,4,6,6,6,6,2,2,2,2,3,2,2,2,2,5,5,5,5,6,5,5,5,5"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('spots', resultDict['status'])

    def test300_050_ShouldReturnStatusSpotsWithLetters(self):
        queryString = "op=check&f=r&r=b&b=o&l=g&t=w&u=y&cube=y,y,y,y,r,y,y,y,y,o,o,o,o,b,o,o,o,o,w,w,w,w,o,w,w,w,w,r,r,r,r,g,r,r,r,r,b,b,b,b,w,b,b,b,b,g,g,g,g,y,g,g,g,g"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('spots', resultDict['status'])

    def test300_055_ShouldReturnStatusSpotsWithColors(self):
        queryString = "op=check&cube=yellow,yellow,yellow,yellow,green,yellow,yellow,yellow,yellow,red,red,red,red,yellow,red,red,red,red,white,white,white,white,blue,white,white,white,white,orange,orange,orange,orange,white,orange,orange,orange,orange,green,green,green,green,red,green,green,green,green,blue,blue,blue,blue,orange,blue,blue,blue,blue"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('spots', resultDict['status'])

    # ----------------------------------------------------------------------
    # ----  Happy path tests for status unknown - Assignment 5 -------------
    # ----------------------------------------------------------------------
    def test300_060_ShouldReturnStatusUnknownWithNumbers(self):
        queryString = "op=check&f=1&r=2&b=3&l=4&t=5&u=6&cube=3,1,1,1,1,1,3,1,6,5,4,5,5,2,3,3,2,6,1,3,5,6,3,5,1,4,1,3,6,6,2,4,2,6,3,5,4,5,2,4,5,3,2,4,4,2,6,4,2,6,6,4,5,2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('unknown', resultDict['status'])

    def test300_065_ShouldReturnStatusUnknownWithDefaultColors(self):
        queryString = "op=check&cube=orange,green,white,blue,green,orange,white,red,white,red,orange,yellow,white,yellow,white,red,yellow,yellow,orange,blue,green,green,blue,white,red,red,green,yellow,blue,green,red,white,yellow,orange,orange,blue,red,orange,blue,white,red,yellow,yellow,red,blue,orange,blue,green,green,orange,green,white,yellow,blue"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('unknown', resultDict['status'])

    def test300_070_ShouldReturnStatusUnknownWithColors(self):
        queryString = "op=check&f=white&r=orange&l=red&b=yellow&t=green&u=blue&cube=yellow,red,green,red,white,white,white,blue,white,white,yellow,orange,red,orange,orange,red,red,orange,yellow,green,red,green,yellow,blue,yellow,blue,white,green,green,red,yellow,red,green,orange,orange,red,yellow,yellow,green,white,green,orange,blue,blue,orange,blue,orange,green,white,blue,yellow,blue,white,blue"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('unknown', resultDict['status'])

    def test300_075_ShouldReturnStatusUnknownWithLetters(self):
        queryString = "op=check&f=f&r=r&l=l&b=b&t=t&u=u&cube=f,t,f,f,f,r,b,l,f,r,u,r,t,r,t,r,u,l,b,r,l,f,b,b,u,u,r,u,u,l,l,l,l,b,b,l,f,f,t,b,t,l,t,b,t,t,t,u,r,u,f,u,r,b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('unknown', resultDict['status'])

    def test300_080_ShouldReturnStatusUnknownWithLetters(self):
        queryString = "op=check&f=o&r=b&b=r&l=g&t=y&u=w&cube=y,y,b,b,o,g,o,b,w,r,b,b,r,b,w,b,w,r,o,g,g,o,r,g,g,b,b,y,y,o,y,g,o,o,o,g,r,w,w,r,y,r,g,o,y,w,y,r,g,w,r,y,w,w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('unknown', resultDict['status'])
