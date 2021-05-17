def fibonacci(n):
    if n ==0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def fibonacci_ram(n):
    global a,b
    if n ==0:
        a=1
        return 1
    elif n == 1:
        b=1
        return 1
    else:
        ans=(a+b)
        b=a
        a=ans
        return ans




for i in range(41):
    print('i=',i)
    print(fibonacci_ram(i),'\n')
