import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 15, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.plot(x,y1,'r',label='y=sin(x)')
plt.plot(x,y2,'g',label='y=cos(x)')
plt.plot(x,y3,'b',label='y=tan(x)')

plt.title("title")
plt.grid()
plt.legend()
plt.show()