import matplotlib.pyplot as plt

X = [0.5, 0.6, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2]
Y = [100, 100, 100, 100, 100, 75, 75, 75, 75, 75]

plt.figure(figsize=(8, 4))

plt.plot(X, Y, marker='o')

# Afficher toutes les valeurs de X sur l'axe
plt.xticks(X)

plt.xlabel("Flow of Q_in multiplied by a cste in relation to Q_max [X*Q_max]")
plt.ylabel("Percentage of the performance of the algo. [%]")
plt.title("Evolution of the effectivness of the merging depending of the Q_in")

plt.grid(True)
plt.savefig("Efficacite.png")
plt.show()