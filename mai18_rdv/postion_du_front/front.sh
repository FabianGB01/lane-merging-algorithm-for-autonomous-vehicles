#!/bin/bash

SIM_DIR="/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv"
DIR_front="$SIM_DIR/postion_du_front"

# Compilation simulation
cd "$SIM_DIR" || exit
make sim
./sim
echo "simulation réussie"

echo "Calcul du front..."
cd "$DIR_front" || exit
python3 position_chgmt_voie.py
echo "Front calculé !"

python3 graph_front.py
echo "script front.sh terminé"
