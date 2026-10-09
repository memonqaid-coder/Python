"""for i in range(5):
    for j in range(5-i):
        print("1", end="")
    print()"""

"""lines=int(input("Enter the number of lines: "))
for j in range(lines):
    print(" "*((lines-1)-j),"*"*(j+1))"""



"""
lines=int(input("Enter the number of lines: "))
for j in range(lines):
    print(" "*j,(lines-j),"*")"""


"""
lines=int(input("Enter the number of lines: "))
for j in range(lines):
    print(" "*((lines-1)-j),"* "*(j+1))"""


"""
lines=100
for j in range(lines):
    print(" "*((lines-1)-j),"* "*(j+1))
for j in range(1,lines+2):
    print(" "*j,(lines-j)*"* ")"""


"""
lines=int(input("Enter the number of lines: "))
for j in range(lines):
    print(" "*((lines-1)-j),"*"*(j+1))"""

"""
for i in range(5):
    for j in range(i+1):
        print(j+1, end="")
    print()"""

"""
k=1
for i in range(5):
    for j in range(i+1):
        print(k, end=" ")
        k+=1
    print()"""

"""
for i in range(5):
    for j in range(i+1):
        print(i, end=" ")
    print()"""
lines=5
for j in range(lines):
    for i in range((lines-1)-j):
        print(" ", end="")
    for i in range(j+1):
        print("2 ", end="")
    print()
for j in range(1,lines):
    for i in range(j):
        print(" ", end="")
    for i in range((lines-j)):
        print("1 ", end="")
    print()