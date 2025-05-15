def combine(n, k):
    
    output = []

    def bt(partial):

        if k == len(partial):
            output.append(partial[:])
        else:

            first_element = 1 if len(partial) == 0 else partial[-1] + 1

            for i in range(first_element, n+1):
                partial.append(i)
                bt(partial)
                partial.pop(-1)
        
    
    bt([])
    return output


print(*combine(4,2))