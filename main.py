from setup import setup
from exactAlgorithm import exactAlgorithm
from heuristicAlgorithm import heuristicAlgorithm
import matplotlib.pyplot as plt

numberOfProcessors = 2

tasks = []
heuristicTime = []
exactTime = []

for i in range(1, 5):
    numberOfTasks = i
    tasks.append(i)

    arrayOfTasks, arrayOfProcessors = setup(numberOfTasks, numberOfProcessors)
    heuristicTime.append(heuristicAlgorithm(arrayOfTasks, arrayOfProcessors))
    exactTime.append(exactAlgorithm(arrayOfTasks, arrayOfProcessors, numberOfProcessors))

plt.plot(tasks, heuristicTime, label="heuristic algorithm")
plt.plot(tasks, exactTime, label="exact algorithm")
plt.ylabel("seconds")
plt.xlabel("tasks")
plt.legend()
plt.show()