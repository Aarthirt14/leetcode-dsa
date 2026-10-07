class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boat=0
        left=0
        right=len(people)-1

        while left<=right:
            if people[right] == limit:
                boat+=1
                right-=1
            elif people[left] + people[right] > limit:
                boat+=1
                right-=1
            elif people[left] + people[right] <= limit:
                boat+=1
                left+=1
                right-=1
            elif people[left]==people[right]:
                boat+=1
        return boat


        