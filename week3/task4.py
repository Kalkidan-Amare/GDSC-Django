sum=counter=0
for i in range(1,51):
    if i%2==0:
        sum+=i
        if i%3==0:
            print("Three",end=' ')
            counter+=1
        elif i%5==0:
            print("Five",end=' ')
            counter+=1
        else:
            print(i,end=' ')
print(f"\nTotal {sum= } count of numbers replaced {counter}")