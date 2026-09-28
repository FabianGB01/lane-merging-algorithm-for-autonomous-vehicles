import csv
from collections import defaultdict
import matplotlib.pyplot as plt

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/temps/moyenne_vit_temps.csv"

# structure : segment -> (temps, vitesse_moyenne)
data = defaultdict(lambda: {"temps": [], "vitesse_moyenne": []})

# lecture du CSV
with open(input_file, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        temps = int(row["temps"])
        segment = row["segment"]
        vitesse_moyenne = float(row["vitesse_moyenne"])

        data[segment]["temps"].append(temps)
        data[segment]["vitesse_moyenne"].append(vitesse_moyenne)

plt.figure()

for segment, values in data.items():
    plt.plot(values["temps"], values["vitesse_moyenne"], label=f"Segment {segment}")

plt.xlabel("Time [s]")
plt.ylabel("Median speed [m/s]")
plt.title("Median speed by segment through time")
plt.legend()
plt.grid(True)

plt.savefig("graphe_vitesse_temps.png")
#plt.show()