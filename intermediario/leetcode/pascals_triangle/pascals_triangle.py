

def generate(numRows):

    pascal_triangle = [[]] * numRows

    pascal_triangle[0] = [1]

    def generate_row(row):

        previous = pascal_triangle[row -1]

        ptr = [0] * (row + 1)

        ptr[0] = previous[0]
        ptr[row] = previous[row-1]

        for i in range(1, row):
            ptr[i] = previous[i] + previous[i-1]
        
        return ptr


    for i in range(1, numRows):
        pascal_triangle[i] = generate_row(i)
    
    return pascal_triangle



print(generate(5))
print(generate(1))


        
        

