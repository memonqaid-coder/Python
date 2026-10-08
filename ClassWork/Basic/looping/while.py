cont ='y'
while cont=='y':
    c1=int(input("Enter the a: "))
    c2=int(input("Enter the b: "))
    match(int(input("Enter your choice first: "))):
        case 1: print("Addition: ",c1+c2)
        case 2: print("Subtraction: ",c1-c2)
        case 3: print("Multiplication: ",c1*c2)
        case 4: print("Division: ",c1/c2)
        case _: print("Invalid choice")
    cont = input("Do you want to continue (y/n): ")
  
