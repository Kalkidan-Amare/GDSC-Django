while(True):    
    n=int(input("Enter an integer: "))
    if n==0:
        break
    if n%2==0:
        print("The number is even.")
    elif n%2==1:
        print("The number is odd.")