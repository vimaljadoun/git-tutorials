# Plot for Ec and Rc with temperature
#Author: Vimal Kumar
#Date: 19/07/2022

import numpy as np
import matplotlib.pyplot as plt
import csv

#font and axis equation setup using LATEX
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 13,
        }
plt.rcParams.update(plt.rcParamsDefault)


temp, rc, ec = [], [], []
for column in open("Ec_Rc_R134a_data.txt","r"):
    a,b,c=[float(k) for k in column.split()]
    temp.append(a)
    rc.append(b)
    ec.append(c)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(temp, rc, 'b', linewidth=1,label=r'$R_c$')
ax.set_xlabel(r'$Temperature(^{\circ}C)$')
ax.set_ylabel(r'$Critical$ $Energy$ $E_c(keV)$')
ax.set_xlim(5,60)
ax.set_ylim(-5,100)

ax.minorticks_on()
ax.tick_params(axis="x", which="minor", direction="in", top=True)
ax.tick_params(axis="x", which="major", direction="in", top=False, labeltop=False, bottom=True, labelbottom=True)
ax.tick_params(axis="y", which="minor", direction="in", right=True)
ax.tick_params(axis="y", which="major", direction="in", right=True, labelright=False, left=True, labelleft=True)


ax2 = ax.twinx()
ax2.plot(temp, ec, 'r', linewidth=1,label=r'$E_c$')
ax2.set_xlabel(r'$Temperature(^{\circ}C)$')
ax2.set_ylabel(r'$Critical$ $Radius$ $R_c(nm)$')
ax2.set_xlim(5,60)
ax2.set_ylim(-5,100)

# Get the handles and labels from both axes
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
# Combine the handles and labels from both axes
handles = handles1 + handles2
labels = labels1 + labels2
# Display both legends
ax.legend(handles, labels)

ax2.minorticks_on()
ax2.tick_params(axis="x", which="minor", direction="in", top=True)
ax2.tick_params(axis="x", which="major", direction="in", top=False, labeltop=False, bottom=True, labelbottom=True)
ax2.tick_params(axis="y", which="minor", direction="in", right=True)
ax2.tick_params(axis="y", which="major", direction="in", right=True, labelright=True, left=False, labelleft=False)

plt.tight_layout()
plt.savefig('temp_vs_EcRc.png', bbox_inches='tight', pad_inches=0.1,dpi=300)
plt.show()


