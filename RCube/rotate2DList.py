'''
    rotate2DList.py
    
    Utility function for Cube
    
    The easiest way to accomplish a face rotation is to transpose a list of lists
    
    However my implementation did not consider a face as a list of lists but as a single list of values, 
    so before transposing a face I must first convert the list to a list of lists, then transpose it,
    then convert it back to a single list

    Created on Oct 25, 2018
    @author: Jordan Sosnowski
'''


def rotateCounterclockwise(matrix):
    # Rotates face counter clockwise
    transposed_matrix = zip(*matrix)  # transpose the matrix
    twoDList = list(map(list, reversed(transposed_matrix)))  # reverse the transposed matrix
    return twoDList

def rotateClockwise(matrix):
    # Rotates face clockwise, performed by calling clockwise rotation 3 times
    matrix = rotateCounterclockwise(rotateCounterclockwise(rotateCounterclockwise(matrix)))
    return matrix

def convert2DListToList(listToBeConverted):
    # Converts 2D list back to a normal list so it can be used normally by the rest of cube code
    convertedList = []
    for n in listToBeConverted:
        convertedList.extend(n)
    return convertedList

def convertListTo2DList(sliceSize, listToBeConverted):
    # converts list provided by cube into a 2D list so it can be transposed
    loopSize = len(listToBeConverted) / sliceSize
    x = 0
    convertedList = []
    for _ in range(loopSize):
        holder = listToBeConverted[x:x + loopSize]
        if len(holder) > 0:
            convertedList.append(holder)
        x += loopSize
    return convertedList
