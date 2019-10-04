#!/usr/bin/python

import pylab
import numpy as np
import matplotlib.pyplot as plt

src = "http://www.cne.pt/sites/default/files/dl2019/_ar_mapa_deputados.pdf"

dist = ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo", "Vila Real", "Viseu", "Madeira", "Açores", "Europa", "Fora da Europa"]

deputados = [16, 3, 19, 3, 4, 9, 3, 9, 3, 10, 48, 2, 40, 9, 18, 6, 5, 8, 6, 5, 2, 2]

eleitores = [645747, 123032, 778359, 141587, 170152, 380064, 136725, 376882, 151557, 415359, 1921189, 96425, 1595205, 380976, 737285, 240942, 219112, 348016, 257897, 228975, 895515, 570435]

dic_mp_eleit = zip(dist, deputados, eleitores)

nelp=[]

print (dic_mp_eleit)

for d in dic_mp_eleit:
    ned = int(d[2]/d[1])
    print(d[0], " -- Número de eleitores por deputado: ", ned)
    nelp.append(ned)

dic_mp_eleit = zip(dist, deputados, eleitores, nelp)

y_pos = np.arange(len(dist))

plt.barh(y_pos, nelp, align='center', alpha=0.75)
plt.yticks(y_pos, dist)
plt.xlabel('Número de Eleitores')
plt.title('Número de Eleitores no Círculo Eleitoral por Deputado Eleito')


plt.savefig("num_deputdos_circ_eleitoral.png", dpi=300, bbox_inches='tight')
