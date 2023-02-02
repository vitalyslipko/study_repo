import random
from random_words import RandomWords
import time

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0, 100))
    str_list.append(w.random_words())

def selection(data):
    for i in range(len(data)):
        minIndex = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minIndex]:
                minIndex = j
        if minIndex != i:
            data[i], data[minIndex] = data[minIndex], data[i]

def average(data):
    avg = []
    for i in range(10):
        start = time.time()
        selection(data)
        end = time.time() - start
        avg.append(end)
    print("Average is: ", sum(avg) / len(avg))
average(int_list)
average(str_list)
average(float_list)
