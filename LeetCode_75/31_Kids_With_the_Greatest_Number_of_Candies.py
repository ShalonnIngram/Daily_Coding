
1. create a variable for the max number of candies
2. iteratie over the list of number of candies
3. if the number in candies + the extra candies >= the max number of candies set the index to True, else False
4. return the list 

    def kidsWithCandies(self, candies, extraCandies):

        max_candies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies

