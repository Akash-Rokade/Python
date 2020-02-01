import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x=np.random.randint(0,50,200)
y=np.random.randint(0,50,200)
z=np.random.randint(0,50,200)
col=np.random.randint(0,200,200)
fig=plt.figure()
ax=fig.gca(projection="3d")
ax.scatter(x,y,z,c=col)
plt.show()
