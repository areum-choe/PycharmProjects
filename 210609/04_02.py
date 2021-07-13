### matplotlib, seaborn, plotly, folium

### 데이터 처리 : pandas
### 선형대수, 딥러닝, 수학함수 : numpy

import numpy as np
import matplotlib.pyplot as plt

# linspace(시작, 끝, 만들 값의 수)
x=np.linspace(0,14,60) #균등하게 나눠서
print(type(x)) #넘파이가 만든 배열
print(x)

y=np.sin(x)
z=np.cos(x)
t=np.tan(x)
plt.plot(x,y,'o')
plt.show()