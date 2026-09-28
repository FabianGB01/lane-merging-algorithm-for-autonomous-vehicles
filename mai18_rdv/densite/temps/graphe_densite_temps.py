import csv
from collections import defaultdict
import matplotlib.pyplot as plt

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/densite//temps/moyenne_densite_temps.csv"

# structure : segment -> (temps, densité)
data = defaultdict(lambda: {"temps": [], "densite": []})

# lecture 
with open(input_file, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        temps = int(row["temps"])
        segment = row["segment"]
        densite = float(row["densite_moyenne"])

        data[segment]["temps"].append(temps)
        data[segment]["densite"].append(densite)

plt.figure()

for segment, values in data.items():
    plt.plot(values["temps"], values["densite"], label=f"Segment {segment}")

plt.xlabel("Time [s]")
plt.ylabel("Average desnity [cars/m]")
plt.title("Density in a segment through time")
plt.legend()
plt.grid(True)

plt.savefig("graphe_densité_temps.png")
#plt.show()