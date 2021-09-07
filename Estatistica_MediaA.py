import random 
p=0
num = [random.randint(0,9) for p in range(0,10)]

media = sum(num) / len(num)
print(num)
print(media)