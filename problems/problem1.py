"""
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
arr = []
length = int(input("How many values are in the array? "))

for i in range(length):
    arr.append(int(input("Value #{} ".format(i+1))))

k = int(input("What is your k value? "))
arr.sort()

def locate(arr, l):
    i = 0; j = len(arr) - 1
    while i <= j:
        if arr[i] + arr[j] == k:
            return True
        elif arr[i] + arr[j] > k:
            j -= 1
        elif arr[i] + arr[j] < k:
            i += 1
    return False

print(locate(arr, k))
