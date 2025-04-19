
def findMedianSortedArrays(nums1, nums2):

    m = len(nums1)
    n = len(nums2)    
 
    arr_merged = []

    p1 = 0
    p2 = 0

    pos = (m + n) // 2

    while len(arr_merged) < pos + 1:

        if not p1 >= m and not p2 >= n and nums1[p1] < nums2[p2]:
            arr_merged.append(nums1[p1])
            p1 += 1 
        elif not p1 >= m and not p2 >= n and nums2[p2] < nums1[p1]:
            arr_merged.append(nums2[p2])
            p2 += 1
        elif not p1 >= m and not p2 >= n:
            arr_merged.append(nums1[p1])
            arr_merged.append(nums2[p2])
            p1 += 1
            p2 += 1
        else:
            if not p1 >= m:
                arr_merged.append(nums1[p1])
                p1 += 1
            if not p2 >= n:
                arr_merged.append(nums2[p2])
                p2 += 1
    
    mediana = 0

    if (m + n) % 2 == 0:
        mediana = (arr_merged[pos] + arr_merged[pos - 1]) / 2
    else:
        mediana = arr_merged[pos]


    return mediana
        
# teste
        
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]

print(findMedianSortedArrays(nums1, nums2))