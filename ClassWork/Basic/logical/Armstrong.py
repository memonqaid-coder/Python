#CASE:1
number = 159
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum+=pow(rem,3)
    number  =number//10
    
if temp==sum:
    print("armstrong")
else:
    print("Not armstrong")

"""--------*---------*--------*-----------*----------*-----------*-------------*--------*---------*-------"""

#CASE:2
for i in range(100, 1000):
    temp = i
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit*3
        temp //= 10

    if total == number:
        print(i, "is an Armstrong number")

"""--------*--------"""
for i in range(100,1000)
number = i
temp = number
sum = 0
    while number!=0:
        rem = number%10
        sum+=pow(rem,3)
        number  =number//10
    
if temp==sum:
    print("armstrong")
else:
    print("Not armstrong")