from collections import defaultdict
import csv
import os

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
output_file = "densite_temps.csv"

segments = [
    (-1000, -950),
    (200, 250),
    (3950, 4000)
]

counts = {f"{a}-{b}": defaultdict(int) for a, b in segments}
lengths = {f"{a}-{b}": (b - a) for a, b in segments}

if not os.path.exists(input_file):
    raise FileNotFoundError(f"{input_file} introuvable")

# lecture
with open(input_file, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        temps = int(row["temps"])
        position = float(row["position"])
        voie = int(row["voie"])

        if voie != 0:
            continue

        for a, b in segments:
            if a <= position <= b:
                label = f"{a}-{b}"
                counts[label][temps] += 1

# append
file_exists = os.path.exists(output_file)

with open(output_file, "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["temps", "segment", "densite"])


    for label, data in counts.items():
        L = lengths[label]

        for temps in sorted(data.keys()):
            densite = data[temps] / L
            writer.writerow([temps, label, densite])

print(f"{output_file} mis à jour (append)")