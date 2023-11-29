name=input("Enter your full name: ")

print(len(name))
print(name.upper())
#print(name)

if 'smith' in name.lower():
    print("Smith found.")
else:
    print("Smith not found.")
