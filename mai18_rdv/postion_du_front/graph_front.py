import pandas as pd
import matplotlib.pyplot as plt

input_file = "/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/postion_du_front/position_chgmt_voie_complete.csv"

df = pd.read_csv(input_file)
df = df.sort_values(by="temps")

plt.figure(figsize=(10, 6))
plt.plot(df["temps"], df["position"])

plt.xlabel("Temps (s)")
plt.ylabel("Position")
plt.title("Position des changements de voie en fonction du temps")

plt.grid(True)
plt.savefig("graphe_bouchon.png")
plt.show()