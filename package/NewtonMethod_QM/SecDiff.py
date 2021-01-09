import numpy as np
from sympy import symbols, diff
from .GeneralDiff import Diff

#Symbol 2D vectors
x1 = symbols("x1")
x2 = symbols("x2") 

class Hessian(Diff):
    def __init__(self,f,x):
        """ Second derivation class for calculating second derivation of funcion based on the initial point.
    
        Attributes:
            f (characters) representing the function (with 2 variables: x1,x2) to differetiate
            x (2d list) representing the initial point
            result (2*2 list) representing the derivative results    
            
        Methods:
            show_result() 
        """
    
    
        Diff.__init__(self,f,x)
        self.result = np.array([[diff(f, x1, 2), diff(diff(f, x1), x2)], [diff(diff(f, x2), x1), diff(f, x2, 2)]], dtype=float)

    def show_result(self):
        """
        Function doing second derivative of function with respect to x"
        Args: None
        Returns: result (ndarray)
        """
        return self.result