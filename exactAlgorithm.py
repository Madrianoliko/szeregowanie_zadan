from itertools import permutations
import time


def exactAlgorithm(arrayOfTasks, arrayOfProcessors, m):
    exactAlgorithmTime = time.time()
    arrayOfPermutations = list(permutations(arrayOfTasks))
    arrayOfSolutions = []
    for i in arrayOfPermutations:
        p = 0
        for j in i:
            arrayOfProcessors[p] += j
            p = p + 1
            if p == int(m):
                p = 0
        arrayOfSolutions.append(max(arrayOfProcessors))
        for index, i in enumerate(arrayOfProcessors):
            arrayOfProcessors[index] = 0

    print("\nAlgorytm dokładny")
    print("Minimalny czas rozwiązania to:", min(arrayOfSolutions))
    index = arrayOfSolutions.index(min(arrayOfSolutions))
    print("Szeregowanie zadań dla procesorów zgodnie z permutacją:", arrayOfPermutations[index])
    endOfExactAlgoritghmTime = time.time()
    exactAlgorithmDifference = endOfExactAlgoritghmTime - exactAlgorithmTime
    print("Wykonuje sie w %.10f" % exactAlgorithmDifference, "sekund\n")
    return exactAlgorithmDifference
