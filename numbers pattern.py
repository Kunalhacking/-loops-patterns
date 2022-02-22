# normal right triangle with number pattern
no_rows=int(input("enter the number"))
for row in range(1,no_rows+1):
    for colums in range(1,row+1):
        print(row,end="")
    print()
# inverted right angle triangle with number pattern
no_rows=int(input("enter the no of rows your want to print"))
for row in range(1,no_rows+1):
    for column in range(1,row+1):
        print(column,end="")
    print()
 # downward pattern 
no_rows=int(input("enter the no of rows you want to print"))
for i in range(1,no_rows+1):
    for j in range(i,no_rows+1):
        print(j,end="") 
    print()  
    