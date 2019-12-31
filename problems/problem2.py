"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def problem2(inputA):
    if len(inputA) == 1:
        return [0]

    newArry = []

    for i in range(len(inputA)):
        result = inputA[0]
        for j in range(1, len(inputA)):
            result *= inputA[j]

        result /= inputA[i]
        newArry.append(int(result))

    return newArry

def problem2WithoutDivision(inputA):
    if len(inputA) == 1:
        return [0]

    newArry = []

    for i in range(len(inputA)):
        tArr = inputA.copy()
        tArr.remove(inputA[i])
        result = tArr[0]
        for i in range(1, len(tArr)):
            result *= tArr[i]
        newArry.append(result)

    return newArry


arr = []
length = int(input("How many values are in the array? "))

for i in range(length):
    arr.append(int(input("Value #{} ".format(i+1))))

arr = [0, 1, 2]
print(arr)
print(problem2(arr)) # better if input does not contain a zero
print(problem2WithoutDivision(arr)) # better if input has a zero




