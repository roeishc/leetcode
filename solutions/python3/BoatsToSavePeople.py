class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        boats: int = 0
        people.sort()
        heavy = len(people) - 1
        light = 0

        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
            boats += 1
            heavy -= 1
        
        return boats
