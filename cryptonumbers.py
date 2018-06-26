

from z3 import *
ca_solver = Solver()  # create an instance of a Z3 CSP solver

F = Int('F')  # create an z3.Int type variable instance called "F"
O = Int('O')
R = Int('R')
T = Int('T')
U = Int('U')
W = Int('W')
ca_solver.add(0 <= F, F <= 9)  # add constraints to the solver: 0 <= F <= 9
ca_solver.add(0 <= O, O <= 9)
ca_solver.add(0 <= R, R <= 9)
ca_solver.add(0 <= T, T <= 9)
ca_solver.add(0 <= U, U <= 9)
ca_solver.add(0 <= W, W <= 9)
ca_solver.add(F != 0)
ca_solver.add(T != 0)
ca_solver.add(Distinct(F,O,R,T,U,W))
ca_solver.add((T + T)*10**2 + (W + W)*10**1 + (O + O)*10**0 == F*10**3 + O*10**2 + U*10**1 + R*10**0)

assert ca_solver.check() == sat, "Uh oh...the solver did not find a solution. Check your constraints."
print("  T W O  :    {} {} {}".format(ca_solver.model()[T], ca_solver.model()[W], ca_solver.model()[O]))
print("+ T W O  :  + {} {} {}".format(ca_solver.model()[T], ca_solver.model()[W], ca_solver.model()[O]))
print("-------  :  -------")
print("F O U R  :  {} {} {} {}".format(ca_solver.model()[F], ca_solver.model()[O], ca_solver.model()[U], ca_solver.model()[R]))
