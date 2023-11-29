def takelist():
    li=[]
    n=int(input("Enter number of items you want to add: "))
    for i in range(0,n):
        accept=int(input(f"Enter element {i+1} "))
        li.append(accept)
    sum=0
    for i in range(0,n):
        if li[i]>0:
            sum+=li[i]

    print(f"sum: {sum} ")

takelist()