import pandas as pd
import os

FICHIER = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
OUTPUT = "bouchon.csv"

SEUIL_VITESSE = 5
VOIE = 0
ID_EXCLU = 0

df = pd.read_csv(FICHIER)

# filtre global
df = df[(df["voie"] == VOIE) & (df["id"] != ID_EXCLU)]

resultats = []

for t, groupe in df.groupby("temps"):

    bouchon = groupe[groupe["vitesse"] < SEUIL_VITESSE]

    if bouchon.empty:
        continue

    queue = bouchon["position"].min()
    tete = bouchon["position"].max()

    resultats.append({
        "temps": t,
        "queue": queue,
        "tete": tete,
        "taille": tete - queue
    })

df_out = pd.DataFrame(resultats)

# --- APPEND LOGIC ---
file_exists = os.path.isfile(OUTPUT)

df_out.to_csv(
    OUTPUT,
    mode="a",
    header=not file_exists,
    index=False
)

print(f"Écrit {len(df_out)} lignes dans {OUTPUT}")
