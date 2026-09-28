from collections import defaultdict
import csv
import os
import statistics

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
output_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/temps/vitesse_temps.csv"

segments = [
    (-500, -400)
]

# stocke les vitesses par segment et par temps
speeds = {f"{a}-{b}": defaultdict(list) for a, b in segments}

if not os.path.exists(input_file):
    raise FileNotFoundError(f"{input_file} introuvable")

# lecture
with open(input_file, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            temps = int(row["temps"])
            position = float(row["position"])
            voie = int(row["voie"])
            vitesse = float(row["vitesse"])
        except ValueError:
            continue

        if voie != 0:
            continue

        for a, b in segments:
            if a <= position < b:
                label = f"{a}-{b}"
                speeds[label][temps].append(vitesse)

# écriture
file_exists = os.path.exists(output_file)

with open(output_file, "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["temps", "segment", "mediane_vitesse"])

    for label, data in speeds.items():
        for temps in sorted(data.keys()):
            if len(data[temps]) > 0:
                mediane = statistics.median(data[temps])
                writer.writerow([temps, label, mediane])

print(f"{output_file} mis à jour")