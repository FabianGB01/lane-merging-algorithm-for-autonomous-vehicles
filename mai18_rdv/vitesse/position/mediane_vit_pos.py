import pandas as pd

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/position/vitesse_pos.csv"
output_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/position/mediane_vit_pos.csv"

df = pd.read_csv(input_file)
df["vitesse"] = pd.to_numeric(df["vitesse"], errors="coerce")

# Calcul de la médiane par position
result = df.groupby("position", as_index=False)["vitesse"].median()
result.rename(columns={"vitesse": "mediane_vitesse"}, inplace=True)

result.to_csv(output_file, index=False)
print("Fichier exporté :", output_file)

with open(input_file, "r") as f:
    lines = f.readlines()

header = lines[0] if lines else "temps,id,position,vitesse,voie,nb_vehicules\n"

with open(input_file, "w") as f:
    f.write(header)

print("vitesse.csv réinitialisé (header conservé)")