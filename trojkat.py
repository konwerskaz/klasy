def triangle(a:float, b:float, c:float):
    if a <= 0 or b <= 0 or c <= 0:
        value = False
        print(value)
    elif a+b>c and a+c>b and b+c>a:
        value = True
        print(value)
    else:
        value = False
        print(value)

triangle(1,2,3)
triangle(2,3,4)
triangle(0,3,0)