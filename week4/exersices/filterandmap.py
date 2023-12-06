li=[0,1,2,3,4,5,6,7,8,9]

filterresult =list(filter(lambda x:x%2==0,li))
print(f"Even numbers from the list: {filterresult}")

mapresult =list(map(lambda x:x*2,li))
print(f"Doubled list: {mapresult}")