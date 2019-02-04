'''
    dispatch.py

    Creates a cube object, then based on the parameters passed to it, a HTTP Response will be produced

    Handles request passed by it by microservice.py
        If op == create
            A rubix cube will be create with the passed sides
                If there are duplicate sides or sides are provided but empty it will return an error
            If sides are not passed those sides will default

            It will return status: created and the cube in list form
                or if an error happened earlier status: errorMessage
        If op == check
            The rubix cube and default sides passed with check are checked to see if it is legal
            If it is legal then the program will check to see if the cube is full, spots or crosses
            If it is neither than it is of type unknown

            It will return status: cubeType or status: ErrorMessage

        If op == rotate
            User passes a cube list and the default side colors of the cube and
            the side to be rotated.
            The cube is first checked to be legal at first and if it is legal then
            the cube is rotated.

            If the rotation is lowercase then it is a clockwise rotation
            If the rotation is uppercase then it is a counter-clockwise rotation

        If op == scramble
            User passes value n which is the number of scrambles, a value from
            0 to 99, and an optional method.

            Method
                random: if the method is random then the rotation is randomly
                picked

                transition: if the method is transitition then the rotation that
                supplies the smallest randomness is picked. Therefore with transtition
                the cube will always be the most random

            The cube will return a dictionary of keys status and rotations. The value
            of status will be the cubes randomness percent and the value of rotations
            will be a list of rotations performed on the cube

    Created for Assignment 4 9/21/18
    Modified for Assignment 5 10/5/18
    Modified for Assignment 6 10/19/18
    Modified for Assignment 7 11/10/18
    @author Jordan Sosnowski
'''

import collections

from RCube.Cube import Cube


def dispatch(parm={}):
    '''Dispatch is passed parm by microservice.

    To be successful contains at least op : create, check, rotate, or scramble

    Parm can contain custom side values, must be under key's 'f', 'r', 'b', 'l', 't', or 'u'
    If custom values are not provided for the faces then they will be defaulted
    If faces are provided in parm but there are no values with them then an error will be returned

    For check a cube must be supplied as well as the face values in parm as well
    If the cube is not a legal cube an error will be returned, otherwise its type will be returned

    For rotate the face for the rotation must be supplied as well as the cube and the face values
    If any of those values are not suppleid an error will return
    Otherwise it will return the rotated cube

    For scramble the method is optional and is n but n will default to 0 if not
    provided and method will default to random

    '''

    dispatchStatus = ''
    op = ''
    cube = ''
    if 'op' in parm:  # if op is in the passed parameters
        colors = _setupColorsForCube(parm)
        if colors is not None:
            cube = Cube(colors)
            op = parm['op']
            if op == 'check':
                _checkCube(parm, cube)
            elif op == 'create':
                cube.createCube()
            elif op == 'rotate':
                _rotateCube(parm, cube)
            elif op == 'scramble':
                _scrambleCube(parm, cube)
            else:  # did not pass correct op
                dispatchStatus = 'error: missing op'
        else:  # Had a face key with missing value
            dispatchStatus = 'error: missing color'
    else:  # op not provided in parm
        dispatchStatus = 'error: missing op'

    httpResponse = _getHttpResponse(dispatchStatus, op, cube)
    return httpResponse


def _setupColorsForCube(parm):
    # Loop through colors collection and if there is a passed value for that side, set it
    colors = collections.OrderedDict(
        (('f', 'green'), ('r', 'yellow'), ('b', 'blue'), ('l', 'white'), ('t', 'red'), ('u', 'orange')))
    for key in colors:  # check to see if user supplied custom sides
        value = _getPassedValue(parm, key)
        if value is not None:
            colors[key] = value
        if value == "missing":
            return None
    return colors


def _getPassedValue(parm, key):
    # checks to see if a passed key is located in the user given parameter list
    if key in parm:  # if the key is given at all
        if parm[key] == '':  # if key is given but value is missing return missing
            return "missing"
        else:
            if " " in parm[key]:  # if value is blank. return None
                return None
            else:
                return parm[key]  # if value is not blank, return custom value
    return None


def _checkCube(parm, cube):
    if 'cube' in parm:
        cube.checkCube(parm['cube'])
    else:
        cube.setErrorMessage('cube must be specified')


def _rotateCube(parm, cube):
    if 'face' in parm:
        rotatingFace = parm['face']
    else:
        rotatingFace = ''
    if 'cube' in parm:
        cubeString = parm['cube']
        cube.checkCube(cubeString)
        cube.rotateCube(rotatingFace)
    else:
        cube.setErrorMessage('cube must be specified')


def _scrambleCube(parm, cube):
    # sets default variables, if provided by parm, sets them
    rotations = '0'
    method = 'random'
    if 'n' in parm:
        rotations = parm['n']
    if 'method' in parm:
        method = parm['method']
    cube.scramble(rotations, method)


def _getError(status, error):
    # Sets up error message if cube has one
    if 'error' in status:
        status = 'error: ' + error
    else:
        status = status
    return status


def _getHttpResponse(dispatchStatus, op, cube):
    # returns http response   
    response = {}
    if 'error' not in dispatchStatus:
        status = _getError(cube.status, cube.error)
        if 'error' not in status:
            if op == 'create' or op == 'rotate':
                response['cube'] = cube.getCubeList()
            elif op == 'scramble':
                response['rotations'] = cube.rotations

    else:
        status = dispatchStatus
    response['status'] = status
    return response
