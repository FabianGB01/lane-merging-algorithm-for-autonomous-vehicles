#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <thread>
#include <chrono>
#include <limits>
#include <random>

#include "GraphicsInterface.hh"
#include "Random.hh"

using namespace std;

GraphicsInterface window;
Matrix<unsigned char> image;




class Vehicule {
public:
// invariables
    int id;
    int taille_vhcl;     // cases (min=1)
    int V_max;

// Etat courrant: t
    int position;           // 1D, ordre sur la route
    int vitesse;         // cases/t    
    int8_t voie;            // 0=autoroute; 1=bande accélération

// Etat futur: t+1
    int next_position;
    int next_vitesse;
    int8_t next_voie;

// Sauvgarde des positions passées.
    vector<std::tuple<int, int, int, int8_t>> historique_positions;


    Vehicule(int _id, int _pos, int _vit, int _taille, int _vmax, int8_t _voie):
        id(_id), 
        position(_pos), 
        vitesse(_vit), 
        taille_vhcl(_taille), 
        V_max(_vmax), 
        voie(_voie),
        next_position(_pos), 
        next_vitesse(_vit), 
        next_voie(_voie),
        historique_positions{make_tuple(_id, _pos, _vit, _voie)} {}
};




int DF(int v){
    return (v * (v + 1)) / 2;
}



/*
void Regulateur_de_vitesse(Vehicule &A, const Vehicule &B){
    int Vmin = 0;
    int vb = B.vitesse;
    int va = A.vitesse;
    int distance = (B.position - B.taille_vhcl) - A.position;
    int next_vitesse;

    if(distance < (2*B.vitesse)){
        if ((distance - B.vitesse) + DF(vb-1) >= DF(va+1) && va < A.V_max) { next_vitesse = va + 1; }
        else if ((distance - B.vitesse) + DF(vb-1) >= DF(va)) { next_vitesse = va; }
        else { if(va>Vmin) {next_vitesse = va - 1; } else{if(A.voie == 0 && B.voie == 0) {printf("cars1 %d, cars2 %d, dist %d\n", A.id, B.id, distance);}}}
    }
    else{
        if (distance + DF(vb-1) >= DF(va+1) && va < A.V_max) { next_vitesse = va + 1; }
        else if (distance + DF(vb-1) >= DF(va)) { next_vitesse = va; }
        else { 
            if(va>Vmin) {
                next_vitesse = va - 1; 
            } 
            else{
                cout << "\nERREUR: probleme dans le regulateur de vitesse.\n" << endl;
            }
        }
    }

    A.next_vitesse = next_vitesse;
    A.next_position = A.position + next_vitesse;
}*/

void Regulateur_de_vitesse(Vehicule &A, const Vehicule &B){
    int vb = B.vitesse;
    int va = A.vitesse;
    int distance = (B.position - B.taille_vhcl) - A.position;
    //if(B.id == 100) {printf("dist=%d\n", distance);}
    int next_vitesse = 0;

    if (distance + DF(vb-1) >= DF(va+1) && va+1 <= A.V_max) { next_vitesse = va + 1; }
        else if (distance + DF(vb-1) >= DF(va)) { next_vitesse = va; }
        else { 
            if(va>0) {
                next_vitesse = va - 1; 
            } 
            else{
                if(A.voie == B.voie){
                    printf("\nERREUR: voiture A va entrer en collision avec B. dist=%d car=%d vit=%d et car=%d vit=%d, pos=%d\n", distance, A.id, A.vitesse, B.id, B.vitesse, A.position);
                }
            }
        }

    A.next_vitesse = next_vitesse;
    A.next_position = A.position + next_vitesse;
}




void Appliquer_changements(vector<Vehicule> &vehicules){
    for (auto &v : vehicules) {
        v.vitesse = v.next_vitesse;
        v.position = v.next_position;
        v.voie = v.next_voie;
        v.historique_positions.push_back(make_tuple(v.id, v.position, v.vitesse, v.voie));
    }
}




void drawRoad(const vector<Vehicule>& vehicules, int longueur_route, int largeur_route, int largeur_vehicule, int debut_merging) {

    // Fond blanc
    for (int i = 0; i < longueur_route; i++)
        for (int j = 0; j < largeur_route; j++)
            image.set(j, i, 0);

    // Ligne noire du haut
    for (int i = 0; i < longueur_route; i++)
        for (int t = 0; t < 5; t++)
            image.set(5 + t, i, 1);
        
    // Ligne jaune du milieu
    for (int i = 0; i < longueur_route; i++)
        if ((i % 30) < 15)
            for (int t = 0; t < 3; t++)
                image.set(39 + t, i, 35);
        
    // Ligne noire du bas
    for (int i = 0; i < longueur_route; i++)
        for (int t = 0; t < 5; t++)
            image.set(70 + t, i, 1);

    // Ligne signal début merging
    for (int i = 10; i < 70; i++)
        for (int j = 0; j < 3; j++)
            image.set(i, j+(debut_merging - 3), 1);

    // Vehicules
    // voie 0
    for (const auto& car : vehicules) {
        int longueur_reelle = car.taille_vhcl;

        if (car.voie == 0){
            for (int j = 0; j < largeur_vehicule; j++) {
                for (int i = 0; i < longueur_reelle; i++) {
                    int y = largeur_vehicule + j;
                    int x = (car.position - longueur_reelle) + i;

                    if (y < largeur_route && x < longueur_route && x >= 0)
                        image.set(y, x, car.id*12);
                }
            }
        } 
    // voie 1
        else if (car.voie == 1){
            for (int j = 0; j < largeur_vehicule; j++) {
                for (int i = 0; i < longueur_reelle; i++) {
                    int y = largeur_vehicule + j + 35;
                    int x = (car.position - longueur_reelle) + i;

                    if (y < largeur_route && x < longueur_route && x >= 0){
                        image.set(y, x, car.id*12);
                    } 
                }
            }
        }
    }

    window.drawMatrix(image);
}

/*
// Il y a des cas après la ligne de merge quand A sur voie 0 suit B sur voie 1. il arrive que a un moment B depasse C qui est a l'arret sur 
// la voie 0, et comme A suit B, A va vite et soudainement la voiture devant elle n'est plus B mais C à l'arret. A n'as plus le temps de freiner.
int Distance_prochaine_car_voie_0(vector<Vehicule>& vehicules, int i){      
    for (int j = i + 1; j < vehicules.size(); j++) {
        if (vehicules[j].voie != 0) {continue;}
        int distance = (vehicules[j].position - vehicules[j].taille_vhcl) - vehicules[i].position;
        int security = vehicules[1].taille_vhcl + ((pow(vehicules[i].vitesse, 2) - pow(vehicules[j].vitesse, 2)) / 2);    // distance pour s'arreter net
        
        if(security < distance){
            return -1;
        }
        else{
            return j;
        }
    }
    return -1;
}
*/



void Regulateur_voie_0(vector<Vehicule>& vehicules, int debut_merging) {
    for (int i = 0; i < vehicules.size() - 1; i++) {
        if (vehicules[i].voie != 0) continue;
        for (int j = i + 1; j < vehicules.size(); j++) {
            // AVANT merging : seulement voie 0
            if (vehicules[i].position < debut_merging) {
                if (vehicules[j].voie == 0) {
                    Regulateur_de_vitesse(vehicules[i], vehicules[j]);
                    break;
                }
            }
            // APRÈS merging : première voiture devant peu importe la voie
            else {
                //int z = Distance_prochaine_car_voie_0(vehicules, i);
                //if(z == -1){
                    Regulateur_de_vitesse(vehicules[i], vehicules[j]);
                    break;
                //}
                //else{
                    //Regulateur_de_vitesse(vehicules[i], vehicules[z]);
                    //break;
                //}
            }
        }
    }
}




void Regulateur_voie_1(vector<Vehicule>& vehicules, int debut_merging){
    for (int i = 0; i < vehicules.size() - 1; i++) {
        if (vehicules[i].voie != 1) { continue; }
        for (int j = i + 1; j < vehicules.size(); j++) {
            // AVANT merging : seulement voie 1
            if (vehicules[j].position < debut_merging) {
                if (vehicules[j].voie == 1) {
                    Regulateur_de_vitesse(vehicules[i], vehicules[j]);
                    break;
                }
            }
            // APRÈS merging : première voiture devant peu importe la voie
            else {
                Regulateur_de_vitesse(vehicules[i], vehicules[j]);
                break;
            }
        }
    }
}




bool Verificateur_De_Distance(const Vehicule &A, const Vehicule &B, const int distance_securite){
    int va = A.vitesse;
    int vb = B.vitesse;
    int distance = (B.position - B.taille_vhcl) - A.position;
    if (distance < 0){ return false; }
    
    if (distance >= distance_securite){ return true; }
    else { return false; }
}



/*
bool Is_Leading_Car(vector<Vehicule>& vehicules, int i){
    for (int j=i+1; j < vehicules.size(); j++){
        if(vehicules[j].voie==1){
            return false;
        }
    }
    return true;
}
*/



void Incorporation(vector<Vehicule>& vehicules, const int distance_securite, int debut_merging){
    bool distDevant = False;
    bool distDerriere = False;

    for (int i=0; i < (vehicules.size()-1); i++){
        if(vehicules[i].voie != 1 || vehicules[i].position < debut_merging){continue;}    // Si la voiture est sur voie 1 et pos >= 200

        for (int j=i-1; j >= -1; j--){   // On cherche une voiture sur la voie 0 derrière
            if(i == 0){       // Si c'est la derniere voiture de la liste
                distDerriere = True;
                break;
            }
            if(vehicules[j].voie == 0){ // Si la voiture derrière est sur la voie 0
                distDerriere = Verificateur_De_Distance(vehicules[j], vehicules[i], distance_securite);
                break;
            }

        }

        for (int j=i+1; j < vehicules.size(); j++){   // On cherche une voiture sur la voie 0 devant
            if(vehicules[j].voie == 0){     // Si la voiture devant est sur la voie 0
                distDevant = Verificateur_De_Distance(vehicules[i], vehicules[j], distance_securite);
                break;
            }
        }

        if (distDevant){
            if (distDerriere){
                // incorporation
                //if (Is_Leading_Car(vehicules, i)){
                    vehicules[i].next_voie = 0;
                //}
            }
        }
    }
}




void ExportPositions(const std::vector<Vehicule>& vehicules, int T, const std::string& filename, int distance_securite)
{
    std::ofstream file(filename);

    if (!file.is_open()) {
        std::cerr << "Erreur ouverture fichier.\n";
        return;
    }

    int nb_vehicules = vehicules.size() - 1;

    // En-tête CSV
    file << "temps,id,position,vitesse,voie,nb_vehicules\n";

    for (const auto& vh : vehicules) {

        for (size_t t = 0; t < vh.historique_positions.size(); ++t) {

            const auto& [id, pos, vit, voie] =
                vh.historique_positions[t];

            file << t << ","
                 << id << ","
                 << pos << ","
                 << vit << ","
                 << (int)voie << ","
                 << nb_vehicules
                 << "\n";
        }
    }

    file.close();

    // 👉 fichier meta séparé
    std::string meta_file = "positions_meta.csv";
    std::ofstream meta(meta_file);

    if (meta.is_open()) {
        meta << "nb_vehicules,";
        meta << "vmax,";
        meta << "distance_securite\n";
        meta << (vehicules.size() - 1) << ",";
        meta << vehicules[1].V_max << ",";
        meta << distance_securite << "\n";
        meta.close();
    }
}




vector<Vehicule> Traffic_Generator(int Nbr_cars_start, int Nbr_cars_end, int vmax, int longeure_vehicule, int8_t voie, int start, int densite){
    vector<Vehicule> vehicules;

    random_device rd;
    mt19937 gen(rd());
    //exponential_distribution<> variation(lambda);

    int position = start;

    for (int i = Nbr_cars_start; i <= Nbr_cars_end; i++) {
        //double noise = variation(gen);
        int gap = longeure_vehicule + vmax + densite;

        vehicules.emplace_back(
            i,
            position,
            vmax,
            longeure_vehicule,
            vmax,
            voie
        );

        position -= gap;
    }

    return vehicules;
}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main(){
    int longueur_route = 1900;
    int largeur_route = 80; 
    int longeure_vehicule = 5;
    int largeur_vehicule = 15;      // Taille standard des vehicules verticalement
    window.open(largeur_route+10, longueur_route+10); 
    image.setDimension(largeur_route, longueur_route);

    int vitesse = 28;
    int distance_securite = vitesse;
    int debut_merging = 200;
    int densite = 47;

    vector<Vehicule> vehicules;
    vehicules.emplace_back(0, 4'000'000, 0, 1, 0, 0);  // voiture 0, CAS LIMITE

    // 1. Initialisation des voitures
    // Traffic_Generator(id_first_car, id_last_car, vmax, longeure_vehicule, voie, start, densite, tolerance)

    
    auto lane0 = Traffic_Generator(1, 2000, vitesse, longeure_vehicule, 0, 200, 89);
    auto lane1 = Traffic_Generator(2001, 4000, vitesse, longeure_vehicule, 1, 200, 28);

    vehicules.insert(vehicules.end(), lane0.begin(), lane0.end());
    vehicules.insert(vehicules.end(), lane1.begin(), lane1.end());
    

    int T = 1000; // nombre de pas de temps
    for (int t = 0; t < T; ++t) {

        // 2. Trier la liste des vehicules
        sort(vehicules.begin(), vehicules.end(), [](const Vehicule &a, const Vehicule &b) {
            return a.position < b.position;
        });

        // 3. Afficher l'état courant
        drawRoad(vehicules, longueur_route, largeur_route, largeur_vehicule, debut_merging);
        this_thread::sleep_for(chrono::milliseconds(200));

        // 4. Identifie quelles voitures peuvent changer de voie
        Incorporation(vehicules, distance_securite, debut_merging);

        // 5. Calculer l'état futur de toutes les voitures
        Regulateur_voie_0(vehicules, debut_merging);
        Regulateur_voie_1(vehicules, debut_merging);

        // 6. Appliquer les changements.
        Appliquer_changements(vehicules);
    }

    
    ExportPositions(vehicules, T, "positions.csv", distance_securite);

    window.close();

    return 0;
}
