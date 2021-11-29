from numpy.random import rand
import numpy as np
import random


def object(data, iter):
    sum = 0
    for i in range(len(data)-1):
        iter +=1
        sum += data[i]**2
    return sum, iter

"""
    Description:
    function which can be called objective take square of value that came from out,then 
    increasing iteration for check if it is  out of bounded domain
     
    
    Paramters:
    data: It's array named person that came from search algorithm fuction.
    iter: It's integer float.
    
    Return:
    it is taken square of data,and addition results to variable,then iter is increased as per transaction,then
    those results is returned.
"""



def randomSearch(individual=10, countOfPopulation=15 ,min=-10, max=10, countOfTransaction=100000):

    # Travel  within   individual
    temp = 0
    # It's a matrix that keeps all values
    original= np.arange(individual*(countOfPopulation+1)).reshape(individual, countOfPopulation+1).astype(float)
    # Calculating of max iteration's count
    maxIteration = countOfTransaction / countOfPopulation
    # Travelling to checking if iteration achieve to maximum iteration
    iter = 0
    # Generation randomly individual
    sample = np.random.uniform(min,max,countOfPopulation)
    # Constant fbest value
    fbest= 0
    # Template fbest value
    fbestg = 0
    while individual > 0:
        # rate of amount of changing
        delta = random.randint(0, 10)
        for i in range(len(sample)):
            if(individual == 10):
                original[temp][i] = sample[i]
            else:
                # Rate Of Current Variable
                rateOfCurrentVariable = (original[temp-1][i] * (delta)/100)
                # subtraction from original value
                subtraction = original[temp-1][i] - rateOfCurrentVariable
                # addition from original value
                addition = original[temp-1][i] + rateOfCurrentVariable
                # Generated Random Number Through Between Stated Interval
                generatedRandomNumberThroughStatedInterval =random.uniform(subtraction, addition)
                # Switch off between previous value and updated value
                original[temp][i] =generatedRandomNumberThroughStatedInterval
        print('Original matrix:',original)
        if (individual == 10):
            # Those're sended to object function to finding proper value
            fbest,iter= object(original[temp],iter)
            # It's assigned fbest ,that has been calculated from objective function, to end of individual array in matrix
            original[temp][-1] = fbest
            print('fbest at first iteration',original[temp][-1])
            print('original at first iteration', original)

        elif(iter < maxIteration):
            # Those're sended to object function to finding proper value
            fbestg, iter = object(original[temp], iter)
            # It's assigned fbest ,that has been calculated from objective function, to end of individual array in matrix
            original[temp][-1] = fbestg
            # If previous fbest is smaller then further.
            if(original[temp-1][-1] < original[temp][-1]):
                fbestg = fbest
                # It's printed.
                print('fbest', original[temp][-1])
                # Switch between previous array and current.
                for i in range(len(original[temp])):
                    original[temp][i] = original[temp - 1][i]
        else:
            print("Maximum iteration has been achieved.")

        # Individual count is decrased that means passed to futher individual.
        individual -= 1
        temp += 1

    print('Fbest is :', original[temp-1][-1])
    print('Decision variable is:', original[temp-1])


"""
    Description:
    Random search is transaction of searching optimum value in bounded domain.

    Parameters:
    individual: It's dimension of dataset.
    min and max: It's interval values those are able to choosen.
    countOfPopulation: It's count of population
    countOfTransaction: It's maximum count of transation
    
    Return:
    None
"""


def main():
    randomSearch()

if __name__ == '__main__':
    main()