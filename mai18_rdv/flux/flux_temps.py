import pandas as pd
import os

file_path = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
output_path = "flux_temps.csv"

x_list = [-6000, 1000]
bin_size = 50  # période de mesure en secondes

df = pd.read_csv(file_path)

# trier par voiture et temps
df = df.sort_values(["id", "temps"])

# position de la voiture au pas suivant
df["pos_next"] = df.groupby("id")["position"].shift(-1)


all_flux = []

for x in x_list:

    # voitures qui traversent le détecteur pendant ce pas de temps
    cross = df[
        (df["position"] <= x) &
        (df["pos_next"] > x)
    ].copy()

    cross = cross.dropna(subset=["pos_next"])

    if cross.empty:
        continue

    # mettre chaque passage dans une fenêtre de temps
    cross["temps_bin"] = (cross["temps"] // bin_size) * bin_size

    # compter les voitures par fenêtre
    flux = (
        cross.groupby("temps_bin")
        .size()
        .reset_index(name="nb_voitures")
    )

    # convertir en voitures/seconde
    flux["flux"] = flux["nb_voitures"] / bin_size

    flux["position"] = x

    flux = flux.rename(columns={"temps_bin": "temps"})

    all_flux.append(flux)


final_flux = pd.concat(all_flux, ignore_index=True)

final_flux = final_flux[["position", "temps", "flux"]]

final_flux = final_flux.sort_values(["position", "temps"])


file_exists = os.path.isfile(output_path)

final_flux.to_csv(
    output_path,
    mode="a",
    header=not file_exists,
    index=False
)

print(f"Fichier sauvegardé : {output_path}")