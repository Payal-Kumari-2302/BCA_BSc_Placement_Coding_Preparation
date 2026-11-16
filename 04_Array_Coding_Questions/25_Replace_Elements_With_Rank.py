# Q25 - Replace Elements with Their Rank

# Problem:
# Replace each array element with its rank in sorted order.


# Solution:

arr = [40, 10, 20, 30]

sorted_arr = sorted(set(arr))

rank = {}

for i in range(len(sorted_arr)):
    rank[sorted_arr[i]] = i + 1

result = []

for num in arr:
    result.append(rank[num])

print("Rank Array:", result)


# Output:
# Rank Array: [4, 1, 2, 3]
