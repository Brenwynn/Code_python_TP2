import glob
import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits


#-------------------------------
# PARTIE TEST : DARKS
#-------------------------------

# START : comparaison du début de pose image 1 vs image 2
print("------------------------------")
print("START")

folder_path = "C:/Users/33778/Desktop/OSAE/TPs/TP2/03-10-2024/"

darkPattern = os.path.join(folder_path, "brut/Test-mux-Oct3-2024-*-dark-75ms.fits") # '*' pour représenter la partie variable, ici: 1633 

# Liste des fichiers de dark
darkFiles = glob.glob(darkPattern)

tmp=fits.getdata(darkFiles[0])
startReference = tmp[0,0,0:127,128:255]  # Début de la pose image 1
startImage = tmp[1,0,0:127,128:255]  # Début de la pose image 2

# Calcul de la différence et statistiques
startDiff = startImage - startReference
avg = np.mean(startDiff) / np.sqrt(2)
rms = np.sqrt(np.mean(np.square(startDiff))) / np.sqrt(2)

print(f"Moyenne de la différence : {avg}")
print(f"RMS de la différence : {rms}")

# Placeholder pour dessiner la palette
# pli, sigma_filter(diff, 3) 
# sigma_filter doit être définie

print("------------------------------") # Fin de la première section

# Deuxième section de l'analyse
# END : comparaison de la fin de pose image 1 vs image 2
print("END")
endReference = tmp[0, 1,0:127,128:255]  # Fin de la pose image 1
endImage = tmp[1, 1,0:127,128:255]  # Fin de la pose image 2

# Calcul de la différence et statistiques
endDiff = endImage - endReference
avg = np.mean(endDiff) / np.sqrt(2)
rms = np.sqrt(np.mean(np.square(endDiff))) / np.sqrt(2)

print(f"Moyenne de la différence : {avg}")
print(f"RMS de la différence : {rms}")

# Placeholder pour dessiner la palette
# pli, sigma_filter(diff, 3) 
# sigma_filter doit être définie

print("------------------------------") # Fin de la deuxième section

#Troisième section de l'analyse 
print("END - START")
endStartReference = tmp[0,1,0:127,128:255]-tmp[0,0,0:127,128:255] # Fin - début image 1
endStartImage = tmp[1,1,0:127,128:255]-tmp[1,0,0:127,128:255] # Fin - début image 2


# Calcul de la différence et statistiques
startEndDiff = endStartImage - endStartReference
avg = np.mean(startEndDiff) / np.sqrt(4)
rms = np.sqrt(np.mean(np.square(startEndDiff))) / np.sqrt(4)
print(f"Moyenne de la différence : {avg}")
print(f"RMS de la différence : {rms}")

# #Affichage des images START
# plt.figure()
# plt.title("Start REF")
# plt.imshow(startReference)
# plt.figure()
# plt.title("Start IMAGE")
# plt.imshow(startImage)
# plt.figure()
# plt.title("Start DIFF")
# plt.imshow(startDiff)
# plt.colorbar()
# plt.show()

#-------------------------------
# PARTIE 3ms
#-------------------------------

print("--------------------------------")
print("PARTIE 3ms")
print("--------------------------------")

pattern = os.path.join(folder_path, "3ms/Test-nicmos-Oct3-2024-*-H-*ms.fits")
files_3ms = glob.glob(pattern)

# Initialisation des tableaux
slopes = np.zeros((256, 256), dtype=float)
offset = np.zeros((256, 256), dtype=float)

# Fonction pour lire les fichiers FITS et effectuer les calculs
def process_file(file):
    tmp = fits.getdata(file)  
    tmp2 = tmp[:, 1, :, :] - tmp[:, 0, :, :]  #fin-Debut de toute les images -->(100,256,256)
    avg_im = np.mean(tmp2, axis=0) # Moyenne
    var_im = np.var(tmp2, axis=0) # Variance
    return avg_im, var_im

# Traitement des fichiers avec les motifs définis
avg_im75, var_im75 = process_file(files_3ms[0])
avg_im90, var_im90 = process_file(files_3ms[1])
avg_im110, var_im110 = process_file(files_3ms[2])
avg_im173, var_im173 = process_file(files_3ms[3])
avg_im277, var_im277 = process_file(files_3ms[4])
avg_im485, var_im485 = process_file(files_3ms[5])

plt.figure(figsize=(12, 8))

# Calcul des pentes et des offsets
for i in range(256):
    for j in range(256):
        x = [avg_im75[i, j], avg_im90[i, j], avg_im110[i, j], avg_im173[i, j], avg_im277[i, j], avg_im485[i, j]]
        y = [var_im75[i, j], var_im90[i, j], var_im110[i, j], var_im173[i, j], var_im277[i, j], var_im485[i, j]]
        # Régression linéaire (calcul des pentes et des offsets)
        A = np.vstack([np.ones(len(x)), x]).T
        line = np.linalg.lstsq(A, y, rcond=None)[0]
        offset[i, j] = line[0]
        slopes[i, j] = line[1]


# Affichage des informations
print("Slopes Info:", slopes)
print("Offset Info:", offset)

# Calcul de la moyenne des pentes et des offsets
avg_slopes = np.mean(slopes)
avg_offset = np.mean(offset)

print("Moyenne des pentes:", avg_slopes)
print("Moyenne des offsets:", avg_offset)



#Tracé régression linéaire
i=100
j=1
x = [
    avg_im75[i, j], 
    avg_im90[i, j], 
    avg_im110[i, j], 
    avg_im173[i, j], 
    avg_im277[i, j], 
    avg_im485[i, j]
]
y = [
    var_im75[i, j], 
    var_im90[i, j], 
    var_im110[i, j], 
    var_im173[i, j], 
    var_im277[i, j], 
    var_im485[i, j]
]
# Créer des points pour tracer la ligne de régression
# Régression linéaire (calcul des pentes et des offsets)
A_pixel = np.vstack([np.ones(len(x)), x]).T
line_pixel = np.linalg.lstsq(A_pixel, y, rcond=None)[0]
x_fit_pixel = np.linspace(min(x), max(x), 100)
y_fit_pixel = line_pixel[0] + line_pixel[1] * x_fit_pixel

# Tracer les points de moyenne/variance pour le pixel
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Points (Moyenne vs Variance)')  # Points
plt.plot(x_fit_pixel, y_fit_pixel, color='red', label='Ligne de Régression', linewidth=2)  # Ligne de régression

# Labels et affichage du graphique
plt.xlabel('Moyenne des Images')
plt.ylabel('Variance des Images')
plt.title(f'Moyenne vs Variance pour le Pixel ({i}, {j})')
plt.grid(True)
plt.legend()
plt.show()