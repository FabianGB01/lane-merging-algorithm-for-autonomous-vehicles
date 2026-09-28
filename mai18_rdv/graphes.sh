#!/bin/bash
set -euo pipefail

# Récupération de N passé en argument
N=$1

if [ -z "$N" ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

SIM_DIR="/home/fabman/Documents/VSCode/ProjetBachelor/mai18_rdv"

DIR_vit_temps="$SIM_DIR/vitesse/temps"
DIR_vit_pos="$SIM_DIR/vitesse/position"

DIR_front="$SIM_DIR/postion_du_front"

DIR_flux="$SIM_DIR/flux"

DIR_bouchon="$SIM_DIR/bouchon"

DIR_trajectoire="$SIM_DIR/trajectoires"

DIR_densite_temps="$SIM_DIR/densite/temps"
DIR_densite_pos="$SIM_DIR/densite/position"

# Compilation simulation
cd "$SIM_DIR" || exit
make sim

# Vitesse temps
cd "$DIR_vit_temps" || exit
./vitesse_temps.sh "$N"

# Vitesse position
cd "$DIR_vit_pos" || exit
./vitesse_pos.sh "$N"

# Flux 
cd "$DIR_flux" || exit
./flux_temps.sh "$N"

#Bouchon
cd "$DIR_bouchon" || exit
./bouchon.sh "$N"

# position du front
cd "$DIR_front" || exit
./front.sh

# Trajectoire
cd "$DIR_trajectoire"
python3 trajectoires.py

# Densité temps
cd "$DIR_densite_temps" || exit
./densite_temps.sh "$N"

# Densité position
cd "$DIR_densite_pos" || exit
./densite_pos.sh "$N"

echo "Tout a été réussi"