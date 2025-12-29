import numpy as np
import matplotlib.pyplot as plt
#font and axis equation setup using LATEX
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
plt.rcParams.update(plt.rcParamsDefault)

# Data
x = np.arange(0, 100, 0.1, dtype=float)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label='sin(s)')
plt.plot(x,y2, label='cos(x)')
plt.axhline(y=0, color='black', linewidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1.5,+1.5)
plt.legend()
plt.savefig('subplot-example0.png',dpi=300)
plt.show()

#------------------------------
# Example-1 for making subplots
#------------------------------
# Set figure size FIRST
plt.figure(figsize=(6, 4))
plt.subplot(2,1,1)
plt.title('Plot of trigonometric functions')

plt.plot(x,y1,label='sin(x)')
plt.axhline(y=0, color='black', linewidth=0.8)
plt.ylim(-1.8,+1.8)
plt.ylabel('y1')
plt.legend()

plt.subplot(2,1,2)
plt.plot(x,y2,label='cos(x)')
plt.axhline(y=0, color='black', linewidth=0.8)
plt.xlabel('x')
plt.ylabel('y2')
plt.ylim(-1.8,+1.8)
plt.legend()
plt.savefig('subplot-example1.png',dpi=300)
plt.show()


#------------------------------
# Example-2 for making subplots
#------------------------------

# Create figure and axes
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(5, 5))

# Configure ticks for all subplots (same as 2x2 example)
for a in ax:
    a.minorticks_on()
    a.tick_params(axis="x", which="minor", direction="in", top=True)
    a.tick_params(axis="x", which="major", direction="in",top=True, labeltop=False,bottom=True, labelbottom=True)
    a.tick_params(axis="y", which="minor", direction="in", right=True)
    a.tick_params(axis="y", which="major", direction="in",right=True, labelright=False,left=True, labelleft=True)

# First subplot
ax[0].plot(x, y1, label='sin(x)')
# Horizontal axis at y = 0
ax[0].axhline(y=0, color='black', linewidth=0.8)
ax[0].set_ylim(-1.8, 1.8)
ax[0].set_xlim(0,100)
ax[0].set_ylabel('y1')
ax[0].set_title('Plot of trigonometric functions')
ax[0].legend()

# Second subplot
ax[1].plot(x, y2, label='cos(x)')
ax[1].axhline(y=0, color='black', linewidth=0.8)
ax[1].set_ylim(-1.8, 1.8)
ax[1].set_xlim(0,100)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y2')
ax[1].legend()

# Layout, save, show
fig.tight_layout()
fig.savefig('subplot-example2.png', dpi=300)
plt.show()

#------------------------------
# Example-3 for making subplots
#------------------------------

# Dummy data
N = 10000
time = np.linspace(0, 0.5, N)
signal = np.sin(2*np.pi*50*time)
noise  = np.random.normal(0, 0.3, N)

# FFT
yf_signal = np.fft.fft(signal)
yf_noise  = np.fft.fft(noise)
xf = np.fft.fftfreq(N, d=time[1]-time[0])

# Create 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(5, 5))

# Configure ticks for all subplots
for ax in axs.flat:
    ax.minorticks_on()
    ax.tick_params(axis="x", which="minor", direction="in", top=True)
    ax.tick_params(axis="x", which="major", direction="in", top=True,labeltop=False, bottom=True, labelbottom=True)
    ax.tick_params(axis="y", which="minor", direction="in", right=True)
    ax.tick_params(axis="y", which="major", direction="in", right=True,labelright=False, left=True, labelleft=True)

# Top-left: signal (time domain)
axs[0, 0].plot(time, signal, label='Signal')
axs[0, 0].legend()

# Top-right: FFT of signal
axs[0, 1].plot(xf[1:N//2], np.abs(yf_signal[1:N//2])/N, label='FFT(Signal)')
axs[0, 1].set_xscale('log')
axs[0, 1].set_xlim(10, 5000)
axs[0, 1].legend()

# Bottom-left: noise (time domain)
axs[1, 0].plot(time, noise, label='Noise')
axs[1, 0].legend()

# Bottom-right: FFT of noise
axs[1, 1].plot(xf[1:N//2], np.abs(yf_noise[1:N//2])/N, label='FFT(Noise)')
axs[1, 1].set_xscale('log')
axs[1, 1].set_xlim(10, 5000)
axs[1, 1].legend()

# Common labels
fig.text(0.30, 0.04, r'$Time\,(s)$', ha='center')
fig.text(0.78, 0.04, r'$Frequency\,(Hz)$', ha='center')
fig.text(0.04, 0.5, r'$Amplitude$', va='center', rotation='vertical')

# Layout
plt.tight_layout(rect=[0.06, 0.06, 1, 0.96])
fig.savefig('subplot-example3.png', dpi=300)
plt.show()