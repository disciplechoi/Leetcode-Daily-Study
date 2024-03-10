"""
 * Review
 - 1st : 02/22/24
"""

# sol1)
# TC : O(nlogn)
# MC : O(len(intervals))

# [1,5], [2, 4] edge case remember!!
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

intervals.sort(key=lambda x: x[0])

# print(intervals)
output = [intervals[0]]

print(output[0][1])

for start, end in intervals[1:]:
    lastEnd = output[-1][1]

    if start < lastEnd:
        output[-1][1] = max(lastEnd, end)
    else:
        output.append([start, end])

return output
