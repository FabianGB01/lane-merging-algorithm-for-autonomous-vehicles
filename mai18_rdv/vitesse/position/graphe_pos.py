import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/position/mediane_vit_pos.csv")

# garder uniquement entre 2 bornes
borne_min = -100
borne_max = 0
df_zoom = df[(df["position"] >= borne_min) & (df["position"] <= borne_max)]

df_zoom = df_zoom.sort_values("position")

positions = df_zoom["position"].values
vitesses = df_zoom["mediane_vitesse"].values

heatmap = vitesses.reshape(1, -1)

plt.figure(figsize=(12, 2))

plt.pcolormesh(
    np.append(positions - 2.5, positions[-1] + 2.5), 
    [0, 1],
    heatmap,
    cmap="inferno",
    shading="flat"
)

plt.yticks([])
plt.xlabel("Position [m]")
plt.title(f"1D heatmap of median speed in segement : [{borne_min} ; {borne_max}]")

plt.colorbar(label="Speed [m/s]")
plt.tight_layout()
plt.savefig("graphe_vitesse_pos.png")
#plt.show()