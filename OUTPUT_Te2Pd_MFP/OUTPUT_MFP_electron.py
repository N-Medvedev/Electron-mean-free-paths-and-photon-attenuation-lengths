import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Set the format:
plt.xlabel("Electron energy (eV)", fontsize=14)
plt.ylabel("Mean free path (A)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(False)
# Set the axes:
# Read the output file:
df = pd.read_csv(r"OUTPUT_Te2Pd_Electron_IMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
plt.xscale("log")
plt.yscale("log")
# Prepare the plot:
columns_to_plot = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
labels = [ "Te K-shell", "Te L1-shell", "Te L2-shell", "Te L3-shell", "Te M1-shell", "Te M2-shell", "Te M3-shell", "Te M4-shell", "Te M5-shell", "Te N1-shell", "Te N2-shell", "Te N3-shell", "Te N4-shell", "Te N5-shell", "Pd K-shell", "Pd L1-shell", "Pd L2-shell", "Pd L3-shell", "Pd M1-shell", "Pd M2-shell", "Pd M3-shell", "Pd M4-shell", "Pd M5-shell", "Pd N1-shell", "Pd N2-shell", "Pd N3-shell", "Valence", "Total inelastic"]
# Create N distinct colors from a colormap
N = len(columns_to_plot)
colors = np.vstack([plt.cm.tab20(np.linspace(1, 0, 20)), plt.cm.tab20b(np.linspace(1, 0, 20))])
# Set line styles:
linestyles = [ "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
for i, col in enumerate(columns_to_plot):
    color = colors[i % len(colors)]
    ls    = linestyles[i % len(linestyles)]
    label = labels[i % len(labels)]
    plt.plot(df.iloc[:, 0], df.iloc[:, col],
    color=color,
    label=label,
    linestyle=ls)
# Add a curve from the second file
df2 = pd.read_csv(r"OUTPUT_Te2Pd_Electron_EMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
columns_to_plot2 = [ 3]
labels2 = [ "Elastic"]
# Create second part of the plot:
for col, label in zip(columns_to_plot2, labels2):
    plt.plot(df2.iloc[:, 0], df2.iloc[:, col], label=label, linestyle="--")
plt.xlim(1.00000000,50000.00000000)
plt.ylim(1.00000000,100000.00000000)
plt.title("Electron mean free paths")
plt.legend(loc="best", fontsize=10, ncol=2)
# Save the plot in this format:
plt.savefig("OUTPUT_MFP_electron.png", dpi=300, bbox_inches="tight")
