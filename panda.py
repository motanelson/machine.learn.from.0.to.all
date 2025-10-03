
import pandas as pd
print("\033c\033[43;30m\narray?")
def muls(m1,lens):
    a=[]
    for n in range(lens):
        a=a+[n*m1]
    return a
df = pd.DataFrame(muls(2,20))
df.to_csv("xxx.csv")

print(df) 