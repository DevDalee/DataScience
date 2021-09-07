num = []
for x in range(0,10):
    num.append(int(input()))
ordNum = sorted(num)
QNum = len(num)
if QNum % 2 == 0:
    med = (ordNum[int(QNum/2)] + ordNum[int(QNum/2-1)])/2.0
else: 
    med = ordNum[int(QNum/2)]
print(num)
print("Mediana = {:0.2f}".format(med))
