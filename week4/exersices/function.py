def greet(name):
    print(f"Hello {name}!")

def add_numbers(a,b):
    return a + b

def print_args(*args):
    for arg in args:
        print(arg,end=" ")
    print()

def calculate_average(*args):
    sum=0 
    count=0
    for arg in args:
        sum+=arg
        count+=1
    return sum/count
    #or just
    #return sum(args)/len(args)

greet("kal")
print(add_numbers(3,7))
print_args(6,4,7,3)
print(calculate_average(23,42,3,23))