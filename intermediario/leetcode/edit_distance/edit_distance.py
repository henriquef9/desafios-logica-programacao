


def minDistance(word1, word2):

    memo = dict()

    def bt(i,j):

        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if word1[i] == word2[j]:
            memo[(i, j)] = bt(i + 1, j + 1)
        else:
            insert = 1 + bt(i, j + 1)
            delete = 1 + bt(i + 1, j)
            replace = 1 + bt(i + 1, j + 1)
            memo[(i, j)] = min(insert, delete, replace)

        return memo[(i, j)]

    return bt(0, 0)

            



word1 = "intention"
word2 = "execution"

print(minDistance(word1, word2))



        
