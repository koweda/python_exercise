h=input('height:')
w=input('weight:')
def bmi(h,w):
    return int(w)/((int(h)/100)**2)

print('bmi:',bmi(h,w))