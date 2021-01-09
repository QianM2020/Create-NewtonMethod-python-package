from NewtonMethod_QM import *

n = NewMeth(x1**2+2*x1-x2**2+3*x2,(-10,10),100)
assert(n.newmeth()[0]== -1. and (n.newmeth()[1]== 1.5))

j = Jacobian(x1**2+2*x1-x2,(-10,10))
assert(j.show_result()[0]== -18. and (j.show_result()[1]== -1))

h = Hessian(x1**2+2*x1-x2**2,(-10,10))
assert(h.show_result()[0,0] == 2 and h.show_result()[0,1] == 0 and h.show_result()[1,0] == 0 and h.show_result()[1,1] == -2)