

1. create a hashmap 
2. iterate over the list and add each item to the dictionary
3. create a set for the items
4. iterate over the dictionary's values & if they are in the set return False, else add them 
5. if not then return True


   def uniqueOccurrences(self, arr):
        count_dict = defaultdict(int)

        for i in arr:
            count_dict[i] += 1

        items = set()
        for freq in count_dict.values():
            if freq in items:
                return False
            else:
                items.add(freq)
        return True
