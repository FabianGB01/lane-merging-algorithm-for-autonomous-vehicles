import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Charger le fichier CSV
df = pd.read_csv("/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv")

# Exclure la voiture d'ID 0
df = df[df["id"] != 0]

# Filtrer jusqu'au temps voulu
t_min = 0
t_max = 10
df = df[(df["temps"] >= t_min) & (df["temps"] <= t_max)]

# Sélection des véhicules
ids = [10, 11, 12, 13]
#ids = sorted(df["id"].unique())
df_filtre = df[df["id"].isin(ids)]

# Création de la figure
plt.figure(figsize=(12, 8))

for vehicule_id, groupe in df_filtre.groupby("id"):

    # Trier les données par temps
    groupe = groupe.sort_values("temps").reset_index(drop=True)

    # Tracer chaque segment séparément
    for i in range(len(groupe) - 1):

        t1 = groupe.loc[i, "temps"]
        t2 = groupe.loc[i + 1, "temps"]

        p1 = groupe.loc[i, "position"]
        p2 = groupe.loc[i + 1, "position"]

        # Couleur selon la voie au point d'arrivée
        voie = groupe.loc[i + 1, "voie"]

        couleur = "red" if voie == 1 else "blue"

        plt.plot(
            [t1, t2],
            [p1, p2],
            color=couleur,
            linewidth=1
        )

# Axes et titre
plt.xlabel("Time (s)")
plt.ylabel("Position")
plt.title(f"Position of cars between t = {t_min}s and t = {t_max}s")

# Graduations
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(10))

# Grille
plt.grid(True, which="major", axis="x")
plt.grid(True, which="major", axis="y")

# Grille normale
plt.grid(True, which="major", axis="x")
plt.grid(True, which="major", axis="y")

# Ligne horizontale plus épaisse à y = 200
#plt.axhline(y=200, color="black", linewidth=1.5)

# Légende
plt.plot([], [], color="blue", label="Lane 0")
plt.plot([], [], color="red", label="Lane 1")
plt.legend()

plt.tight_layout()
plt.savefig("trajectoires.png", dpi=300)
plt.show()