"""
    LeetCode: 739. Daily Temperatures
    Link: https://leetcode.com/problems/daily-temperatures/
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """

    Key Points:
    Need to wait at least next temp to know days to wait -> store temps

    Algo 1:
    Iterate over temperatures and for each temp keep track of a counter.
    Increment counter if next temp is higher.


    Temps: [73, 74, 75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
    """

    days = [0] * len(temperatures)
    for i in range(len(temperatures)):
        curr = temperatures[i]
        count = 0
        for temp in temperatures[i:]:
            if temp > curr:
                days[i] = count
                break
            count += 1
    return days


# Driver


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
expected = [1, 1, 4, 2, 1, 1, 0, 0]
result = dailyTemperatures(temperatures)
print(result == expected)
