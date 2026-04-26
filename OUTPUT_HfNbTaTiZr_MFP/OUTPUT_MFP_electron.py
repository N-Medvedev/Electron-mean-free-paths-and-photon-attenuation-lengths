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
df = pd.read_csv(r"OUTPUT_HfNbTaTiZr_Electron_IMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
plt.xscale("log")
plt.yscale("log")
# Prepare the plot:
columns_to_plot = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
labels = [ "Hf K-shell", "Hf L1-shell", "Hf L2-shell", "Hf L3-shell", "Hf M1-shell", "Hf M2-shell", "Hf M3-shell", "Hf M4-shell", "Hf M5-shell", "Hf N1-shell", "Hf N2-shell", "Hf N3-shell", "Hf N4-shell", "Hf N5-shell", "Hf N6-shell", "Hf N7-shell", "Hf O1-shell", "Hf O2-shell", "Hf O3-shell", "Nb K-shell", "Nb L1-shell", "Nb L2-shell", "Nb L3-shell", "Nb M1-shell", "Nb M2-shell", "Nb M3-shell", "Nb M4-shell", "Nb M5-shell", "Nb N1-shell", "Nb N2-shell", "Nb N3-shell", "Ta K-shell", "Ta L1-shell", "Ta L2-shell", "Ta L3-shell", "Ta M1-shell", "Ta M2-shell", "Ta M3-shell", "Ta M4-shell", "Ta M5-shell", "Ta N1-shell", "Ta N2-shell", "Ta N3-shell", "Ta N4-shell", "Ta N5-shell", "Ta N6-shell", "Ta N7-shell", "Ta O1-shell", "Ta O2-shell", "Ta O3-shell", "Ti K-shell", "Ti L1-shell", "Ti L2-shell", "Ti L3-shell", "Ti M1-shell", "Ti M2-shell", "Ti M3-shell", "Zr K-shell", "Zr L1-shell", "Zr L2-shell", "Zr L3-shell", "Zr M1-shell", "Zr M2-shell", "Zr M3-shell", "Zr M4-shell", "Zr M5-shell", "Zr N1-shell", "Zr N2-shell", "Zr N3-shell", "Valence", "Total inelastic"]
# Create N distinct colors from a colormap
N = len(columns_to_plot)
colors = np.vstack([plt.cm.tab20(np.linspace(1, 0, 20)), plt.cm.tab20b(np.linspace(1, 0, 20))])
# Set line styles:
linestyles = [ "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
for i, col in enumerate(columns_to_plot):
    color = colors[i % len(colors)]
    ls    = linestyles[i % len(linestyles)]
    label = labels[i % len(labels)]
    plt.plot(df.iloc[:, 0], df.iloc[:, col],
    color=color,
    label=label,
    linestyle=ls)
# Add a curve from the second file
df2 = pd.read_csv(r"OUTPUT_HfNbTaTiZr_Electron_EMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
columns_to_plot2 = [ 6]
labels2 = [ "Elastic"]
# Create second part of the plot:
for col, label in zip(columns_to_plot2, labels2):
    plt.plot(df2.iloc[:, 0], df2.iloc[:, col], label=label, linestyle="--")
plt.xlim(1.00000000,67419.00100000)
plt.ylim(1.00000000,100000.00000000)
plt.title("Electron mean free paths")
plt.legend(loc="best", fontsize=9, ncol=3)
# Save the plot in this format:
plt.savefig("OUTPUT_MFP_electron.png", dpi=300, bbox_inches="tight")
