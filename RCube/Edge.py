'''
    Edge.py
    
    Created on Oct 24, 2018
    @author: Jordan Sosnowski
'''


class Edge:
    firstSide = ''
    secondSide = ''

    firstIndex = 0
    secondIndex = 0

    firstValue = ''
    secondValue = ''

    ''' Edge Matrix
    
        F    B    L    R    T    U
        1    -    -    -    7    -
        3    -    5    -    -    -
        5    -    -    3    -    -
        7    -    -    -    -    1
        -    1    -    -    1    -
        -    3    -    5    -    -
        -    5    3    -    -    -
        -    7    -    -    -    7
        -    -    1    -    3    -
        -    -    7    -    -    3
        -    -    -    1    5    -
        -    -    -    7    -    5

        
    '''

    def __init__(self, first, second):
        self.firstSide = first
        self.secondSide = second

        if first == 'f':
            if second == 't':
                self.firstIndex = 1
                self.secondIndex = 7

            elif second == 'l':
                self.firstIndex = 3
                self.secondIndex = 5

            elif second == 'r':
                self.firstIndex = 5
                self.secondIndex = 3

            elif second == 'u':
                self.firstIndex = 7
                self.secondIndex = 1

        elif first == 'b':
            if second == 't':
                self.firstIndex = 1
                self.secondIndex = 1

            elif second == 'r':
                self.firstIndex = 3
                self.secondIndex = 5

            elif second == 'l':
                self.firstIndex = 5
                self.secondIndex = 3

            elif second == 'u':
                self.firstIndex = 7
                self.secondIndex = 7

        elif first == 'l':
            if second == 't':
                self.firstIndex = 1
                self.secondIndex = 3

            elif second == 'u':
                self.firstIndex = 7
                self.secondIndex = 3

        elif first == 'r':
            if second == 't':
                self.firstIndex = 1
                self.secondIndex = 5

            elif second == 'u':
                self.firstIndex = 7
                self.secondIndex = 5

    def __str__(self):
        printValue = "Edge: " + self.firstSide + ", " + self.secondSide + "\n" \
                     + "Indexed at: " + str(self.firstIndex) + " " + str(self.secondIndex)
        return printValue
