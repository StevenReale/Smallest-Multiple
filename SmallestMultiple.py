testNum = 20
#returns a dictionary with each prime factor of input from 2 through 20
def GetPrimeFactors(input):
    primeCount = {2: 0, 3: 0, 5: 0, 7:0, 11: 0, 13: 0, 17: 0, 19: 0}
    for prime in primeCount:
        newInput = input
        while True:
            if newInput % prime == 0:
                primeCount[prime] += 1
                newInput /= prime
            else:
                break
    return primeCount

#creates a blank roster list of prime factors 2 through 20
#iterates from 2 through input (max of 22). For each value, adds any prime factors to roster that do not already appear
def AllFactorCount(input):
    currentPrimeFactors = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19:0}
    incrementPrimeFactors = dict()
    for i in range(2, input+1):
        incrementPrimeFactors = GetPrimeFactors(i)
        print("determining prime factors of", i)
        print(incrementPrimeFactors)
        print(currentPrimeFactors)
        for j in currentPrimeFactors:
            if incrementPrimeFactors[j] > currentPrimeFactors[j]:
                print("increment greater than current. updating current")
                currentPrimeFactors[j] = incrementPrimeFactors[j]
    return currentPrimeFactors

#multiplies through all prime factors to determine final solution
def multPrimeFactors(factors):
    total = 1
    for j in factors:
        total *= j ** factors[j]
    return total
#che
allFactors = AllFactorCount(testNum)
print("\n The list of all prime factors of all integers from 2 through", testNum, "is: ", allFactors)
print("The smallest multiple of all of the integers from 2 through", testNum, "is:", multPrimeFactors(allFactors))
