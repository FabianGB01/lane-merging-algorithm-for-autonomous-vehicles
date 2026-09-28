#!/bin/bash

# Récupération de N passé en argument
N=$1

if [ -z "$N" ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

SIM_DIR="/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv"
PY_DIR="/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv/densite/temps"

cd "$SIM_DIR" || exit
make sim

for ((i=1; i<=N; i++))
do
    echo "=============================="
    echo "Simulation $i / $N"
    echo "=============================="

    # Lancer simulation C++
    cd "$SIM_DIR" || exit
    ./sim

    cd "$PY_DIR" || exit
    python3 densite_temps.py
done

cd "$PY_DIR" || exit
python3 moyenne_densite_temps.py
python3 graphe_densite_temps.py

echo "Pipeline terminé."