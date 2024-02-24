"""
 * Review
 - 1st : 02/22/24
"""

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

intervals.sort(key=lambda x: x[0])

# print(intervals)
merged = []

for i in range(0, len(intervals) - 1):
    if i[1] > i + 1[1]:
        merged.append([i[0], i + 1[1]])
