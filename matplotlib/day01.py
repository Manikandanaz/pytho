import matplotlib.pyplot as plt
import matplotlib_inline as inl
import numpy as np
a=np.linspace(0,10,20)
b=np.linspace(0,10,5)
fig=plt.figure(figsize=(10,5))
ax1=plt.subplot()
ax1.set_title("DATA VISUALTION")
ax1.plot(a)
ax1.plot(b)
plt.show()