import numpy as np
import matplotlib.pyplot as plt

#font and axis equation setup using LATEX
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
plt.rcParams.update(plt.rcParamsDefault)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

x = np.arange(-10,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,'-', label='sin(x)')
plt.plot(x,y2,'-', label='cos(x)')
plt.plot(0,0)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.minorticks_on()
plt.tick_params(axis="x", which="minor", direction="in", top=True)
plt.tick_params(axis="x", which="major", direction="in", top=True, labeltop=False, bottom=True, labelbottom=True)
plt.tick_params(axis="y", which="minor", direction="in", right=True)
plt.tick_params(axis="y", which="major", direction="in", right=True, labelright=False, left=True, labelleft=True)
plt.tight_layout()
plt.savefig('trignometric-func.png',dpi=300)
plt.show()
