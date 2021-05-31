import random


def setup(numberOfTasks, numberOfProcessors):
    arrayOfTasks = []
    arrayOfProcessors = []

    for i in range(0, int(numberOfTasks)):
        arrayOfTasks.append(random.randint(1, 1000))

    for i in range(0, int(numberOfProcessors)):
        arrayOfProcessors.append(0)

    return arrayOfTasks, arrayOfProcessors
