# # heart shape pattern 
# for i in range(6):
#     for j in range(7):
#         if (i==0 and j%3!=0) or (i==1 and j%3==0 ) or (i-j==2 )or (i+j==8):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print() 
#  ** ** 
# *  *  *
# *     *
#  *   *
#   * *
#    *
# advance  pattern 2

# m pattern in python 
# for i in range(1,8):
#     for j in range(1,8):
#         if (j==1) or (j==7 ) or (i==j) and (j>1 and j<5) or (i==2 and j==6) or (i==3 and j==5):                                           
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#                                 # *     *
                                # **   **
                                # * * * *
                                # *  *  *
                                # *     *
                                # *     *
                                # *     *
# ..............................................................................................                                
#  next pattern 
# for i in range(6):
#     for j in range(4):
#         if((j==0)or(j==4) and (i!=0) or (i==0 or  i==3) and (j>0 and j<4)):
            
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print() 
# ...........................................................................................                          
# str=input("enter the string to print")
# length=len(str)
# for i in range(length):
#     for j in range(i+1):
#         print(str[j],end="")
#     print()       
# ...........................................................................................
# OUTPUT 
#  P
#  PY
#  PYT
#  PYTH
#  PYTHO
#  PYTHON
# ..............................................................................................
# import time
# n=int(input("enter the number"))
# initial= time.time()
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# print(f"the total time is{time.time()-initial}")

# ex-3
#ex-3 code with harry:
# input = int n 
# boolen variable (true,false)
# n= int(input("enter the no of row you want to print\n"))
# b= bool(int(input("type 1 or 0\n")))
# if b==1:
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
#         print()
# elif b==0:
#     for i in range(n):
#         for j in range(i,n):
#             print("*",end="")
#         print()
# else:
#     print(f"you have to print either 0 or 1")
    

