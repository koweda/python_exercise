
def fizzbuzz(n):   
    output='' 
    if n%3==0:
        output='fizz'
    if n%5==0:
        output+='buzz'
    if len(output)>0:
        n=output
    return n

for i in range(1,101):
    print(fizzbuzz(i))