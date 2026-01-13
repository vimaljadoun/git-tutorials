# This code demostrate the distribution of random numbers fitted in gaussian distribution

import numpy as np
import matplotlib.pyplot as plt
#font and axis equation setup using LATEX
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
plt.rcParams.update(plt.rcParamsDefault)

# Parameters
mu, sigma = 100, 15
N = 10_000

# Generate data
x = np.random.normal(mu, sigma, N)

# Create figure
fig, ax = plt.subplots(figsize=(6, 4))

# Histogram (normalized to probability density)
counts, bins, _ = ax.hist(
    x,
    bins=50,
    density=True,
    color='green',
    alpha=0.75,
    label='Data'
)

# Gaussian PDF
bin_centers = 0.5 * (bins[1:] + bins[:-1])
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * \
      np.exp(-0.5 * ((bin_centers - mu) / sigma) ** 2)

ax.plot(bin_centers, pdf, 'r--', lw=2, label='Gaussian PDF')

# Labels and styling
ax.set_xlabel('IQ')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ ($\mu=100,\ \sigma=15$)')
ax.set_xlim(40, 160)
ax.set_ylim(0, 0.03)
ax.grid(True)
ax.legend()
plt.minorticks_on()
plt.tick_params(axis="x", which="minor", direction="in", top=True)
plt.tick_params(axis="x", which="major", direction="in", top=True, labeltop=False, bottom=True, labelbottom=True)
plt.tick_params(axis="y", which="minor", direction="in", right=True)
plt.tick_params(axis="y", which="major", direction="in", right=True, labelright=False, left=True, labelleft=True)
plt.tight_layout()
plt.tight_layout()
plt.savefig('histogram.png', bbox_inches='tight', pad_inches=0.1,dpi=300)
plt.show()

