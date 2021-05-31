import time


def heuristicAlgorithm(arrayOfTasks, arrayOfProcessors):
    heuristicAlgorithmTime = time.time()

    arrayOfTasks.sort(reverse=True)
    for i in arrayOfTasks:
        index = arrayOfProcessors.index(min(arrayOfProcessors))
        arrayOfProcessors[index] += i

    print("\nAlgorytm heurystyczny")
    print("Minimalny czas rozwiązania to:", max(arrayOfProcessors))
    print("Szeregowanie zadań dla procesorów zgodnie z permutacją:", arrayOfTasks)
    endOfHeuristicAlgoritghmTime = time.time()
    heuristicAlgorithmDifference = endOfHeuristicAlgoritghmTime - heuristicAlgorithmTime
    print("Wykonuje sie w %.10f" % heuristicAlgorithmDifference, "sekund\n")

    return heuristicAlgorithmDifference
