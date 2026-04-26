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
df = pd.read_csv(r"OUTPUT_Cu_on_Si_Photon_IMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
plt.xscale("log")
plt.yscale("log")
# Prepare the plot:
columns_to_plot = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
labels = [ "Cu K-shell", "Cu L1-shell", "Cu L2-shell", "Cu L3-shell", "Cu M1-shell", "Cu M2-shell", "Cu M3-shell", "Si K-shell", "Si L1-shell", "Si L2-shell", "Si L3-shell", "Valence", "Total"]
# Create N distinct colors from a colormap
N = len(columns_to_plot)
colors = plt.cm.tab20(np.linspace(1, 0, 20))
# Set line styles:
linestyles = [ "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
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
plt.legend(loc="best", fontsize=10)
# Save the plot in this format:
plt.savefig("OUTPUT_MFP_photon.png", dpi=300, bbox_inches="tight")
