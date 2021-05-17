n=18

# result=''
# base=2
# while n>0:
#     result= str(n%base)+result
#     n//=base
# print(result)

n=10010
n_s=str(n)
result=0
for i in range(len(n_s)):
    print(n_s[i],"\t" ,(len(n_s)-i-1))
    result = int(n_s[i])*(2**(len(n_s)-i-1))+result
print(result)