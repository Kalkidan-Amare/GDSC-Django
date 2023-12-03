word=input("Please enter the word to check: ")
if word==(word[::-1]):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
    print(f"because {word[::-1]} is not equal to {word}.")