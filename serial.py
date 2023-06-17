"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    
    def __init__(self, start):
        '''Initates the program'''
        self.orig = start
        self.a = start
        self.first = True
    
    def generate(self):
        '''generates the first number is first is true, otherwise it adds to the number'''
        if (self.first):
            self.first = False
            return self.a
        else:
            self.a += 1
            return self.a
    
    def reset(self):
        '''resets to first number'''
        self.a = self.orig -1
        

