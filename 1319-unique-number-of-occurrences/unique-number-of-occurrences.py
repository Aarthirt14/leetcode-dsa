class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        if len(freq) == len(set(freq.values())):
            return True
        return False

            
        