from datetime import date as dt
import matplotlib.pyplot as plt
import numpy as np
dtfrmt = dt.today().strftime('%d-%m-%Y')

print (dtfrmt)
x = np.linspace(1,25,17)
plt.plot(x,np.sin(x))
plt.show()