"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        # for i in sorted_intervals:
        #     print(i.start, i.end)
        #print(sorted_intervals)
        heap = []
        heapq.heapify(heap)
        ans = 1
        #earliest_end = float('inf')

        for i in range(len(sorted_intervals)-1):
            heapq.heappush(heap, sorted_intervals[i].end)
            if (heap[0] > sorted_intervals[i+1].start):
                ans += 1
            else:
                heapq.heappop(heap)

        return ans
            