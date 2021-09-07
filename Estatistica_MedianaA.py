import random 
p=0
num = [random.randint(0,9) for p in range(0,10)]
ordNum = sorted(num)
QNum = len(num)
if QNum % 2 == 0:
    med = (ordNum[int(QNum/2)] + ordNum[int(QNum/2-1)])/2.0
else: 
    med = ordNum[int(QNum/2)]
print(num)
print("Mediana = {:0.2f}".format(med))
