import matplotlib.pyplot as plt
plt.plot([10,20,300],[20,10,50],"b")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(color='k',axis='both',linestyle="--")
plt.legend("x")
plt.title("MATPLOTLIB EXAMPLE")
plt.show()