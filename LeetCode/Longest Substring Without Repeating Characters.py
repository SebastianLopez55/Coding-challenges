def lengthOfLongestSubstring(s):
    L, R = 0, 0
    tempS = ""
    longest = ""

    while R < len(s):
        if s[R] not in tempS:
            tempS += s[R]
            R += 1
        else:
            tempS = ""
            L += 1
            R = L
        if len(tempS) > len(longest):
            longest = tempS

    return len(longest)


print(lengthOfLongestSubstring(" "))
