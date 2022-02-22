# in this we will practice cobining shapes
# hill shapes 
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    
# diamond shape
n= int(input("enter the no of rows you want to print"))

    print()
# downwrd hill shape
n= int(input("enter the no of rows you want to print"))
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
