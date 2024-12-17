def numberSum(numbers):
    expectedSum = 5
    operations = 0
    i = 0
    j = i + 1
    while i < len(numbers):
        j = i + 1
        print("i and j at start of loop", i, j)
        while j < len(numbers):
            if numbers[i] + numbers[j] == expectedSum:
                operations += 1
                # Remove the two numbers that summed to 5.
                numbers.pop(j)
                numbers.pop(i)
                i = -1
                print("i = ", i, ", j = ", j, ", operations count is now", operations, "and numbers array is now:", numbers)
                break
            else: 
                j+= 1
            print("j is now ", j)
        i+= 1
        print("increment i at bottom of loop to ", i)
    return operations
print(numberSum([1,2,3,4,5,5,4,3,2,1]))