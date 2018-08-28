import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*(np.pi),0.1)
amp1=np.sin(x)
amp2=np.cos(x)
plt.plot(x,amp1,label="Cos")
plt.plot(x,amp2,label="Sin")
plt.legend()
plt.show()
