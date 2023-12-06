print_args=lambda x,y: x+y
result =print_args(3,5)
print(result)

square=lambda x: x**2
print(f"square of 5: {square(5)}")

even=lambda x:True if x%2==0 else False
print(f"is 5 even: {even(5)}")