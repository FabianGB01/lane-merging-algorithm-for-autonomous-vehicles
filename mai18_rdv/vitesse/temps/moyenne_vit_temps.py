import csv
from collections import defaultdict

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/temps/vitesse_temps.csv"
output_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/temps/moyenne_vit_temps.csv"

# (temps, segment) -> [densités]
data = defaultdict(list)

# lecture
with open(input_file, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        temps = int(row["temps"])
        segment = row["segment"]
        mediane_vitesse = float(row["mediane_vitesse"])

        key = (temps, segment)
        data[key].append(mediane_vitesse)

# écriture moyenne
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["temps", "segment", "vitesse_moyenne"])

    for (temps, segment), values in sorted(data.items()):
        moyenne = sum(values) / len(values)
        writer.writerow([temps, segment, moyenne])

print("moyenne_vit_temps.csv généré avec succès !")

with open(input_file, "r") as f:
    lines = f.readlines()

header = lines[0] if lines else "temps,segment,dmediane_vitesse\n"

with open(input_file, "w") as f:
    f.write(header)

print("vitesse_temps.csv réinitialisé (header conservé)")