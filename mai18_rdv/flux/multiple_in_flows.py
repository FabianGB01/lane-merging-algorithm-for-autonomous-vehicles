import pandas as pd
import matplotlib.pyplot as plt

L = ["Qmax/2","Qmax/1.75", "Qmax/1.5", "Qmax/1.25", "Qmax/1.23", 
     "Qmax/1.20", "Qmax/1.14", "Qmax/1.10", "Qmax/1.05", 
     "Qmax", "1.38Qmax", "1.5Qmax", "1.75Qmax", "1.83Qmax", "2Qmax"]

OUT_normal = [0.424, 0.485, 0.566, 0.67, 0.67, 0.67, 0.67 ,0.67, 0.5, 0.5 ,0.5 ,0.5 ,0.5, 0.43, 0.42]

IN = [0.424, 0.485, 0.566, 0.679, 0.691, 0.709, 0.747, 
      0.767, 0.812, 0.848, 1.167, 1.273, 1.474, 1.556, 1.697]

OUT = [0.424, 0.485, 0.566, 0.46, 0.48, 0.67, 0.66, 
       0.50, 0.50, 0.50, 0.50, 0.43, None, None, None]

OUT_inverse = [0.424, 0.485, 0.566, 0.50, 0.68, 0.68, 
               0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 
               None, None, None]

# Calculate percentage errors
ERROR_OUT = [
    round(abs(i-o)/i*100, 2) if o is not None else None 
    for i, o in zip(OUT_normal, OUT)
]

ERROR_OUT_inverse = [
    round(abs(i-o)/i*100, 2) if o is not None else None 
    for i, o in zip(OUT_normal, OUT_inverse)
]

# Create table
tableau = pd.DataFrame([
    L, 
    IN, 
    OUT, 
    OUT_inverse,
    ERROR_OUT,
    ERROR_OUT_inverse
])

# Create figure
fig, ax = plt.subplots(figsize=(18, 4))

ax.axis('off')

table = ax.table(cellText=tableau.values,
                 rowLabels=[
                     "Ratio to Q_in", 
                     "Input flow", 
                     "Output flow", 
                     "Output inverse flow",
                     "Error OUT (%)",
                     "Error OUT inverse (%)"
                 ],
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(8)

table.scale(1, 2)

plt.savefig("tableau_flux.png", dpi=300, bbox_inches="tight")

plt.close()