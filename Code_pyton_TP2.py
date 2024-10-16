import glob
import numpy as np
from astropy.io import fits
#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj

#oezfboibezf

# Trouver les fichiers qui correspondent à "*1225*.fits"
# listfiles = glob.glob("/C:/Users/smeju/Desktop/MASTER_OSAE/TP/TP2/03-10-2024/*1225*.fits")
# print("Fichiers trouvés : ", listfiles)
# Lire le premier fichier FITS trouvé pas utile pour l'instant mais a creuser pour simplifier la rerche du fichier a traiter
# with fits.open("C:/Users/smeju/Desktop/MASTER_OSAE/TP/TP2/03-10-2024/brut/Test-mux-Oct3-2024-1633-dark-75ms.fits") as hdul:
#     tmp = hdul[0].data
#     print("Données du fichier FITS : ", tmp)

# Première section de l'analyse
# On compare start de 2  images

print("Start")
tmp=fits.getdata("C:/Users/smeju/Desktop/MASTER_OSAE/TP/TP2/03-10-2024/brut/Test-mux-Oct3-2024-1633-dark-75ms.fits",ext=0)
reference = tmp[0, 0,1:128,129:256]  # Début de la pose image 1
print("Reference image : ", reference)

image = tmp[1, 0,1:128,129:256]  # Début de la pose image 2
print("Image : ", image)

# Calcul de la différence et statistiques
diff = image - reference
avg = np.mean(diff) / np.sqrt(2)
rms = np.sqrt(np.mean(np.square(diff))) / np.sqrt(2)

print(f"Moyenne de la différence : {avg}")
print(f"RMS de la différence : {rms}")

# Placeholder pour dessiner la palette
# pli, sigma_filter(diff, 3) 
# sigma_filter doit être définie

# Fin de la première section
print("End")

# Deuxième section de l'analyse
# On compare end de deux images

reference = tmp[0, 1,1:128,129:256]  # Fin de la pose image 1
image = tmp[1, 1,1:128,129:256]  # Fin de la pose image 2

# Calcul de la différence et statistiques
diff = image - reference
avg = np.mean(diff) / np.sqrt(2)
rms = np.sqrt(np.mean(np.square(diff))) / np.sqrt(2)

print(f"Moyenne de la différence : {avg}")
print(f"RMS de la différence : {rms}")

# Placeholder pour dessiner la palette
# pli, sigma_filter(diff, 3) 
# sigma_filter doit être définie

