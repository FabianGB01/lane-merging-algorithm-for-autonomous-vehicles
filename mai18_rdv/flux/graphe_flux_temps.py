import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

file_path = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/flux/mediane_flux_temps.csv"

df = pd.read_csv(file_path)
df["time"] = df["temps"]

plt.figure(figsize=(14, 20))
labels = ["Q_in at position -6000", "Q_out at position 1000"]

for i, position in enumerate(df["position"].unique()):
    subset = df[df["position"] == position]

    plt.plot(
        subset["time"],
        subset["flux"],
        label=labels[i]
    )

plt.xlabel("Time [s]")
plt.ylabel("Flow [cars/s]")
plt.title("Flow of cars at a position through time")
plt.legend()

# Récupération des axes
ax = plt.gca()

# Graduations principales
ax.xaxis.set_major_locator(MultipleLocator(56))
ax.yaxis.set_major_locator(MultipleLocator(0.01))

# Grille sur les graduations principales
ax.grid(True, which="major", axis="x")
ax.grid(True, which="major", axis="y")

plt.savefig("graphe_flux_temps_ordre.png")
plt.show()