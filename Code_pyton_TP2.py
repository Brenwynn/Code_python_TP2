import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits


# Première section de l'analyse

# START : comparaison du début de pose image 1 vs image 2
print("------------------------------")
print("START")
tmp=fits.getdata("C:/Users/33778/Desktop/OSAE/TPs/TP2/03-10-2024/brut/Test-mux-Oct3-2024-1633-dark-75ms.fits")
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

#Affichage des images START
plt.figure()
plt.title("Start REF")
plt.imshow(startReference)
plt.figure()
plt.title("Start IMAGE")
plt.imshow(startImage)
plt.figure()
plt.title("Start DIFF")
plt.imshow(startDiff)
plt.colorbar()
plt.show()

