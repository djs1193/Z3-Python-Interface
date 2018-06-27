import random
from z3 import *
from operator import mul
from functools import reduce

def factor(n):

    in1,in2,out=Ints('in1 in2 out')

    s=Solver()
    s.add(out==n)
    s.add(in1*in2==out)
    # inputs cannot be negative and must be non-1:
    s.add(in1>1)
    s.add(in2>1)

    if s.check()==unsat:     # can return unsat or unknown for prime number.
        return [n]
    if s.check()==unknown:
        return [n]

    m=s.model()
    in1_n=m[in1].as_long()
    in2_n=m[in2].as_long()

    rt=list(factor (in1_n) + factor (in2_n)) # put the current value inthe list and send them for factorization
    return rt

# infinite test:
print(factor(3513452))
