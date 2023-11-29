'''
n = 122
while n>=97:
    if n % 2 == 1:
        print(chr(n - 32),end=" " )
    else:
        print(chr(n), end=" " )
    n -= 1
'''

#list comprehension
#print(' '.join(chr(n - 32) if n % 2 == 1 else chr(n) for n in range(122, 96, -1)))

n=122
while n>=97:
    print(f"{chr(n - 32) if n%2==1 else chr(n)}", end=" " )
    n-=1

