import numpy as np
import array
import time
import matplotlib.pyplot as plt
import matplotlib
print("\033c\033[43;30m\narray?")
def muls(m1,lens):
    a=[]
    for n in range(lens):
        a=a+[n*m1]
    return a

#print(matplotlib._version)
x=np.array(muls(4,20))
y=np.array(muls(2,20))

fig, ax = plt.subplots()

# mudar cor de fundo da figura toda
fig.patch.set_facecolor("yellow")

# mudar cor de fundo só da área do gráfico
ax.set_facecolor("yellow")

ax.plot(x, y, color="blue")
plt.show()
#time.sleep(10)