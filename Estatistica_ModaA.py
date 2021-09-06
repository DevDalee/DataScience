import random
import statistics

num = [random.randint(1,5) for x in range(1,10) ]
moda = statistics.mode(num)
print(num)
print(moda)