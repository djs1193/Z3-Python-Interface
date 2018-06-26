from z3 import *
ca_solver = Solver()  # create an instance of a Z3 CSP solver

X = Real("X")
Y = Real("Y")
Z = Real("Z")

ca_solver.add(3*X + 2*Y - Z == 1)
ca_solver.add(2*X - 2*Y + 4*Z == -2)
ca_solver.add(-X + (1/2)*Y - Z == 0)

print(ca_solver.check())      #can take two value sat or unsat
print(ca_solver.model())      # output [z = -2, y = -2, x = 1]
