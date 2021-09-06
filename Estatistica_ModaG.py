import statistics

num = []
for x in range(0,10):
    num.append(int(input()))
moda = statistics.mode(num)
print(num)
print(moda)