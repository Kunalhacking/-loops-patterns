
n= int(input("enter the number of rows you want to print"))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()   
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()

