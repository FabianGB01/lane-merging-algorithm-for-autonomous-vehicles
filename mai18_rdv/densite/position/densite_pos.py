from collections import defaultdict
import csv
import os

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
output_file = "densite_pos.csv"

segments = [
    (-450, -400),
    (-400, -350),
    (-350, -300),
    (-300, -250),
    (-250, -200),
    (-200, -150),
    (-150, -100),
    (-100, -50),
    (-50, 0),
    (0, 50),
    (50, 100),
    (100, 150),
    (150, 200),
    (250, 300),
    (300, 350),
    (350, 400),
    (400, 450),
    (450, 500)
]

counts = {f"{a}/{b}": defaultdict(int) for a, b in segments}
lengths = {f"{a}/{b}": (b - a) for a, b in segments}

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
            if a <= position < b:  
                label = f"{a}/{b}"
                counts[label][temps] += 1
                break

# append
file_exists = os.path.exists(output_file)

with open(output_file, "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["temps", "segment", "densite"])


    for label, data in counts.items():
        L = lengths[label]

        for temps in sorted(data.keys()):
            densite = (data[temps] / L)
            writer.writerow([temps, label, densite])

print(f"{output_file} mis à jour (append)")