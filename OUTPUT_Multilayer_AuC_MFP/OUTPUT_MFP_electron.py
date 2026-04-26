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
df = pd.read_csv(r"OUTPUT_Multilayer_AuC_Electron_IMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
plt.xscale("log")
plt.yscale("log")
# Prepare the plot:
columns_to_plot = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
labels = [ "Au K-shell", "Au L1-shell", "Au L2-shell", "Au L3-shell", "Au M1-shell", "Au M2-shell", "Au M3-shell", "Au M4-shell", "Au M5-shell", "Au N1-shell", "Au N2-shell", "Au N3-shell", "Au N4-shell", "Au N5-shell", "Au N6-shell", "Au N7-shell", "Au O1-shell", "Au O2-shell", "Au O3-shell", "C K-shell", "Valence", "Total inelastic"]
# Create N distinct colors from a colormap
N = len(columns_to_plot)
colors = np.vstack([plt.cm.tab20(np.linspace(1, 0, 20)), plt.cm.tab20b(np.linspace(1, 0, 20))])
# Set line styles:
linestyles = [ "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
for i, col in enumerate(columns_to_plot):
    color = colors[i % len(colors)]
    ls    = linestyles[i % len(linestyles)]
    label = labels[i % len(labels)]
    plt.plot(df.iloc[:, 0], df.iloc[:, col],
    color=color,
    label=label,
    linestyle=ls)
# Add a curve from the second file
df2 = pd.read_csv(r"OUTPUT_Multilayer_AuC_Electron_EMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
columns_to_plot2 = [ 3]
labels2 = [ "Elastic"]
# Create second part of the plot:
for col, label in zip(columns_to_plot2, labels2):
    plt.plot(df2.iloc[:, 0], df2.iloc[:, col], label=label, linestyle="--")
plt.xlim(1.00000000,80729.00100000)
plt.ylim(1.00000000,100000.00000000)
plt.title("Electron mean free paths")
plt.legend(loc="best", fontsize=10, ncol=2)
# Save the plot in this format:
plt.savefig("OUTPUT_MFP_electron.png", dpi=300, bbox_inches="tight")
