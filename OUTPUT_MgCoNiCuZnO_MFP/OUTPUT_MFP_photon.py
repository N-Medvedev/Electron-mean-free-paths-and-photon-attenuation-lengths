import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Set the format:
plt.xlabel("Photon energy (eV)", fontsize=14)
plt.ylabel("Attenuation length (A)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(False)
# Set the axes:
# Read the output file:
df = pd.read_csv(r"OUTPUT_MgCoNiCuZnO_Photon_IMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
plt.xscale("log")
plt.yscale("log")
# Prepare the plot:
columns_to_plot = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
labels = [ "Mg K-shell", "Mg L1-shell", "Mg L2-shell", "Mg L3-shell", "Co K-shell", "Co L1-shell", "Co L2-shell", "Co L3-shell", "Co M1-shell", "Co M2-shell", "Co M3-shell", "Ni K-shell", "Ni L1-shell", "Ni L2-shell", "Ni L3-shell", "Ni M1-shell", "Ni M2-shell", "Ni M3-shell", "Cu K-shell", "Cu L1-shell", "Cu L2-shell", "Cu L3-shell", "Cu M1-shell", "Cu M2-shell", "Cu M3-shell", "Zn K-shell", "Zn L1-shell", "Zn L2-shell", "Zn L3-shell", "Zn M1-shell", "Zn M2-shell", "Zn M3-shell", "O K-shell", "Valence", "Total"]
# Create N distinct colors from a colormap
N = len(columns_to_plot)
colors = np.vstack([plt.cm.tab20(np.linspace(1, 0, 20)), plt.cm.tab20b(np.linspace(1, 0, 20))])
# Set line styles:
linestyles = [ "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
for i, col in enumerate(columns_to_plot):
    color = colors[i % len(colors)]
    ls    = linestyles[i % len(linestyles)]
    label = labels[i % len(labels)]
    plt.plot(df.iloc[:, 0], df.iloc[:, col],
    color=color,
    label=label,
    linestyle=ls)
plt.xlim(1.00000000,50000.00000000)
plt.ylim(10.00000000,10000000.00000000)
plt.title("Photon attenuation length")
plt.legend(loc="best", fontsize=9, ncol=2)
# Save the plot in this format:
plt.savefig("OUTPUT_MFP_photon.png", dpi=300, bbox_inches="tight")
