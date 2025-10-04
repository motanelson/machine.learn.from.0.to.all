print("\033c\033[43;30m\narray?")
def joinsxy(listx,listy):
    a=[]
    if len(listx)== len(listy):
        if len(listx)==0:
            return a
        for n in range(len(listx)):
            x=listx[n]
            y=listy[n]
            xy=[x] + [y]
            a=a+[xy]
    else:
        return a
    return a
def muls(m1,lens):
    a=[]
    for n in range(lens):
        a=a+[n*m1]
    return a


x=muls(4,20)
y=muls(2,20)
aa=joinsxy(x,y)
print(aa)
