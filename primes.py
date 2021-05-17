def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    #print(IsPrime)
    for i in range(2, int(n ** 0.5) + 1): # if import math can use math.sqrt(n)
        #print('i=',i)
        if IsPrime[i]: #when false will do nothing
            #print('i=',i)
            for j in range(i ** 2, n + 1, i): #start i*i to n+1 , step i   ； for j = i**2, i**2+i, i**2+2i, i**2+3i, ..., not exceeding n :
                print('j=',j)
                IsPrime[j] = False
                #print(i,j,IsPrime,'\n')
    return [x for x in range(2, n + 1) if IsPrime[x]] #all x such that IsPrime[x] is true.

print(eratosthenes(20))