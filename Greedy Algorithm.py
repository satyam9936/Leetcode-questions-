#chess- based on possible outcomes chess pieces changes
#volleyball/ footbal- maximize score 

# greedy algorithm- optimal choice 
'''1- grredy choice 
2-optimal substraction- if we have local optimal solution-global optimal
 capacity=50kg 
'''
  # fractional knapsack problm'''
#leetcode 781
from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #create hashmap
      from collections import defaultdict
      freq_map= defaultdict(int)
      for ans in answers:
        freq_map[ans]+=1
        output=0
        for k, value in freq_map.items():
          q=value//(k+1)
          r=value%(k+1)
          q+=1 if r>0 else 0
          output += q*(k+1)
        return output
      
    # activity selection problem
    

        


