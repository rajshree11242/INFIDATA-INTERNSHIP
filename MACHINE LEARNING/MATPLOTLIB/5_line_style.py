import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,10])

plt.plot(ypoints,ls="dotted",color='red')
plt.show()

plt.plot(ypoints,ls="dashed",lw=5,color='#ffcee0')
plt.show()

plt.plot(ypoints,ls="dashdot",lw=10,)
plt.show()

plt.plot(ypoints,ls="solid")
plt.show()

