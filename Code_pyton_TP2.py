import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits


# Première section de l'analyse

# START : comparaison du début de pose image 1 vs image 2

print("Start")
tmp=fits.getdata("C:/Users/33778/Desktop/OSAE/TPs/TP2/03-10-2024/Test-mux-Oct3-2024-1408-dark-173ms.fits")
reference = tmp[0,0,0:127,128:255]  # Début de la pose image 1
print("Reference image : ", reference)

plt.figure()
plt.imshow(reference)
plt.colorbar()
plt.show()

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
# END : comparaison de la fin de pose image 1 vs image 2

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

