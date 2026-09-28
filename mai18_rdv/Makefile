# Paths to your include and lib directories
INCLUDE_DIR = /home/fabman/Documents/VSCode/ProjetBachelor/SpcTools/Include
LIB_DIR = /home/fabman/Documents/VSCode/ProjetBachelor/SpcTools/Lib

# Compiler and flags
CXX = g++
CXXFLAGS = -O3 -I$(INCLUDE_DIR)
LDFLAGS = -L$(LIB_DIR) -L/usr/X11R6/lib -lMisc -lGI -lX11

# Targets
sim: mai18.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

test: test.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

clear:
	rm -f sim test positions.csv positions_meta.csv

	rm -f postion_du_front/*.csv
	rm -f postion_du_front/*.png

	rm -f densite/position/*.csv
	rm -f densite/position/*.png
	rm -f densite/temps/*.csv
	rm -f densite/temps/*.png

	rm -f vitesse/position/*.csv
	rm -f vitesse/position/*.png
	rm -f vitesse/temps/*.csv
	rm -f vitesse/temps/*.png

	rm -f flux/*.csv
	rm -f flux/*.png

	rm -f bouchon/*.csv
	rm -f bouchpn/*.png

	rm -f trajectoires/*.png
	