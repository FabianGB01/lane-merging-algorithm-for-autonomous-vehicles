import csv
import os

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/positions.csv"
output_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/vitesse/position/vitesse_pos.csv"

file_exists = os.path.isfile(output_file)

with open(input_file, mode="r", newline="") as infile, \
     open(output_file, mode="a", newline="") as outfile:

    reader = csv.DictReader(infile)

    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()

    for row in reader:
        try:
            t = int(row["position"])
            voie = int(row["voie"])
        except ValueError:
            continue

        if t % 5 == 0 and voie == 0:
            writer.writerow(row)