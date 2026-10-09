"""lines=5
for j in range(lines):
    print(" "*((lines-1)-j),"* "*(j+1))
for j in range(1,lines+2):
    print(" "*j,(lines-j)*"* ")
"""
"""
lines=5
for j in range(lines):
    print(" "*(lines-1-j)+"("+(" "*(2*j-1)+")" if j>0 else""))
for j in range(1,lines):
    print(" "*j+"("+(" "*(2*(lines-j)-3)+")"if j<lines-1 else""))
"""
"""
for j in range (5):
    for i in range (j+1):
        print ((j+i)%2,end="")
    print()"""
