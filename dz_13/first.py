import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0, 100))
    str_list.append(w.random_words())

print(int_list)
print(float_list)
print(str_list)
