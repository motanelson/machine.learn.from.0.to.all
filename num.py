import numpy as np
print("\033c\033[43;30m\narray?")
def muls(m1,lens):
    a=[]
    for n in range(lens):
        a=a+[n*m1]
    return a


a=muls(2,20)
aa=np.array(a)
print(aa)