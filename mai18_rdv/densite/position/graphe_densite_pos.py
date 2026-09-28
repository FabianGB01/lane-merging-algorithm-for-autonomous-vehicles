import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/densite/position/moyenne_densite_pos.csv"
)

# extraction des bornes
df[["seg_min", "seg_max"]] = (
    df["segment"]
    .str.split("/", expand=True)
    .astype(float)
)

# position centrale
df["position"] = (df["seg_min"] + df["seg_max"]) / 2

# moyenne temporelle
df_mean = (
    df.groupby("position", as_index=False)["densite_moyenne"]
    .mean()
    .sort_values("position")
)

positions = df_mean["position"].values
densite = df_mean["densite_moyenne"].values

heatmap = densite.reshape(1, -1)

plt.figure(figsize=(12, 2))

# largeur des cellules
step = np.diff(positions).mean()

pos_edges = np.append(
    positions - step / 2,
    positions[-1] + step / 2
)

plt.pcolormesh(
    pos_edges,
    [0, 1],
    heatmap,
    cmap="inferno",
    shading="flat"
)

plt.yticks([])
plt.xlabel("Position [m]")
plt.title("1D heatmap of the density in space")

plt.colorbar(label="Density [cars/m]")

plt.tight_layout()
plt.savefig("graphe_densite_pos.png")
#plt.show()