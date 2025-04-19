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
            
# def lengthOfLongestSubstring(s):
    
#     max_length = 0
#     mapa = {}
#     count = 0
#     i = 0
#     while i < len(s):

#         if mapa.get(s[i]) != None:
#             count = 0
#             i = mapa[s[i]] + 1
#             mapa = {}
#             print(s[i])

#         count += 1
#         mapa[s[i]] = i
#         i += 1
#         if count > max_length:
#             max_length = count

#     return max_length
    

# def lengthOfLongestSubstring(s):
    
#     if not s:
#         return 0

#     max_length = 0

#     l = 0
#     r = 1

#     while l < len(s) and r < len(s):

#         for i in range(l, r):

#             if s[r] == s[i]:
#                 if max_length < r - l:
#                     max_length = r - l
#                 l = i + 1
#                 break
#         r += 1

#     if max_length < r - l:
#         max_length = r - l
  
#     return max_length
    

def lengthOfLongestSubstring(s):
    
    if not s:
        return 0

    max_length = 0

    l = 0
    r = 0
    mapa = {}

    while r < len(s):

        if mapa.get(s[r]) != None:
            while s[l] != s[r]:
                mapa.pop(s[l])
                l += 1
            mapa.pop(s[l])
            l += 1
            
        
        if max_length < r - l + 1:
            max_length = r - l + 1
        
        mapa[s[r]] = r 
        r += 1
        
    
  
    return max_length
    

# teste

s = "abba"

print(lengthOfLongestSubstring(s))