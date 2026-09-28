import pandas as pd
import os

file_path = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/flux/flux_temps.csv"
output_file = "mediane_flux_temps.csv"

df = pd.read_csv(file_path)
result = df.groupby(
    ["position", "temps"]
)["flux"].mean().reset_index()

result.to_csv(output_file, index=False)

df_empty = pd.DataFrame(columns=df.columns)
df_empty.to_csv(file_path, index=False)

print("Médiane calculée → mediane_flux_temps.csv")
print("Fichier input vidé (header conservé).")