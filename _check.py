x=3
def calc(x):
    x += 4
    return x
print(x)
print(calc(x))
print(x,'\n')

a=[3]
def calc2(a):
    a[0] += 4
    return a
print(a)
print(calc2(a))
print(a,'\n')

b=[3]
def calc3(b):
    b = [4]
    return b
print(b)
print(calc3(b))
print(b,'\n')
