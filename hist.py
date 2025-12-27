#It will run only in Python 2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as malb
mu, sigma=100,15
x = mu + sigma*np.random.randn(10000)

#histogram of the data
n, bins, patches = plt.hist(x, 50, facecolor='green', alpha=0.75)

#add a best fit line
y = malb.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', lw=1)
plt.xlabel('Smart')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()
