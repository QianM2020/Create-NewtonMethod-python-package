import numpy as np
from sympy import symbols, diff
from .GeneralDiff import Diff

#Symbol 2D vectors
x1 = symbols("x1")
x2 = symbols("x2") 

class Jacobian(Diff):
    def __init__(self,f,x):
        """ First derivation class for calculating first derivation of funcion based on the initial point.
    
        Attributes:
            f (characters) representing the function (with 2 variables: x1,x2) to differetiate
            x (2d list) representing the initial point
            result (2d list) representing the derivative results    
            
        Methods:
            show_result() 
        """
    
        Diff.__init__(self,f,x)
        self.result = np.array([diff(f, x1).subs(x1, self.init[0]).subs(x2, self.init[1]), diff(f, x2).subs(x1, self.init[0]).subs(x2, self.init[1])], dtype=float) 
    
    def show_result(self):
        """
        Function doing first derivative of function with respect to x"
        Args: None
        Returns: result (ndarray)
        """
        return self.result