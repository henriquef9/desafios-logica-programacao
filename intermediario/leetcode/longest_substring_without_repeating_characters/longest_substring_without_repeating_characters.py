# def lengthOfLongestSubstring(s):
    
#     max_length = 0
    
#     for i in range(len(s)):
#         mapa = {}
#         count = 0
#         for j in range(i, len(s)):

#             if mapa.get(s[j]) != None:
#                 break

#             mapa[s[j]] = j
#             count += 1

#         if count > max_length:
#             max_length = count
    
#     return max_length
            
def lengthOfLongestSubstring(s):
    
    max_length = 0
    mapa = {}
    count = 0
    i = 0
    while i < len(s):

        if mapa.get(s[i]) != None:
            count = 0
            i = mapa[s[i]] + 1
            mapa = {}
            print(s[i])

        count += 1
        mapa[s[i]] = i
        i += 1
        if count > max_length:
            max_length = count

    return max_length
    


s = "dvdf"

print(lengthOfLongestSubstring(s))