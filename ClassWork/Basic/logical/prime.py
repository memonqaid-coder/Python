"""n=14
flag=0
for i in range(3,n):
    
    if n % i == 0:
        flag = 1

    if flag==0:
        print("Prime")
    else:
        print("Not Prime")
"""
for k in range(3,101):
    
     number = k
     flag=0   

     for i in range(3,number):
         if number%i==0:
             flag=1
             break
        
     if flag==0:
         print(f"{number} is Prime")   
     else:
         # print(f"{number} is Not prime")
         pass