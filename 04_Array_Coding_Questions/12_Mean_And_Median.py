# Q12 - Find Mean and Median

# Problem:
# Calculate the mean and median of an array.


# Solution:

arr = [1, 2, 3, 4, 5]

# Mean

mean = sum(arr) / len(arr)

# Median

arr.sort()

n = len(arr)

if n % 2 == 0:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

else:
    median = arr[n // 2]

print("Mean:", mean)
print("Median:", median)


# Output:
# Mean: 3.0
# Median: 3
