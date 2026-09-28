# Bachelor's Final Year Project

This paper was written as my bachelor's project under the supervision of Professor Bastien Chopard and Professor Pierre Leone.
In it, we modeled a lane-merging algorithm for autonomous vehicles and studied its performance when merging two lanes.

# Abstract
We consider the lane merging problem for autonomous cars. We implement a discrete simulation based on the concept
where the space is as a collection of cells of arbitrary size and cars are moving from one cell to another. The rules the
cars follow, are set by the "speed regulator", which bases the movement on the cars ahead. Once cars reach a point in
space called the merging point. The merging algorithm merges cars in an alternating sequence. The goal of this work is to
study the consequences of various flows in the bottle neck and try to show that unbalanced flows between lanes have similar
performance.

# Code
The algorithm is completly in C++, (mai18.cpp), I used python (numpy, pandas, mathplotlib) for the graphs and for a graphic 
représentation I used the tools given by Bastien Chopard in SpcTools. The project can be excetuded with this library.
