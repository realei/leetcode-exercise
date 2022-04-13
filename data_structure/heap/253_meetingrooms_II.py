"""
[会员题目]
给你一个会议时间安排的数组 intervals ，
每个会议时间都会包括开始和结束的时间 
intervals[i] = [start^{i}, end^{i}] ，
返回所需会议室的最小数量。

Example 1:
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2

Example 2:
输入：intervals = [[7,10],[2,4]]
输出：1

算法:

1. 按照 开始时间 对会议进行排序。
2. 初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
3. 对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
    (1)若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
    (2)若房间不空闲。开新房间，并加入到堆中。
4.处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。

复杂度分析

* 时间复杂度：O(N\log N)

    - 时间开销主要有两部分。第一部分是数组的 排序 过程，消耗 O(N\log N)O(NlogN) 的时间。数组中有 NN 个元素。

    - 接下来是 最小堆 占用的时间。在最坏的情况下，全部 N 个会议都会互相冲突。在任何情况下，我们都要向堆执行N次插入操作。在最坏的情况下，我们要对堆进行N次查找并删除最小值操作。总的时间复杂度为(NlogN)，因为查找并删除最小值操作只消耗O(logN) 的时间。

* 空间复杂度：O(N) 。额外空间用于建立 最小堆 。在最坏的情况下，堆需要容纳全部 NN 个元素。因此空间复杂度为 O(N)
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
