


def minDistance(word1, word2):

    memo = {}

    def dp(index1, index2, word):

        if word == word2:
            return 1
        
        if index1 >= len(word1) and index2 >= len(word2):
            return 0

        if index1 >= len(word1):
            index1 = len(word1)-1
        if index2 >= len(word2):
            index2 = len(word2)-1
        

        if index1 == index2:
            return dp(index1+1, index2+1, word)
        else:

            dp(index1, index2+1 , word[:index1] + word2[index2] + word[index1:])
            dp(index1 +1, index2, word[:index1] + word[index1:])
            dp(index1+1, index2+1,  word[:index1] + word2[index2] + word[index1+1:])
    
    return dp(0,0, word1)


            



word1 = "horse"
word2 = "ros"

print(minDistance(word1, word2))



        
