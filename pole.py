import math
def ppowierzchni(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        value = False
    elif a+b>c and a+c>b and b+c>a:
        value = True
    else:
        value = False
    if value == True:
                s = (a+b+c)/2
                P = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print(P)

ppowierzchni(3,4,5)