import numpy as np
from .GeneralDiff import Diff
from .FstDiff import Jacobian
from .SecDiff import Hessian

class NewMeth(Diff):
    def __init__(self,f,x,iters):
        """
    Computing approximate optimal values with Newton methods.
    Attributes
        f (characters) representing the function to differetiate
        x (2d list) representing the initial point
        iters (integer) representing the maximum iteration epochs
    Methods:
        def newmeth()
        """
        Diff.__init__(self,f,x)
        self.iters = iters
        
    def newmeth(self):
        """
        Function computing pproximate optimal values with Newton methods
        Args: None
        Returns: x_new (2darray)
        """
        Hessian_T = np.linalg.inv(Hessian(self.func, self.init).show_result())
        H_G = np.matmul(Hessian_T, Jacobian(self.func, self.init).show_result())
        x_new = self.init - H_G
        print("The 1st iteration result is:", x_new)
        for i in range(1, self.iters):
            Hessian_T = np.linalg.inv(Hessian(self.func, x_new).show_result())
            H_G = np.matmul(Hessian_T, Jacobian(self.func, x_new).show_result())
            x_new = x_new - H_G
        print("The "+str(i+1)+"th iteration result is:", x_new)
        return x_new