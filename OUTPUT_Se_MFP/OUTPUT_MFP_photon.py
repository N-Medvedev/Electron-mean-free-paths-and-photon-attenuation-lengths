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
df = pd.read_csv(r"OUTPUT_Se_Photon_IMFP.dat", sep=r'\s+', header=None, comment="#", skipinitialspace=True)
plt.xscale("log")
plt.yscale("log")
# Prepare the plot:
columns_to_plot = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
labels = [ "Se K-shell", "Se L1-shell", "Se L2-shell", "Se L3-shell", "Se M1-shell", "Se M2-shell", "Se M3-shell", "Se M4-shell", "Se M5-shell", "Valence", "Total"]
# Create N distinct colors from a colormap
N = len(columns_to_plot)
colors = plt.cm.tab20(np.linspace(1, 0, 20))
# Set line styles:
linestyles = [ "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
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
