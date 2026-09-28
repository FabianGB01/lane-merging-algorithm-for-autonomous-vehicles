import pandas as pd
import os

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
output_dir = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/postion_du_front"
output_file = os.path.join(output_dir, "position_chgmt_voie.csv")

# Tri par voiture puis temps
df = pd.read_csv(input_file)
df = df.sort_values(by=["id", "temps"])

resultats = []

# Parcours de chaque voiture
for car_id, group in df.groupby("id"):

    group = group.reset_index(drop=True)

    for i in range(1, len(group)):

        prev_lane = group.loc[i - 1, "voie"]
        curr_lane = group.loc[i, "voie"]

        # Détection du changement 1 -> 0
        if prev_lane == 1 and curr_lane == 0:

            prev_position = group.loc[i - 1, "position"]
            prev_time = group.loc[i - 1, "temps"]

            resultats.append({
                "temps": prev_time,
                "position": prev_position
            })

os.makedirs(output_dir, exist_ok=True)
out_df = pd.DataFrame(resultats)
out_df.to_csv(output_file, index=False)

print("Fichier créé :", output_file)
print("Position of the front through time :", len(resultats))