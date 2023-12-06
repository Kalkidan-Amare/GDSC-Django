num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

try:
    print(num1*num2)
except ValueError:
    print("Invalid input")

print("Dividing num1 and num2")

try:
    print(num1/num2)
except Exception as e:
    print(f"{e}")
