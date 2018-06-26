from z3 import *

a,b,c,d,e,f = Ints('a b c d e f')
s = Solver()
s.add(215*a + 275*b + 335*c + 355*d + 420*e + 580*f == 1505, a>=0, b>=0, c>=0, d>=0, e>=0, f>=0)

results=[]

# enumerate all possible solutions:
while True:
    if s.check() == sat:
        m = s.model()
        print (m)
        results.append(m)
        block = []
        for d in m:
            c=d()                   # a,b,c,d,e,f
            block.append(c != m[d]) # f != 0
        print(block)
        s.add(Or(block))          # new answer should be different than previous
    else:
        print ("results total=", len(results))
        break
