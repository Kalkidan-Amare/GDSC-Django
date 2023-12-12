def basic_operations(x, y):
    try:
        dict = {'sum': x+y, 'difference': x-y, 'product': x*y, 'quotient': x/y}
    except Exception as e:
        print(f"{e}")

    return dict

def power_operations(x, y,**kwargs):
    try:
        result=x**y

        if 'modulo' in kwargs:
            result = result % kwargs['modulo']
        
        return result
    except TypeError:
        print("Invalid input")

def apply_operations(operations):
    try:
        li=list(map(lambda x:x[0](x[1][0],x[1][1]),operations))
        return li
    except Exception as e:
        print(f"{e}")


Updated at 2023-12-12 16:15:12.792675
Updated