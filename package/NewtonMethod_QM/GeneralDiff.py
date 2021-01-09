class Diff:
    
    def __init__(self, f, x):
    
        """ Generic differetiate class for differentation calculating.
    
        Attributes:
            f (characters) representing the function to differetiate
            x (2d list) representing the initial point
        """
      
        self.func = f
        self.init = x
      