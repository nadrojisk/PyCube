'''
    Corner.py
    
    
    Created on Oct 24, 2018
    @author: Jordan Sosnowski 
'''


class Corner:
    firstSide = ''
    secondSide = ''
    thirdSide = ''

    firstIndex = 0
    secondIndex = 0
    thirdIndex = 0

    firstValue = ''
    secondValue = ''
    thirdValue = ''

    ''' Corner Matrix
    
        F    B    L    R    T    U
        0    -    2    -    6    -
        2    -    -    0    8    -
        6    -    8    -    -    0
        8    -    -    6    -    2
        -    0    -    2    2    -
        -    2    0    -    0    -
        -    6    -    8    -    8
        -    8    6    -    -    6
        
    '''

    def __init__(self, first, second, third):
        self.firstSide = first
        self.secondSide = second
        self.thirdSide = third

        if first == 'f':
            if second == 'l' and third == 't':
                self.firstIndex = 0
                self.secondIndex = 2
                self.thirdIndex = 6
            elif second == 'r' and third == 't':
                self.firstIndex = 2
                self.secondIndex = 0
                self.thirdIndex = 8
            elif second == 'l' and third == 'u':
                self.firstIndex = 6
                self.secondIndex = 8
                self.thirdIndex = 0
            elif second == 'r' and third == 'u':
                self.firstIndex = 8
                self.secondIndex = 6
                self.thirdIndex = 2
        elif first == 'b':
            if second == 'r' and third == 't':
                self.firstIndex = 0
                self.secondIndex = 2
                self.thirdIndex = 2
            elif second == 'l' and third == 't':
                self.firstIndex = 2
                self.secondIndex = 0
                self.thirdIndex = 0

            elif second == 'r' and third == 'u':
                self.firstIndex = 6
                self.secondIndex = 8
                self.thirdIndex = 8
            elif second == 'l' and third == 'u':
                self.firstIndex = 8
                self.secondIndex = 6
                self.thirdIndex = 6

    def __str__(self):
        printValue = "Corner: " + self.firstSide + ", " + self.secondSide + ", " + self.thirdSide + "\n" \
                     + "Indexed at: " + str(self.firstIndex) + " " + str(self.secondIndex) + " " + str(self.thirdIndex)
        return printValue
