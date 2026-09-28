import pandas as pd
import matplotlib.pyplot as plt

L = ["Qmax/2","Qmax/1.75", "Qmax/1.5", "Qmax/1.25", "Qmax/1.23", 
     "Qmax/1.20", "Qmax/1.14", "Qmax/1.10", "Qmax/1.05", 
     "Qmax", "1.38Qmax", "1.5Qmax", "1.75Qmax", "1.83Qmax", "2Qmax"]

multi = [1/2, 4/7, 2/3, 4/5, 100/123, 5/6, 50/57, 10/11, 20/21, 1, 1.38, 1.5, 1.75, 1.83, 2]

IN = [0.424, 0.485, 0.566, 0.679, 0.691, 0.709, 0.747, 
      0.767, 0.812, 0.848, 1.167, 1.273, 1.474, 1.556, 1.697]
OUT = [0.424, 0.485, 0.566, 0.46, 0.48, 0.67, 0.66, 0.50, 0.50, 0.50, 0.50, 0.43, None, None, None]
OUT_inverse = [0.424, 0.485, 0.566, 0.50, 0.68, 0.68, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, None, None, None]


Qmax = 28/33

rep = []

for i in multi :
    D0 = (42/(i*Qmax)) - 5
    D1 = (84/(i*Qmax)) - 5
    tuplle = (D0, D1)
    rep.append(tuplle)

print(rep)
    


