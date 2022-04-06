"""
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

实现 MovingAverage 类：

MovingAverage(int size) 用窗口大小 size 初始化对象。
double next(int val) 计算并返回数据流中最后 size 个值的移动平均值。


输入：
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]

解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/moving-average-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Q1: check url: https://blog.csdn.net/weixin_39986952/article/details/84842567
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        self.nums.append(val)
        return sum(self.nums[-self.size:])/min(self.size, len(self.nums))


# class MovingAverage:
#     def __init__(self, size: int):
#         self.size = size
#         self.queue = []
        
#     def next(self, val: int) -> float:
#         size, queue = self.size, self.queue
#         queue.append(val)
#         # calculate the sum of the moving window
#         window_sum = sum(queue[-size:])

#         return window_sum / min(len(queue), size)
