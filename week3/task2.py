symbol=input("Please enter the pattern to be printed: ")
if len(symbol)>1:
    print("The length of the character should be 1.")
elif symbol in ['a','e','i','o','u','A','E','I','O','U']:
    print("Vowels are not allowed.")
else:
    for i in range(1,6):
            print(symbol*(2*i-1))