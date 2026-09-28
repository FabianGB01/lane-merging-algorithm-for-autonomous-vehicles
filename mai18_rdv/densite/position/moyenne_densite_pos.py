import csv
from collections import defaultdict

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/densite/position/densite_pos.csv"
output_file = "moyenne_densite_pos.csv"

# (temps, segment) -> [densités]
data = defaultdict(list)

# lecture
with open(input_file, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        temps = int(row["temps"])
        segment = row["segment"]
        densite = float(row["densite"])

        key = (temps, segment)
        data[key].append(densite)

# écriture moyenne
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["temps", "segment", "densite_moyenne"])

    for (temps, segment), values in sorted(data.items()):
        moyenne = sum(values) / len(values)
        writer.writerow([temps, segment, moyenne])

print("moyenne_densite_pos.csv généré avec succès !")

with open(input_file, "r") as f:
    lines = f.readlines()

header = lines[0] if lines else "temps,segment,densite\n"

with open(input_file, "w") as f:
    f.write(header)

print("densite_pos.csv réinitialisé (header conservé)")