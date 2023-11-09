

- initialize the pointers, add characters to array then join 
1. While Loop  - iterate over each of the words, while in bounds, and add to list 
2. append each of the characters to a list
3. Add to the counter
4. ensure all of the characters are added by appending (by index) any remaining characters
5. join all of the characters together in the list 


    def mergeAlternately(self, word1, word2):
        i, j = 0, 0

        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1
            j += 1

        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
