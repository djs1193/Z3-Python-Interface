known =[
"01?10001?",
"01?100011",
"011100000",
"000000000",
"111110011",
"????1001?",
"????3101?",
"?????211?",
"?????????"]
from z3 import *
import sys
WIDTH=len(known [0])
HEIGHT=len(known)



def chk_bomb(row,col):
    s = Solver ()
    cells =[[ Int('cell_row = %d cell_col =%d' % (r,c)) for c in range(WIDTH +2)] for r in range(HEIGHT+2)]
    #Note we already doing a +2 to take care of the border

    # make border
    for c in range(WIDTH +2):
        s.add(cells [0][c]==0)
        s.add(cells[HEIGHT +1][c]==0)
    for r in range(HEIGHT +2):
        s.add(cells[r][0]==0)
        s.add(cells[r][ WIDTH +1]==0)     #to the border assign the values 0


    for r in range(1,HEIGHT +1):          #looking at the cells we are concerned with
        for c in range(1,WIDTH +1):
            t= known[r-1][c-1]            #since our known board i nxn and cells are (n+1)X(n+1) with the border
            if t in "012345678":          # t is the number present at the box
                s.add(cells[r][c]==0)     # if t is a number it is not the bomb make it equavalent to 0
                #now add the 3X3 around the given [r][c] and equate it the integer value it had
                s.add(cells[r-1][c-1] + cells[r-1][c] + cells[r-1][c+1] + cells[r][c-1]+ cells[r][c+1] + cells[r+1][c-1] + cells[r+1][c] + cells[r+1][c+1]== int(t))
    s.add(cells[row][col]==1)             # now the given variables from the function is chosen to be the bomb given value 1
    result=str(s.check ())
    if result =="unsat":
        print ("row=%d col=%d, unsat!" % (row , col))
    # enumerate all hidden cells:
for r in range(1,HEIGHT +1):
    for c in range(1,WIDTH +1):
        if known[r-1][c-1]=="?":         # only check for those values which has ? with them
            chk_bomb(r,c)
