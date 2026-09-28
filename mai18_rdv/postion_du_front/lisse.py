import pandas as pd

FICHIER = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/postion_du_front/position_chgmt_voie_test.csv"
OUTPUT = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/postion_du_front/position_chgmt_voie_complete.csv"


# Lecture
df = pd.read_csv(FICHIER)

# Trier par temps
df = df.sort_values("temps").reset_index(drop=True)


# Temps de début et fin
temps_min = int(df["temps"].min())
temps_max = int(df["temps"].max())


resultats = []

# Position précédente
position_precedente = None

# Index pour parcourir le fichier
index = 0


# Pour chaque seconde
for t in range(temps_min, temps_max + 1):

    # Si on a une donnée à ce temps
    if index < len(df) and df.loc[index, "temps"] == t:

        position_precedente = df.loc[index, "position"]

        resultats.append({
            "temps": t,
            "position": position_precedente
        })

        index += 1

    # Sinon on répète la dernière position
    else:

        resultats.append({
            "temps": t,
            "position": position_precedente
        })


# Sauvegarde
df_out = pd.DataFrame(resultats)

df_out.to_csv(OUTPUT, index=False)

print(f"{len(df_out)} lignes écrites dans {OUTPUT}")