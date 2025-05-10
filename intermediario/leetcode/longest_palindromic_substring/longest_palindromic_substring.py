def longestPalindrome(s):
    
    center = 0

    start = 0
    end = 0

    n= len(s)

    while center < len(s):

        if (2 * min(center, n - center - 1) + 1) + 1 < start - end + 1:
            break

        left = center
        right = center + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1

        if (end - start + 1) < (right - 1 - left + 1 - 1):
            start = left + 1
            end = right - 1

        print(start, end, s[start:end+1])


        left = center
        right = center

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1

        if (end - start + 1) < (right - 1 - left + 1 - 1):
            start = left + 1
            end = right - 1
        
        center+=1

        print(start, end, s[start:end+1])

    return s[start:end+1]

s = "babad"

print(longestPalindrome(s))
        



