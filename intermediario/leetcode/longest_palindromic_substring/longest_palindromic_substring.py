def longestPalindrome(s):
    
    center = 0

    start = 0
    end = 0

    while center < len(s):

        left = center
        right = center

        if center + 1 < len(s) and s[center] == s[center+1]:
            right+=1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1

        if (end - start + 1) < (right - 1 - left + 1 - 1):
            start = left + 1
            end = right - 1

        print(start, end, s[start:end+1])


        left = center
        right = center
        if center - 1 >= 0 and center + 1 < len(s) and s[center - 1] == s[center + 1]:
            right+=1
            left-=1
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
        



