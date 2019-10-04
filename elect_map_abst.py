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

plt.close()

src2 = "https://www.eleicoes.mai.gov.pt/legislativas2015/territorio-nacional.html"

part = [0.5631, 0.5777, 0.6021, 0.4723, 0.5746, 0.5633, 0.5990, 0.5138, 0.5229, 0.5626, 0.606, 0.5831, 0.6030, 0.5787, 0.5833, 0.5074, 0.4826, 0.5128, 0.4890, 0.4122, 0.1743, 0.0893]

dic_mp_eleit = zip(dist, deputados, eleitores, nelp, part)

vot = []

for d in dic_mp_eleit:
    vot_prev = int(d[3]*d[4])
    print(d[0], " -- Número de votantes por deputado: ", vot_prev)
    vot.append(vot_prev)

dic_mp_eleit = zip(dist, deputados, eleitores, nelp, part, vot)

plt.barh(y_pos, vot, align='center', alpha=0.75)
plt.yticks(y_pos, dist)
plt.xlabel('Número de Votantes')
plt.title('Número de Votantes Previsto por Círculo Eleitoral e por Deputado Eleito')


plt.savefig("num_deputdos_circ_eleitoral_votantes.png", dpi=300, bbox_inches='tight')

plt.close()
