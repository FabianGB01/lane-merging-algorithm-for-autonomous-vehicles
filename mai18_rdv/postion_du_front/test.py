import pandas as pd

FICHIER = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/postion_du_front/position_chgmt_voie.csv"
OUTPUT = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/postion_du_front/position_chgmt_voie_test.csv"

SEUIL = 0.10  # 10 %

# Lecture
df = pd.read_csv(FICHIER)

# Trier selon le temps
df = df.sort_values("temps").reset_index(drop=True)

# Correction des valeurs
for i in range(1, len(df)):

    ancienne_position = df.loc[i-1, "position"]
    position_actuelle = df.loc[i, "position"]

    variation = abs(position_actuelle - ancienne_position) / abs(ancienne_position)

    if variation > SEUIL:
        df.loc[i, "position"] = ancienne_position


# Sauvegarde
df.to_csv(OUTPUT, index=False)

print(f"{len(df)} lignes écrites dans {OUTPUT}")