#leetcode 452
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int: # TC= O(nlogn)
        points.sort(key=lambda x:x[1])
        arrow_pos=points[0][1]
        arrow_count=1

        for i in range (1,len(points)):
            if arrow_pos>=points[i][0]:
                continue
            arrow_count+=1
            arrow_pos= points[i][1]
            
        return arrow_count