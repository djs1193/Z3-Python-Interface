# All the adjacent states should be colored differently

from z3 import *
s = Solver()

colors = {'0': 'BLUE','1': 'RED','2': 'GREEN'}

WA = Int('WA')
NT=  Int('NT')
SA = Int('SA')
Q =  Int('Q')
NSW = Int('NSW')
V = Int('V')
T = Int('T')

s.add( 0 <= WA, WA <= 2,0 <= NT, NT <= 2,0 <= SA, SA <= 2,0 <= Q, Q <= 2,0 <= NSW, NSW <= 2,0 <= V, V <= 2,0 <= T, T <= 2 )
s.add(WA != NT , WA != SA)
s.add( NT != Q , NT != SA )
s.add(SA != NSW , SA != Q , SA != V)
s.add(Q != NSW , Q != NT , Q != SA)
s.add( NSW != SA , NSW != Q , NSW != V)
s.add(V != SA , V != NSW)

print(s.check())
print("WA = %s " % colors[s.model()[WA].as_string()])
print("NT = %s " % colors[s.model()[NT].as_string()])
print("SA = %s " % colors[s.model()[SA].as_string()])
print("Q = %s " % colors[s.model()[Q].as_string()])
print("NSW = %s " % colors[s.model()[NSW].as_string()])
print("V = %s " % colors[s.model()[V].as_string()])
print("T = %s " % colors[s.model()[T].as_string()])
