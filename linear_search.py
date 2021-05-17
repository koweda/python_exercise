data=[50,30,90,10,20,70,60,40,80]
found=False
for i in range(len(data)):
    if data[i]==40: 
        print(i)
        found= True
        break
if not found:
    print('Not Found')

def linear_s(data,value):
    for i in range(len(data)):
        if data[i]==value: 
            return i
    return -1

print(linear_s(data,40))
    