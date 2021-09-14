import statistics
import math
num = [1005,963,1035,1027,1281,1272,1051,1079,1034,1070,1173,1079,1067,1104,1347,1439,1029,1100,1204,1160]
num.sort()
media = sum(num)/ len(num)
mediana = statistics.median(num)
moda = statistics.mode(num)
variancia = statistics.variance(num)
DesvioPadrao = math.sqrt(variancia)

print("A Média é: {:0.2f}".format(media))
print("A Mediana é: {:0.2f}".format(mediana))
print("A Moda é: {:0.2f}".format(moda))
print("A Variancia é: {:0.2f}".format(variancia))
print("A Desvio-Padrão é: {:0.2f}".format(DesvioPadrao))