import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Charger les données
df = pd.read_csv("/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/bouchon/bouchon.csv")

# Supprimer les lignes sans bouchon
df = df.dropna(subset=["queue", "tete"])

# Plot
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].xaxis.set_major_locator(MultipleLocator(50))
ax[0].yaxis.set_major_locator(MultipleLocator(1))

ax[0].plot(df["temps"], df["queue"], label="Tail of the jam")
ax[0].plot(df["temps"], df["tete"], label="Head of the jam")
ax[0].set_xlabel("Time [s]")
ax[0].set_ylabel("Position [m]")
ax[0].set_title("Position of the head and tail of the jam")
ax[0].legend()
ax[0].grid()


ax[1].xaxis.set_major_locator(MultipleLocator(50))
ax[1].yaxis.set_major_locator(MultipleLocator(1))

ax[1].plot(df["temps"], df["taille"], color="red")
ax[1].set_xlabel("Time [s]")
ax[1].set_ylabel("Position [m]")
ax[1].set_title("Size of the jam")
ax[1].grid()

plt.tight_layout()
plt.savefig("graph_bouchon.png")
#plt.show()
